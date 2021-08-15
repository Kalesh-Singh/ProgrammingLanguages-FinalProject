#!/usr/bin/env python2

from collections import namedtuple

from symbol_table import SymbolTable

## This file sets up the datatypes for representing an intermediate
## language. You will likely not need to make changes to this file
## but you will likely need to make use of these types.

class IlGenException(Exception): pass

def indent(s, amt):
    return '\n'.join(' '*amt+line for line in s.split('\n'))

ModulesTuple = namedtuple("Modules", ("modules"))
class Modules(ModulesTuple):
    '''Modules represents all loaded modules.'''

    def __new__(cls):
        self = super(Modules, cls).__new__(cls, dict())
        return self

    def lookup_module(self, name):
        '''find a module from its name'''
        return self.modules[name]

    def lookup(self, fn):
        '''find a function from its ref'''
        return self.lookup_module(fn.module).lookup(fn)

    def add(self, module):
        '''add a new module'''
        self.modules[module.name] = module
        return self

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        lines = list()
        lines.append("modules {")
        for mod in self.modules.itervalues():
            lines.append(indent(str(mod), 2))
        lines.append("}")
        return '\n'.join(lines)


ModuleTuple = namedtuple("Module", ('name', 'functions'))
class Module(ModuleTuple):
    '''A module represents a named collection of functions'''

    def __new__(cls, name):
        self = super(Module, cls).__new__(cls, name, list())
        return self

    def new_function(self, name, type, params=None, parent=None, freevars=None):
        '''create a new function in this module'''
        fn = Function(self.name, len(self.functions), name, type, params, parent, freevars)
        self.functions.append(fn)
        return fn

    def lookup(self, fn_ref):
        '''find a function from its ref'''
        if fn_ref.module != self.name:
            raise IlGenException(
                "unexpected module in fn lookup {}: {}".format(fn_ref, self.name))
        return self.functions[fn_ref.id]

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        lines = list()
        lines.append("module {} {{".format(self.name))
        for fn in self.functions:
            lines.append(indent(str(fn), 2))
        lines.append("}")
        return '\n'.join(lines)


ParamTuple = namedtuple("Param", ('id', 'name', 'type'))
class Param(ParamTuple):
    ''' represents a function paramater declaration '''

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '{}'.format(self.name)

## Represents the labels that you can jump to in a labeled loop
LabeledLoop = namedtuple("LabeledLoop", ("continue_blk", "exit_blk"))

FunctionTuple = namedtuple(
    "Function",
    ('module', 'id', 'name', 'params', 'parent', 'freevars', 'blocks'))
class Function(FunctionTuple):
    ''' 
    this represents a compiled ir function. it is a control flow graph
    of basic blocks.
    '''

    def __new__(cls, module, id, name, type, params=None, parent=None, freevars=None):
        if params is None:
            params = list()
        if freevars is None:
            freevars = list()
        self = super(Function, cls).__new__(
                cls, module, id, name, params, parent, freevars, list())
        self._type = type
        self.loop_conts = list()
        self.loop_exits = list()
        self.labels = dict()
        self.locals = list()
        return self

    def new_block(self):
        '''create a new block and added it to this function'''
        block = Block(len(self.blocks))
        self.blocks.append(block)
        return block

    def new_register(self, type):
        '''create a new register of the given type'''
        rid = len(self.locals)
        reg = Register(rid, self.ref(), type)
        self.locals.append(reg)
        return reg

    def ref(self):
        '''get the function ref for this function (an easy way to lookup the
        function later in the module(s).'''
        return FunctionRef(self.module, self.id, self.name, self.type())

    def type(self):
        '''the sile type of this function'''
        return self._type

    def push_loop(self, cont, exit):
        '''push the continue/exit blocks for a loop'''
        self.loop_conts.append(cont)
        self.loop_exits.append(exit)

    def pop_loop(self):
        '''pop the continue/exit blocks for a loop'''
        self.loop_conts.pop()
        self.loop_exits.pop()

    def loop_cont(self):
        '''get the nearest continue block'''
        return self.loop_conts[-1]

    def loop_exit(self):
        '''get the nearest exit block'''
        return self.loop_exits[-1]

    def add_label(self, name, cont, exit):
        '''label a loop'''
        self.labels[name] = LabeledLoop(cont, exit)

    def closure(self, module, symbols, closing=None):
        '''compute a closure of this function, by finding the symbols to capture'''
        if closing is None:
            closing = set()
        r = self.ref()
        closing.add(self.ref())
        capture = dict()
        for var in self.freevars:
            operand = symbols[var]
            value = None
            if isinstance(operand, Register):
                value = operand
            elif isinstance(operand, FunctionRef):
                if operand in closing:
                    value = None
                value = module.lookup(operand).closure(module, symbols, closing)
            else:
                raise IlExecutionException("unexpected operand {}".format(operand))
            if value is not None:
                capture[var] = value
        return Closure(self.ref(), capture)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        lines = list()
        parent = ''
        if self.parent is not None:
            parent = ' in {}'.format(self.parent)
        params = ', '.join(str(p) for p in self.params)
        lines.append("function {}({}) {{".format(self.ref(), params))
        lines.append("  freevars: {}".format(self.freevars))
        for block in self.blocks:
            lines.append(indent(str(block), 2))
        lines.append("}")
        return '\n'.join(lines)

    def dotty(self):
        header  = 'digraph "{}" {{\n'.format(repr(str(self.ref()))[1:-1])
        header += 'bgcolor="transparent";\n'
        header += 'label="{}";\n'.format(repr(str(self.ref()))[1:-1])
        header += 'labelloc=top;\n'
        header += '''node [shape="rect", labeljust=l, fontname="DejaVuSansMono",
                        style=filled, fillcolor=white];\n'''
        nodes = list()
        edges = list()
        for block in self.blocks:
            nodes.append('{} [label="{}"];'.format(block.id, block.__dotty__()))
            for link in block.next:
                label = ''
                if link.link_type != LINKS['UNCONDITIONAL']:
                    label = ' [label="{}"]'.format(LINK_NAMES[link.link_type])
                edges.append('{} -> {}{};'.format(link.src, link.target, label))
        footer = "}"
        return header + '\n'.join(nodes) + '\n' + '\n'.join(edges) + '\n' + footer


