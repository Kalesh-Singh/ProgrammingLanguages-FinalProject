#!/usr/bin/env python2

from collections import namedtuple

import il
from sile_types import types

class IlExecutionException(Exception): pass

## This is the IL interpretter. IT RUNS THE PROGRAM
## You will need to edit this file.

RuntimeClosure = namedtuple("RuntimeClosure", ("fn", "captured"))

Address = namedtuple("Address", ("fn", "block", "inst"))

class Frame(object):

    def __init__(self, return_addr, fn, result_reg, params, captured):
        self.return_addr = return_addr
        self.fn = fn
        self.params = params
        self.result_reg = result_reg
        self.locals = [None for _ in fn.locals]
        self.closure = captured

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        local = list()
        for val in self.locals:
            if isinstance(val, RuntimeClosure):
                val = "(closure of {})".format(val.fn)
            local.append(val)
        closure = list()
        for val in self.closure:
            if isinstance(val, RuntimeClosure):
                val = "(closure of {})".format(val.fn)
            closure.append(val)
        return (
            'Frame {}({}):\n  result_reg = {}\n  locals = {}\n  closure = {}\n'.format(
                self.fn.ref(), self.params, self.result_reg, local, closure))

def run(mods):
    IlMachine.run(mods)

class IlMachine(object):

    @staticmethod
    def run(mods):
        main = il.FunctionRef('main', 0, 'main', types.Function([], types.UNIT))
        main = mods.lookup(main)
        self = IlMachine(mods)
        self.push_frame(None, main, None, list(), dict())
        self.execute(Address(main, 0, 0))
        self.pop_frame()

    def __init__(self, mods):
        self.modules = mods
        self.register = dict()
        self.frames = list()

    def push_frame(self, return_addr, fn, result_reg, params, captured):
        frame = Frame(return_addr, fn, result_reg, params, captured)
        self.frames.append(frame)
        return frame

    def pop_frame(self):
        return self.frames.pop()

    def frame(self):
        return self.frames[-1]

    def find_frame(self, reg):
        idx = len(self.frames)-1
        while idx >= 0 and reg.fn != self.frames[idx].fn.ref():
            idx -= 1
        if idx < 0:
            raise IlExecutionException("unknown register {}: {}".format(reg, self.frames))
        return self.frames[idx]

    def store(self, reg, value):
        if isinstance(reg, il.Register):
            frame = self.find_frame(reg)
            frame.locals[reg.id] = value
        elif isinstance(reg, il.ClosureRegister):
            self.frame().closure[reg.id] = value
        else:
            raise IlExecutionException("unknown register type {}".format(reg))

    def load(self, reg):
        frame = self.find_frame(reg)
        return frame.locals[reg.id]

    def load_from_closure(self, reg):
        return self.frame().closure[reg.id]

    def execute(self, start_addr):
        if len(self.frames) > 100:
            raise Exception("fail -- stack overflow")
        addr = start_addr
        while addr is not None:
            try:
                addr = self.once(addr)
            except:
                print 'error'
                print 'in', addr.fn.ref(), addr.block, addr.inst
                print addr.fn
                print 'call stack'
                for frame in self.frames:
                    print frame
                raise

    def once(self, addr):
        if addr.fn is None:
            return
        if addr.block is None:
            return
        if addr.inst is None:
            return
        blk = addr.fn.blocks[addr.block]
        if addr.inst >= len(blk.code):
            return
        instruction = blk.code[addr.inst]
        cont = self.inst(addr, instruction)
        if cont is None and len(self.frames) > 1:
            frame = self.pop_frame()
            self.store(frame.result_reg, None)
            return frame.return_addr
        return cont

    def block(self, fn, blk):
        for inst in blk.code:
            new_blk, ret = self.inst(fn, inst)
            if ret:
                break
            if new_blk is not None:
                return new_blk
        return None

    def inst(self, addr, inst):
        if addr.inst + 1 < len(addr.fn.blocks[addr.block].code):
            next = Address(addr.fn, addr.block, addr.inst+1)
        else:
            next = None
        # arithmetic
        if inst.op == il.OPS['IMM']:
            self.store(inst.result, self.value(inst.a))
        elif inst.op == il.OPS['MV']:
            self.store(inst.result, self.value(inst.a))
        elif inst.op == il.OPS['ADD']:
            # DONE
            self.store(inst.result, self.value(inst.a) + self.value(inst.b))
        elif inst.op == il.OPS['SUB']:
            # DONE
            self.store(inst.result, self.value(inst.a) - self.value(inst.b))
        elif inst.op == il.OPS['MUL']:
            # DONE
            self.store(inst.result, self.value(inst.a) * self.value(inst.b))
        elif inst.op == il.OPS['MOD']:
            # DONE
            self.store(inst.result, self.value(inst.a) % self.value(inst.b))
        elif inst.op == il.OPS['DIV']:
            # DONE
            self.store(inst.result, self.value(inst.a) / self.value(inst.b))

        # comparison operators
        elif inst.op == il.OPS['EQ']:
            # DONE
            self.store(inst.result, self.value(inst.a) == self.value(inst.b))
        elif inst.op == il.OPS['NE']:
            # DONE
            self.store(inst.result, self.value(inst.a) != self.value(inst.b))
        elif inst.op == il.OPS['LT']:
            # DONE
            self.store(inst.result, self.value(inst.a) < self.value(inst.b))
        elif inst.op == il.OPS['GT']:
            # DONE
            self.store(inst.result, self.value(inst.a) > self.value(inst.b))
        elif inst.op == il.OPS['LE']:
            # DONE
            self.store(inst.result, self.value(inst.a) <= self.value(inst.b))
        elif inst.op == il.OPS['GE']:
            # DONE
            self.store(inst.result, self.value(inst.a) >= self.value(inst.b))
        elif inst.op == il.OPS['NOT']:
            # DONE
            self.store(inst.result, not self.value(inst.a))

        # function call related
        elif inst.op == il.OPS['CALL']:
            # DONE
            callee = self.value(inst.a)
            captured = list()
            if isinstance(callee, il.Function):
                pass
            elif isinstance(callee, RuntimeClosure):
                captured = callee.captured
                callee = self.modules.lookup(callee.fn)
            else:
                raise IlExecutionException("can't call a {}".format(callee))
            params = [self.value(param) for param in inst.b]
            frame = self.push_frame(next, callee, inst.result, params, captured)
            self.execute(Address(callee, 0, 0))
            return self.frame().return_addr

        elif inst.op == il.OPS['PRM']:
            self.store(inst.result, self.value(inst.a))
        elif inst.op == il.OPS['RTRN']:
            frame = self.frame()
            value = self.value(inst.a)
            self.pop_frame()
            self.store(frame.result_reg, value)
            return frame.return_addr
        elif inst.op == il.OPS['CLOSURE']:
            capture = [self.value(reg) for reg in inst.b]
            closure = RuntimeClosure(inst.a, capture)
            closure.captured.append(closure)
            self.store(inst.result, closure)

        # control flow
        elif inst.op == il.OPS['JUMP']:
            return Address(addr.fn, inst.result.target, 0)
        elif inst.op == il.OPS['IFTRUE']:
            # DONE
            if self.value(inst.a):
                return Address(addr.fn, inst.result.then, 0)
            else:
                return Address(addr.fn, inst.result.otherwise, 0)

        # instrinsic
        elif inst.op == il.OPS['PRINT']:
            # DONE
            print str(self.value(inst.a)).lower()

        else:
            raise IlExecutionException("unknown instruction {}".format(inst))

        return next

    def value(self, operand):
        if isinstance(operand, il.Constant):
            return operand.value
        elif isinstance(operand, il.Register):
            return self.load(operand)
        elif isinstance(operand, il.ClosureRegister):
            return self.load_from_closure(operand)
        elif isinstance(operand, il.Param):
            return self.frame().params[operand.id]
        elif isinstance(operand, il.FunctionRef):
            return self.modules.lookup(operand)
        elif isinstance(operand, il.JumpTarget):
            raise IlExecutionException("jump target has no value {}".format(operand))
        elif isinstance(operand, il.IfJumpTargets):
            raise IlExecutionException("jump target has no value {}".format(operand))
        else:
            raise IlExecutionException("unknown operand {}".format(operand))

