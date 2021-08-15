#!/usr/bin/env python2

from sile_types import types
from frontend.ast import Node
from il.symbol_table import SymbolTable

# This file implements the type checker!
# You probably won't need to edit it.


class TypeError(Exception): pass

def check(ast):
    return TypeChecker.check(ast)

def as_typed(n, t):
    return Node(n.label, value=n.value, type=t)

class TypeChecker(object):

    @classmethod
    def check(cls, ast):
        checker = TypeChecker()
        return checker.stmts(ast)

    def __init__(self):
        self.symbols = SymbolTable()
        self.functions = list()

    def function(self):
        return self.functions[-1]

    def push_function(self, fn):
        self.functions.append(fn)
        return fn

    def pop_function(self):
        return self.functions.pop()

    def assert_kid_count(self, want, n):
        if len(n.children) != want:
            raise TypeError(
                "malformed {} want {} children got: {}".format(
                    n.label, want, n))

    def assert_name(self, name, n):
        if n.label != name:
            raise TypeError(
                "expected {} got: {}".format(want, n))

    def stmts(self, n):
        self.assert_name("stmts", n)
        self.symbols = self.symbols.push()
        typed = as_typed(n, types.UNIT)
        for kid in n.children:
            typed.addkid(self.stmt(kid))
        self.symbols = self.symbols.pop()
        return typed

    def stmt(self, n):
        return self.dispatch(n, {
            "decl": self.decl_stmt,
            "assign": self.assign_stmt,
            "expr-stmt": self.expr_stmt,
            "print": self.print_stmt,
            "if": self.if_stmt,
            "while": self.while_stmt,
            "label": self.label_stmt,
            "continue": self.break_continue_stmt,
            "break": self.break_continue_stmt,
            "return": self.return_stmt,
            "function": self.fn_stmt,
            "stmts": self.stmts,
        })

    def decl_stmt(self, n):
        self.assert_kid_count(2, n)
        name = n.children[0].value
        expr = self.expr(n.children[1])
        name_node = as_typed(n.children[0], expr.type)
        self.symbols[name] = expr.type
        return as_typed(n, types.UNIT).addkid(name_node).addkid(expr)

    def assign_stmt(self, n):
        self.assert_kid_count(2, n)
        name = self.expr(n.children[0])
        expr = self.expr(n.children[1])
        if name.type != expr.type:
            raise TypeError("got {} want {}".format(expr, name.type))
        return as_typed(n, types.UNIT).addkid(name).addkid(expr)

    def expr_stmt(self, n):
        self.assert_kid_count(1, n)
        expr = self.expr(n.children[0])
        return as_typed(n, types.UNIT).addkid(expr)

    def print_stmt(self, n):
        self.assert_kid_count(1, n)
        expr = self.expr(n.children[0])
        return as_typed(n, types.UNIT).addkid(expr)

    def if_stmt(self, n):
        if len(n.children) < 2:
            raise TypeError("malformed if-statement: {}".format(n))
        cond = self.expr(n.children[0])
        then = self.stmts(n.children[1])
        if cond.type != types.BOOLEAN:
            raise TypeError("expected boolean got: {}".format(cond))
        if len(n.children) == 2:
            return as_typed(n, types.UNIT).addkid(cond).addkid(then)
        elif len(n.children) == 3:
            otherwise = self.stmts(n.children[2])
            return (as_typed(n, types.UNIT)
                        .addkid(cond)
                        .addkid(then)
                        .addkid(otherwise))
        else:
            raise TypeError("malformed if-statement: {}".format(n))

    def while_stmt(self, n):
        self.assert_kid_count(2, n)
        cond = self.expr(n.children[0])
        body = self.stmts(n.children[1])
        return as_typed(n, types.UNIT).addkid(cond).addkid(body)

    def label_stmt(self, n):
        label = n.children[0].value
        self.symbols[label] = types.LABEL
        stmt = self.stmt(n.children[1])
        if stmt.label != "while":
            raise TypeError("you may only label while loops got: {}".format(n))
        label_node = as_typed(n.children[0], types.LABEL)
        return as_typed(n, types.UNIT).addkid(label_node).addkid(stmt)

    def break_continue_stmt(self, n):
        if len(n.children) == 0:
            return as_typed(n, types.UNIT)
        self.assert_kid_count(1, n)
        label = self.expr(n.children[0])
        if label.type != types.LABEL:
            raise TypeError("attempt to break to a non-label: {}".format(n))
        return as_typed(n, types.UNIT).addkid(label)

    def return_stmt(self, n):
        self.assert_kid_count(1, n)
        expr = self.expr(n.children[0])
        if len(self.functions) <= 0:
            raise TypeError("return outside of function: {}".format(n))
        if expr.type != self.function().returns:
            raise TypeError(
                "expected return type {} got: {}".format(self.function().returns, expr))
        return as_typed(n, types.UNIT).addkid(expr)

    def fn_stmt(self, n):
        self.assert_kid_count(4, n)
        name = n.children[0].value
        params = as_typed(n.children[1], types.UNIT)
        returns = self.type_expr(n.children[2])
        param_types = list()
        for p in n.children[1].children:
            param = self.param_decl(p)
            self.symbols[param.children[0].value] = param.type
            params.addkid(param)
            param_types.append(param.type)
        fn_type = types.Function(param_types, returns.type)
        name_node = as_typed(n.children[0], fn_type)
        self.push_function(fn_type)
        self.symbols[name] = fn_type
        self.symbols = self.symbols.push()
        body = self.stmts(n.children[3])
        self.symbols = self.symbols.pop()
        self.pop_function()
        typed = (as_typed(n, types.UNIT)
                    .addkid(name_node)
                    .addkid(params)
                    .addkid(returns)
                    .addkid(body))
        return typed

    def exprs(self, n):
        self.assert_name("exprs", n)
        typed = as_typed(n, types.UNIT)
        for kid in n.children:
            typed.addkid(self.expr(kid))
        return typed

    def expr(self, n):
        return self.dispatch(n, {
            "negate": self.op(None)([types.INT, types.FLOAT]),
            "+": self.op(None)([types.INT, types.FLOAT]),
            "-": self.op(None)([types.INT, types.FLOAT]),
            "*": self.op(None)([types.INT, types.FLOAT]),
            "/": self.op(None)([types.INT, types.FLOAT]),
            "%": self.op(None)([types.INT, types.FLOAT]),
            "==": self.op(types.BOOLEAN)([types.INT, types.FLOAT]),
            "!=": self.op(types.BOOLEAN)([types.INT, types.FLOAT]),
            "<": self.op(types.BOOLEAN)([types.INT, types.FLOAT]),
            ">": self.op(types.BOOLEAN)([types.INT, types.FLOAT]),
            "<=": self.op(types.BOOLEAN)([types.INT, types.FLOAT]),
            ">=": self.op(types.BOOLEAN)([types.INT, types.FLOAT]),
            "not": self.op(types.BOOLEAN)([types.BOOLEAN]),
            "&&": self.op(types.BOOLEAN)([types.BOOLEAN]),
            "||": self.op(types.BOOLEAN)([types.BOOLEAN]),
            "call": self.call,
            "NAME": self.name,
            "INTEGER": self.basic(types.INT),
            "FLOAT": self.basic(types.FLOAT),
        })
        pass

    def op(self, return_type):
        def op(param_types):
            def op(n):
                in_type = None
                first = self.expr(n.children[0])
                for pt in param_types:
                    if pt == first.type:
                        in_type = pt
                        break
                if in_type is None:
                    raise TypeError(
                        "{} expected type in {} got: {}".format(
                            n.label, param_types, first))
                kids = list()
                for kid in n.children:
                    kid = self.expr(kid)
                    if in_type != kid.type:
                        raise TypeError(
                            "{} expected type {} got: {}".format(
                                n.label, in_type, kid.type))
                    kids.append(kid)
                if return_type is None:
                    typed = as_typed(n, in_type)
                else:
                    typed = as_typed(n, return_type)
                typed.children = kids
                return typed
            return op
        return op

    def call(self, n):
        self.assert_kid_count(2, n)
        fn = self.expr(n.children[0])
        params = self.exprs(n.children[1])
        if not isinstance(fn.type, types.Function):
            raise TypeError("called a non-function: {}".format(fn))
        if len(params.children) != len(fn.type.params):
            raise TypeError(
                "call {} and decl {} did not agree".format(n, fn.type))
        for idx in xrange(len(params.children)):
            if params.children[idx].type != fn.type.params[idx]:
                raise TypeError("param {} want type {} got {}".format(
                        idx,
                        fn.type.params[idx],
                        params.children[idx].type))
        return as_typed(n, fn.type.returns).addkid(fn).addkid(params)


    def name(self, n):
        if n.value not in self.symbols:
            raise TypeError("undefined name: {}".format(n))
        return as_typed(n, self.symbols[n.value])

    def basic(self, basic_type):
        def action(n):
            return as_typed(n, basic_type)
        return action

    def param_decl(self, n):
        self.assert_kid_count(2, n)
        type_expr = self.type_expr(n.children[1])
        name = as_typed(n.children[0], type_expr.type)
        return as_typed(n, type_expr.type).addkid(name).addkid(type_expr)

    def type_expr(self, n):
        return self.dispatch(n, {
            "function-type": self.fn_type_expr,
            "TYPE": self.basic_type_expr,
        })

    def basic_type_expr(self, n):
        self.assert_kid_count(0, n)
        name = n.value
        if name not in types.Basics:
            raise TypeError(
                "invalid primitive type {} allowed: {}".format(n, types.Basics.keys()))
        return as_typed(n, types.Basics[name])

    def fn_type_expr(self, n):
        self.assert_kid_count(2, n)
        params = self.types(n.children[0])
        returns = self.type_expr(n.children[1])
        param_types = [param.type for param in params.children]
        fn_type = types.Function(param_types, returns.type)
        return as_typed(n, fn_type).addkid(params).addkid(returns)

    def types(self, n):
        self.assert_name("types", n)
        typed = as_typed(n, types.UNIT)
        for kid in n.children:
            typed.addkid(self.type_expr(kid))
        return typed

    def dispatch(self, n, actions):
        if n.label not in actions:
            raise TypeError("got {} expected one of {}".format(
                n.label, actions.keys()))
        return actions[n.label](n)

