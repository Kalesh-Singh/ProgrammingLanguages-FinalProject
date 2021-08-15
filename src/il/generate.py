#!/usr/bin/env python

import sys

import il
from sile_types import types
from il import IlGenException
from freevars import freevars
from symbol_table import SymbolTable

## This file is the intermediate code generator. You likely will
## need to make changes in this file!

## Some portions of the code generator will be working but others
## will not be. You will need to fill it in.

def generate(ast):
    mods = il.Modules()
    generate_module(mods, 'main', ast)
    return mods

def generate_module(modules, name, ast):
    mod = il.Module(name)
    modules.add(mod)
    return IlGenerator.generate(modules, mod, ast)

class IlGenerator(object):

    @staticmethod
    def generate(modules, module, ast):
        self = IlGenerator(modules, module)
        self.stmts(self.function().new_block(), ast)
        return self.module

    def __init__(self, modules, module):
        self.modules = modules
        self.module = module
        self.functions = [self.module.new_function('main', types.Function([], types.UNIT))]
        self.symbols = SymbolTable()

    def function(self):
        return self.functions[-1]

    def push_function(self, name, type, params, freevars):
        fn = self.module.new_function(
            name, type, params=params, parent=self.function().id, freevars=freevars)
        self.functions.append(fn)
        return fn

    def pop_function(self):
        return self.functions.pop()

    def new_register(self, regtype):
        return self.function().new_register(regtype)

    def stmts(self, blk, n):
        self.symbols = self.symbols.push()
        for kid in n.children:
            blk = self.stmt(blk, kid)
        self.symbols = self.symbols.pop()
        return blk

    def stmt(self, blk, n):
        return self.dispatch_stmt(blk, n, {
            "decl": self.decl_action,
            "assign": self.assign_action,
            "expr-stmt": self.expr_stmt_action,
            "print": self.print_action,
            "if": self.if_action,
            "while": self.while_action,
            "label": self.label_action,
            "break": self.break_action,
            "continue": self.continue_action,
            "function": self.function_action,
            "return": self.return_action,
            "stmts": self.stmts,
        })

    def decl_action(self, blk, n):
        name = n.children[0].value
        dest = self.new_register(n.children[1].type)
        a, blk = self.expr(blk, dest, n.children[1])
        self.symbols[name] = a
        return blk

    def assign_action(self, blk, n):
        name = n.children[0].value
        dest = self.symbols[name]
        a, blk = self.expr(blk, dest, n.children[1])
        return blk

    def print_action(self, blk, n):
        a, blk = self.expr(blk, None, n.children[0])
        blk.append(il.Instruction(il.OPS['PRINT'], a, None, None))
        return blk

    def return_action(self, blk, n):
        a, blk = self.expr(blk, None, n.children[0])
        if isinstance(a, il.FunctionRef):
            closure = self.module.lookup(a).closure(self.module, self.symbols)
            if len(closure.captured) > 0:
                a, blk = self.create_closures(blk, closure)
        blk.append(il.Instruction(il.OPS['RTRN'], a, None, None))
        return blk

    def create_closures(self, blk, closure):
        ## Implements function closure creation
        registers = list()
        rewrite = dict()
        for name, operand in closure.captured.iteritems():
            if isinstance(operand, il.Closure):
                fn_ref = operand.fn
                operand, blk = self.create_closures(blk, operand)
                rewrite[fn_ref] = il.ClosureRegister(len(registers), fn_ref.type())
            registers.append(operand)
        result = self.new_register(closure.fn.type())
        rewrite[closure.fn] = il.ClosureRegister(len(registers), closure.fn.type())
        for idx, reg in enumerate(registers):
            rewrite[reg] = il.ClosureRegister(idx, reg.type())
        closure_code = self.rewrite(closure.fn, rewrite)
        blk.append(il.Instruction(
            il.OPS['CLOSURE'], closure_code.ref(), registers, result))
        return result, blk

    def rewrite(self, fn_ref, rewrites):
        ## Implements function rewriting for closure creation
        old = self.module.lookup(fn_ref)
        new = self.push_function(old.name + '-closure', old.type(), old.params, list())
        new.locals = old.locals
        def replace(operand):
            if isinstance(operand, il.FunctionRef) and operand in rewrites:
                return rewrites[operand]
            elif isinstance(operand, il.Register) and operand in rewrites:
                return rewrites[operand]
            elif isinstance(operand, il.Register) and operand.fn == old.ref():
                return il.Register(operand.id, new.ref(), operand.type())
            elif isinstance(operand, list):
                return [replace(inner) for inner in operand]
            return operand
        for old_blk in old.blocks:
            new_blk = new.new_block()
            for inst in old_blk.code:
                new_blk.append(il.Instruction(
                    inst.op, replace(inst.a), replace(inst.b),
                    replace(inst.result)))
        for idx, old_blk in enumerate(old.blocks):
            new_blk = new.blocks[idx]
            for link in old_blk.next:
                new_blk.link_to(new.blocks[link.target], link.link_type)
        self.pop_function()
        return new

    def if_action(self, entry, n):
        # DONE
        then = self.function().new_block()
        otherwise = self.function().new_block()
        if len(n.children) == 2:
            afterwards = otherwise
        elif len(n.children) == 3:
            afterwards = self.function().new_block()
        else:
            raise IlGenException("malformed if statement")
        cond, cond_out = self.expr(entry, None, n.children[0])
        cond_out.if_link(cond, then, otherwise)
        then_out = self.stmts(then, n.children[1])
        then_out.goto_link(afterwards)
        if len(n.children) == 3:
            otherwise_out = self.stmts(otherwise, n.children[2])
            otherwise_out.goto_link(afterwards)
        return afterwards
        
    def while_action(self, entry, n):
        header = self.function().new_block()
        body = self.function().new_block()
        afterwards = self.function().new_block()
        return self._while_action(entry, n, header, body, afterwards)

    def _while_action(self, entry, n, header, body, afterwards):
        self.function().push_loop(header, afterwards)
        entry.goto_link(header)
        cond, cond_out = self.expr(header, None, n.children[0])
        cond_out.if_link(cond, body, afterwards)
        body_out = self.stmts(body, n.children[1])
        body_out.goto_link(header)
        self.function().pop_loop()
        return afterwards

    def label_action(self, entry, n):
        # DONE
        name = n.children[0].value
        header = self.function().new_block()
        body = self.function().new_block()
        afterwards = self.function().new_block()
        self.function().add_label(name, header, afterwards)
        labeledLoop = il.LabeledLoop(header, afterwards)
        self.symbols[name] = labeledLoop
        return self._while_action(entry, n.children[1], header, body, afterwards)

    def break_action(self, blk, n):
        # DONEISH
        if len(n.children) == 0:
            exit = self.function().loop_exit()
        else:
            label = n.children[0].value
            exit = self.symbols[label].exit_blk
        blk.goto_link(exit)
        dead = self.function().new_block()
        return dead

    def continue_action(self, blk, n):
        if len(n.children) == 0:
            header = self.function().loop_cont()
        else:
            label = n.children[0].value
            header = self.symbols[label].continue_blk
        blk.goto_link(header)
        dead = self.function().new_block()
        return dead

    def expr_stmt_action(self, blk, n):
        _, blk = self.expr(blk, None, n.children[0])
        return blk

    def function_action(self, blk, n):
        type = n.children[0].type
        name = n.children[0].value
        params = [
            il.Param(id=idx, name=param.children[0].value, type=param.type)
            for idx, param in enumerate(n.children[1].children)]
        body = n.children[3]
        free = freevars(n)
        fn = self.push_function(name, type, params, free)
        # DONE
        self.symbols[name] = fn.ref()
        self.symbols = self.symbols.push()
        entry_blk = fn.new_block()
        for idx, param in enumerate(fn.params):
            r = self.new_register(param.type)
            self.symbols[param.name] = r
            entry_blk.append(il.Instruction(il.OPS['PRM'], param, 0, r))
        self.stmts(entry_blk, body)
        self.symbols = self.symbols.pop()
        self.pop_function()
        self.symbols[name] = fn.ref()
        return blk

    def expr(self, blk, result, n):
        return self.dispatch_expr(blk, result, n, {
            "negate": self.negate,
            "+": self.binop(il.OPS['ADD']),
            "-": self.binop(il.OPS['SUB']),
            "*": self.binop(il.OPS['MUL']),
            "/": self.binop(il.OPS['DIV']),
            "%": self.binop(il.OPS['MOD']),
            "==": self.binop(il.OPS['EQ']),
            "!=": self.binop(il.OPS['NE']),
            "<": self.binop(il.OPS['LT']),
            ">": self.binop(il.OPS['GT']),
            "<=": self.binop(il.OPS['LE']),
            ">=": self.binop(il.OPS['GE']),
            "not": self.not_op,
            "&&": self.and_op,
            "||": self.or_op,
            "call": self.call,
            "NAME": self.name,
            "INTEGER": self.number,
            "FLOAT": self.number,
        })

    def negate(self, blk, result, n):
        if result is None:
            result = self.new_register(n.type)
        a, blk = self.expr(blk, None, n.children[0])
        blk.append(il.Instruction(
            il.OPS['SUB'], il.Constant(0, n.type), a, result))
        return result, blk

    def binop(self, op):
        def binop(blk, result, n):
            if result is None:
                result = self.new_register(n.type)
            a, blk = self.expr(blk, None, n.children[0])
            b, blk = self.expr(blk, None, n.children[1])
            blk.append(il.Instruction(op, a, b, result))
            return result, blk
        return binop

    def not_op(self, blk, result, n):
        # DONE
        if result is None:
            result = self.new_register(n.type)
        a, blk = self.expr(blk, None, n.children[0])
        blk.append(il.Instruction(il.OPS['NOT'], a, None, result))
        return result, blk

    def and_op(self, a_in_blk, result, n):
        # DONE
        if result is None:
            result = self.new_register(n.type)
        a, a_out_blk = self.expr(a_in_blk, result, n.children[0])
        b_in_blk = self.function().new_block()
        exit_blk = self.function().new_block()
        a_out_blk.if_link(a, b_in_blk, exit_blk)
        #                    on-true   on-false
        b, b_out_blk = self.expr(b_in_blk, result, n.children[1])
        b_out_blk.goto_link(exit_blk)
        return result, exit_blk
    
    def or_op(self, a_in_blk, result, n):
        if result is None:
            result = self.new_register(n.type)
        a, a_out_blk = self.expr(a_in_blk, result, n.children[0])
        b_in_blk = self.function().new_block()
        exit_blk = self.function().new_block()
        a_out_blk.if_link(a, exit_blk, b_in_blk)
        #                    on-true   on-false
        b, b_out_blk = self.expr(b_in_blk, result, n.children[1])
        b_out_blk.goto_link(exit_blk)
        return result, exit_blk

    def call(self, blk, result, n):
        # DONE
        if result is None:
            result = self.new_register(n.type)
        name = n.children[0].value
        fn = self.symbols.get(name)
        param_operands = list()
        for param in n.children[1].children:
            reg, _ = self.expr(blk, None, param)
            param_operands.append(reg)
        
        blk.append(il.Instruction(il.OPS['CALL'], fn, param_operands, result))
        return result, blk

    def name(self, blk, result, n):
        if result is None:
            return self.symbols[n.value], blk
        blk.append(il.Instruction(
            il.OPS['MV'], self.symbols[n.value], None, result))
        return result, blk

    def number(self, blk, result, n):
        const = il.Constant(n.value, n.type)
        if result is None:
            return const, blk
        blk.append(il.Instruction(il.OPS['IMM'], const, None, result))
        return result, blk

    def dispatch_stmt(self, blk, n, labels_to_actions):
        for name, func in labels_to_actions.iteritems():
            if n.label == name:
                return func(blk, n)
        raise IlGenException(
            "got '{}', want one of: {}".format(n.label, labels_to_actions.keys()))

    def dispatch_expr(self, blk, result, n, labels_to_actions):
        for name, func in labels_to_actions.iteritems():
            if n.label == name:
                return func(blk, result, n)
        raise IlGenException(
            "got '{}', want one of: {}".format(n.label, labels_to_actions.keys()))