FunctionRefTuple = namedtuple("FunctionRef", ('module', 'id', 'name'))
class FunctionRef(FunctionRefTuple):
    '''represents an short name for the function to use for looking up in the
    module(s).'''

    def __new__(cls, module, id, name, type):
        self = super(FunctionRef, cls).__new__(cls, module, id, name)
        self._type = type
        return self

    def type(self):
        '''get the type of the function referred to by this ref'''
        return self._type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "fn:{}:{}:{}".format(self.module, self.id, self.name)

    def short(self):
        return "{}:{}".format(self.module, self.id)

ClosureTuple = namedtuple("Closure", ('fn', 'captured'))
class Closure(ClosureTuple):
    '''represents a compile time closure. It has a function ref, and the closed
    over symbols.'''

    def type(self):
        return self.fn.type()

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Closure of {} captured {}".format(self.fn, self.captured)


LINK_NAMES = [
    'UNCONDITIONAL',
    'TRUE',
    'FALSE',
]
LINKS = {name:idx for idx, name in enumerate(LINK_NAMES)}
LinkTuple = namedtuple('Link', ('src', 'target', 'link_type'))
class Link(LinkTuple):
    '''This represents a jump in the control flow graph. It has the
    source/target indices as well as what kind of jump it is.'''

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        link_type = ''
        if self.link_type == LINKS['TRUE']:
            link_type = ' on true'
        elif self.link_type == LINKS['FALSE']:
            link_type = ' on false'
        elif self.link_type == LINKS['UNCONDITIONAL']:
            link_type = ''
        else:
            raise Exception("unexpected link type")

        return '({}->{}{})'.format(self.src, self.target, link_type)

