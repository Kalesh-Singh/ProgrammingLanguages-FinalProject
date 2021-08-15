#!/usr/bin/env

from symbol_table import SymbolTable
from il import IlGenException

## This file computes the free variables in a function.
## You likely will not need to make changes in this file.

def freevars(function_ast):

    freevars = set()

    def stmts(symbols, n):
        symbols = symbols.push()
        for kid in n.children:
            stmt(symbols, kid)
        symbols = symbols.pop()

    def stmt(symbols, n):
        dispatch(symbols, n, {
            "decl": decl,
            "assign": assign,
            "print": print_stmt,
            "return": return_stmt,
            "if": if_stmt,
            "while": while_stmt,
            "break": nop,
            "continue": nop,
            "expr-stmt": expr_stmt,
            "label": label_stmt,
            "function": function_decl,
            "stmts": stmts,
        })

    def decl(symbols, n):
        expr(symbols, n.children[1])
        symbols.put(n.children[0].value, True)

    def assign(symbols, n):
        expr(symbols, n.children[0])
        expr(symbols, n.children[1])

    def print_stmt(symbols, n):
        expr(symbols, n.children[0])

    def return_stmt(symbols, n):
        expr(symbols, n.children[0])

    def expr_stmt(symbols, n):
        expr(symbols, n.children[0])

    def if_stmt(symbols, n):
        expr(symbols, n.children[0])
        if len(n.children) == 2:
            stmts(symbols, n.children[1])
        elif len(n.children) == 3:
            stmts(symbols, n.children[1])
            stmts(symbols, n.children[2])
        else:
            raise IlGenException("malformed if statement: {}".format(n))

    def while_stmt(symbols, n):
        expr(symbols, n.children[0])
        stmts(symbols, n.children[1])

    def label_stmt(symbols, n):
        stmt(symbols, n.children[1])
        symbols.put(n.children[0].value, True)

    def function_decl(symbols, n):
        name = n.children[0].value
        params = [
            param.children[0].value
            for idx, param in enumerate(n.children[1].children)]
        body = n.children[3]
        symbols[name] = True
        symbols = symbols.push()
        for param in params:
            symbols[param] = True
        stmts(symbols, body)
        symbols = symbols.pop()

    def expr(symbols, n):
        dispatch(symbols, n, {
            "+": binop,
            "-": binop,
            "*": binop,
            "/": binop,
            "%": binop,
            "negate": unaryop,
            "not": unaryop,
            "&&": binop,
            "||": binop,
            "==": binop,
            "!=": binop,
            "<": binop,
            ">": binop,
            "<=": binop,
            ">=": binop,
            "call": call,
            "NAME": name_action,
            "FLOAT": nop,
            "INTEGER": nop,
        })

    def binop(symbols, n):
        expr(symbols, n.children[0])
        expr(symbols, n.children[1])

    def unaryop(symobls, n):
        expr(symbols, n.children[0])

    def call(symbols, n):
        expr(symbols, n.children[0])
        for param in n.children[1].children:
            expr(symbols, param)

    def nop(symbols, n):
        pass

    def name_action(symbols, n):
        if n.value not in symbols:
            freevars.add(n.value)

    def dispatch(symbols, n, labels_to_actions):
        for name, func in labels_to_actions.iteritems():
            if n.label == name:
                return func(symbols, n)
        raise IlGenException(
            "got '{}', want one of: {}".format(n.label, labels_to_actions.keys()))

    name = function_ast.children[0].value
    params = [
        param.children[0].value
        for idx, param in enumerate(function_ast.children[1].children)]
    body = function_ast.children[3]
    symbols = SymbolTable()
    symbols.put(name, True)
    for param in params:
        symbols.put(param, True)
    stmts(symbols, body)

    return freevars