BlockTuple = namedtuple("Block", ('id', 'code', 'prev', 'next'))
class Block(BlockTuple):
    '''Represents a basic block of sequential instructions. May end in a
    conditional jump.'''

    def __new__(cls, id):
        self = super(Block, cls).__new__(cls, id, list(), list(), list())
        return self

    def append(self, instruction):
        '''Add an instruction'''
        self.code.append(instruction)
        return self

    def link_to(self, block, link_type):
        '''link this block to another with the given type. you probably want
        if_link/goto_link unless you are implementing function rewriting for
        closure construction.'''
        def isunconditional(link):
            return link.link_type == LINKS['UNCONDITIONAL']
        def matches(link):
            return link.link_type == link_type
        if any(isunconditional(link) for link in self.next):
            raise IlGenException("already has an unconditional link")
        if any(matches(link) for link in self.next):
            raise IlGenException("already has an {} link".format(link_type))
        link = Link(self.id, block.id, link_type)
        self.next.append(link)
        block.prev.append(link)
        return self

    def if_link(self, condition, then, otherwise):
        '''link this block to the then/otherwise blocks by adding an IFTRUE
        instruction on the given condition.'''
        self.append(Instruction(
                OPS['IFTRUE'], condition, None, IfJumpTargets(then.id, otherwise.id)))
        self.link_to(then, LINKS['TRUE'])
        self.link_to(otherwise, LINKS['FALSE'])

    def goto_link(self, block):
        '''unconditionally link this block to the given block witha JUMP
        instruction'''
        self.append(Instruction(
                OPS['JUMP'], None, None, JumpTarget(block.id)))
        self.link_to(block, LINKS['UNCONDITIONAL'])

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        lines = list()
        lines.append('blk {}'.format(self.id))
        lines.append('  next: {}'.format(' '.join(str(l) for l in self.next)))
        lines.append('  prev: {}'.format(' '.join(str(l) for l in self.prev)))
        lines.append('  instructions:')
        for inst in self.code:
            lines.append('    {}'.format(inst))
        return '\n'.join(lines)

    def __dotty__(self):
        lines = list()
        for inst in self.code:
            lines.append('{}'.format(inst))
        return 'blk-{}\n'.format(self.id) + '\\l'.join(lines) + '\\l'


RegisterTuple = namedtuple("Register", ('id', 'fn'))
class Register(RegisterTuple):
    '''this is a "function local symbolic register" that represents local
    variables. The id is just a number, the fn is the function ref for the
    function this register belongs in.'''

    def __new__(cls, id, fn, type):
        self = super(Register, cls).__new__(cls, id, fn)
        self._type = type
        return self

    def type(self):
        return self._type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'reg:{}:{}:{}'.format(self.fn.short(), self.id, self.type())

ClosureRegisterTuple = namedtuple("ClosureRegister", ('id',))
class ClosureRegister(ClosureRegisterTuple):
    '''like a regular register but used when the register in question is has
    been captured and put in a closure. Since you can only access the top level
    closure it doesn't need a function ref.'''

    def __new__(cls, id, type):
        self = super(ClosureRegister, cls).__new__(cls, id)
        self._type = type
        return self

    def type(self):
        return self._type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return 'closure:{}:{}'.format(self.id, self.type())

ConstantTuple = namedtuple("Constant", ('value',))
class Constant(ConstantTuple):
    '''a constant value.'''

    def __new__(cls, value, type):
        self = super(Constant, cls).__new__(cls, value)
        self._type = type
        return self

    def type(self):
        return self._type

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return '${}:{}'.format(self.value, self.type())


IfJumpTargets = namedtuple("IfJumpTargets", ("then", "otherwise"))
JumpTarget = namedtuple("JumpTarget", ("target",))


## THE OP CODES
OP_NAMES = [
    # moves
    'IMM', # IMM $constant result
    'MV',  # IMM reg:1     reg:result

    # arithmetic
    'ADD', # ADD a b reg:result
    'SUB',
    'MUL',
    'DIV',
    'MOD',

    # comparison operators
    'EQ', # EQ a b reg:result
    'NE',
    'LT',
    'GT',
    'LE',
    'GE',

    # boolean operators
    'NOT', # NOT a reg:result

    # function call related
    'CALL', # CALL fn/closure [params]+ reg:result
    'PRM',  # PRM  name idx reg:result  loads a function parameter into a local
    'RTRN', # RTRN a                    returns a value from the function

    # creates a closure of the given function by capturing the given registers
    # and bundling that with the given function. Note, you have to rewrite the
    # code of the function to use the ClosureRegisters where appropriate.
    'CLOSURE', # CLOSURE fn [registers to put in closure] reg:result

    # control flow
    'JUMP',   # JUMP result:target
    'IFTRUE', # IFTRUE a result:targets

    # instrinsic
    'PRINT', # PRINT a
]
OPS = {name:idx for idx, name in enumerate(OP_NAMES)}
InstructionTuple = namedtuple("Instruction", ("op", "a", "b", "result"))
class Instruction(InstructionTuple):

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        op = OP_NAMES[self.op]
        a = ''
        b = ''
        result = ''
        if self.a is not None:
            a = ' {}'.format(self.a)
        if self.b is not None:
            b = ' {}'.format(self.b)
        if self.result is not None:
            result = ' {}'.format(self.result)
        return '{}{}{}{}'.format(op, a, b, result)

