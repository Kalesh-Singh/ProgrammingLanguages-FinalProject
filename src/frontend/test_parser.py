#!/usr/bin/env python2

import pytest

from frontend import lexer
from frontend import parser
from frontend.ast import Node
from frontend.lexer import TOKENS, TOKEN_IDS

def test_dispatch_EOS():
    with pytest.raises(parser.SileParseError):
        tokens = []
        _, out_idx = parser._Parser(tokens).dispatch(0, {
            TOKEN_IDS["INTEGER"]: None,
            TOKEN_IDS["NAME"]: None,
        })
        assert out_idx == 0

def test_dispatch_wrong():
    with pytest.raises(parser.SileParseError):
        tokens = lexer.tokenize("+")
        _, out_idx = parser._Parser(tokens).dispatch(0, {
            TOKEN_IDS["INTEGER"]: None,
            TOKEN_IDS["NAME"]: None,
        })
        assert out_idx == 0

def test_consume_EOS():
    with pytest.raises(parser.SileParseError):
        tokens = []
        got, out_idx = parser._Parser(tokens).consume(0, TOKEN_IDS["NAME"])
        assert out_idx == 0

def test_consume_wrong():
    with pytest.raises(parser.SileParseError):
        tokens = lexer.tokenize("3")
        got, out_idx = parser._Parser(tokens).consume(0, TOKEN_IDS["NAME"])
        assert out_idx == 0

def test_consume():
    tokens = lexer.tokenize("wizard")
    want = lexer.Token(lexer.TOKEN_IDS['NAME'], 'NAME', 'wizard', 'wizard')
    got, out_idx = parser._Parser(tokens).consume(
        0,
        TOKEN_IDS["NAME"])
    assert out_idx == 1
    assert want == got

def test_consume_choice():
    tokens = lexer.tokenize("wizard")
    want = lexer.Token(lexer.TOKEN_IDS['NAME'], 'NAME', 'wizard', 'wizard')
    got, out_idx = parser._Parser(tokens).consume(
        0,
        TOKEN_IDS["INTEGER"],
        TOKEN_IDS["NAME"])
    assert out_idx == 1
    assert want == got

def test_dispatch():
    def false(idx):
        assert False
    def true(idx):
        assert True
    tokens = lexer.tokenize("wizard")
    parser._Parser(tokens).dispatch(0, {
        TOKEN_IDS["INTEGER"]: false,
        TOKEN_IDS["NAME"]: true,
    })

def test_factor_name():
    tokens = lexer.tokenize("wizard")
    want = Node("NAME", "wizard")
    got, out_idx = parser._Parser(tokens).factor_name(0)
    assert out_idx == 1
    assert want == got

def test_call_no_args():
    tokens = lexer.tokenize("()")
    want = Node("call").addkid(Node("exprs"))
    got, out_idx = parser._Parser(tokens).call(0)
    assert out_idx == 2
    assert want == got

def test_call():
    tokens = lexer.tokenize("(a,b,c,)")
    want = Node("call").addkid(
        Node("exprs")
            .addkid(Node("NAME", "a"))
            .addkid(Node("NAME", "b"))
            .addkid(Node("NAME", "c")))
    got, out_idx = parser._Parser(tokens).call(0)
    assert out_idx == 8
    assert want == got

def test_expr_list():
    tokens = lexer.tokenize("a,b")
    want = (
        Node("exprs")
            .addkid(Node("NAME", "a"))
            .addkid(Node("NAME", "b")))
    got, out_idx = parser._Parser(tokens).expr_list(0)
    assert out_idx == 3
    assert want == got

def test_expr_list_trailing_comma():
    tokens = lexer.tokenize("a,b,")
    want = (
        Node("exprs")
            .addkid(Node("NAME", "a"))
            .addkid(Node("NAME", "b")))
    got, out_idx = parser._Parser(tokens).expr_list(0)
    assert out_idx == 4
    assert want == got

def test_factor_int():
    tokens = lexer.tokenize("3")
    want = Node("INTEGER", 3)
    got, out_idx = parser._Parser(tokens).factor_int(0)
    assert out_idx == 1
    assert want == got

def test_factor_float():
    tokens = lexer.tokenize("3.1")
    want = Node("FLOAT", 3.1)
    got, out_idx = parser._Parser(tokens).factor_float(0)
    assert out_idx == 1
    assert want == got

def test_factor_paren():
    tokens = lexer.tokenize("(2.0e0)")
    want = Node("FLOAT", 2.0)
    got, out_idx = parser._Parser(tokens).factor_paren(0)
    assert out_idx == 3
    assert want == got

def test_factor():
    tokens = lexer.tokenize("(400)")
    want = Node("INTEGER", 400)
    got, out_idx = parser._Parser(tokens).factor(0)
    assert out_idx == 3
    assert want == got

def test_unary():
    tokens = lexer.tokenize("x")
    want = Node("NAME", "x")
    got, out_idx = parser._Parser(tokens).unary(0)
    assert out_idx == 1
    assert want == got

def test_unary_negate():
    tokens = lexer.tokenize("- x")
    want = Node("negate").addkid(Node("NAME", "x"))
    got, out_idx = parser._Parser(tokens).unary(0)
    assert out_idx == 2
    assert want == got

def test_term_prime_epsilon():
    tokens = lexer.tokenize("x")
    want = Node("term'")
    got, out_idx = parser._Parser(tokens).term_prime(0)
    assert out_idx == 0
    assert want == got

def test_term_prime_mul():
    tokens = lexer.tokenize("* x")
    want = Node("term'").addkid(Node("*")).addkid(Node("NAME", "x"))
    got, out_idx = parser._Parser(tokens).term_prime(0)
    assert out_idx == 2
    assert want == got

def test_term_prime_div():
    tokens = lexer.tokenize("/ x")
    want = Node("term'").addkid(Node("/")).addkid(Node("NAME", "x"))
    got, out_idx = parser._Parser(tokens).term_prime(0)
    assert out_idx == 2
    assert want == got

def test_term_prime_mod():
    tokens = lexer.tokenize("% x")
    want = Node("term'").addkid(Node("%")).addkid(Node("NAME", "x"))
    got, out_idx = parser._Parser(tokens).term_prime(0)
    assert out_idx == 2
    assert want == got

def test_term_prime_div_mul():
    tokens = lexer.tokenize("/ x * y")
    want = Node("term'").addkid(Node("/")).addkid(
            Node("*")
                .addkid(Node("NAME", "x"))
                .addkid(Node("NAME", "y")))
    got, out_idx = parser._Parser(tokens).term_prime(0)
    assert out_idx == 4
    assert want == got

def test_term():
    tokens = lexer.tokenize("x * y")
    want = Node("*").addkid(Node("NAME", "x")).addkid(Node("NAME", "y"))
    got, out_idx = parser._Parser(tokens).term(0)
    assert out_idx == 3
    assert want == got


def test_arith_expr_prime_epsilon():
    tokens = lexer.tokenize("x")
    want = Node("expr'")
    got, out_idx = parser._Parser(tokens).arith_expr_prime(0)
    assert out_idx == 0
    assert want == got

def test_arith_expr_prime_add():
    tokens = lexer.tokenize("+ x")
    want = Node("expr'").addkid(Node("+")).addkid(Node("NAME", "x"))
    got, out_idx = parser._Parser(tokens).arith_expr_prime(0)
    assert out_idx == 2
    assert want == got

def test_arith_expr_prime_sub():
    tokens = lexer.tokenize("- x")
    want = Node("expr'").addkid(Node("-")).addkid(Node("NAME", "x"))
    got, out_idx = parser._Parser(tokens).arith_expr_prime(0)
    assert out_idx == 2
    assert want == got

def test_arith_expr_prime_sub_add():
    tokens = lexer.tokenize("- x + y")
    want = Node("expr'").addkid(Node("-")).addkid(
            Node("+")
                .addkid(Node("NAME", "x"))
                .addkid(Node("NAME", "y")))
    got, out_idx = parser._Parser(tokens).arith_expr_prime(0)
    assert out_idx == 4
    assert want == got


def test_arith_expr():
    tokens = lexer.tokenize("x + y")
    want = Node("+").addkid(Node("NAME", "x")).addkid(Node("NAME", "y"))
    got, out_idx = parser._Parser(tokens).arith_expr(0)
    assert out_idx == 3
    assert want == got

def test_comparison_no_compare():
    tokens = lexer.tokenize("x + y")
    want = Node("+").addkid(Node("NAME", "x")).addkid(Node("NAME", "y"))
    got, out_idx = parser._Parser(tokens).comparison(0)
    assert out_idx == 3
    assert want == got

def test_comparison_ops():
    ops = ['==', '!=', '<', '>', '<=', '>=']
    for op in ops:
        tokens = lexer.tokenize(' '.join(['x', op, 'y']))
        want = Node(op).addkid(Node("NAME", "x")).addkid(Node("NAME", "y"))
        got, out_idx = parser._Parser(tokens).comparison(0)
        assert out_idx == 3
        assert want == got

def test_not_expr_nonot():
    tokens = lexer.tokenize("x + y")
    want = Node("+").addkid(Node("NAME", "x")).addkid(Node("NAME", "y"))
    got, out_idx = parser._Parser(tokens).not_expr(0)
    assert out_idx == 3
    assert want == got

def test_not_expr_not():
    tokens = lexer.tokenize("!x + y")
    want = Node("not").addkid(
        Node("+").addkid(Node("NAME", "x")).addkid(Node("NAME", "y")))
    got, out_idx = parser._Parser(tokens).not_expr(0)
    assert out_idx == 4
    assert want == got

def test_and_expr_prime():
    tokens = lexer.tokenize("&& x")
    want = Node("and_expr'").addkid(Node("&&")).addkid(Node("NAME", "x"))
    got, out_idx = parser._Parser(tokens).and_expr_prime(0)
    assert out_idx == 2
    assert want == got

def test_and_expr_prime_chained():
    tokens = lexer.tokenize("&& x && y")
    want = Node("and_expr'").addkid(Node("&&")).addkid(
            Node("&&").addkid(Node("NAME", "x"))
                      .addkid(Node("NAME", "y")))
    got, out_idx = parser._Parser(tokens).and_expr_prime(0)
    assert out_idx == 4
    assert want == got

def test_and_expr_chained():
    tokens = lexer.tokenize("z && x && y")
    want = (
        Node("&&")
            .addkid(Node("&&")
                .addkid(Node("NAME", "z"))
                .addkid(Node("NAME", "x")))
            .addkid(Node("NAME", "y")))
    got, out_idx = parser._Parser(tokens).and_expr(0)
    assert out_idx == 5
    assert want == got

def test_or_expr():
    tokens = lexer.tokenize("|| x")
    want = Node("or_expr'").addkid(Node("||").addkid(Node("NAME", "x")))
    got, out_idx = parser._Parser(tokens).or_expr(0)
    assert out_idx == 2
    assert want == got

def test_or_expr_chained():
    tokens = lexer.tokenize("|| x && y || z")
    want = (
        Node("or_expr'")
            .addkid(Node("||")
                .addkid(Node("&&")
                    .addkid(Node("NAME", "x"))
                    .addkid(Node("NAME", "y"))))
            .addkid(Node("||")
                .addkid(Node("NAME", "z"))))
    got, out_idx = parser._Parser(tokens).or_expr(0)
    assert out_idx == 6
    assert want == got

def test_expr():
    tokens = lexer.tokenize("z + y || x")
    want = (
        Node("||")
            .addkid(Node("+")
                .addkid(Node("NAME", "z"))
                .addkid(Node("NAME", "y")))
            .addkid(Node("NAME", "x")))
    got, out_idx = parser._Parser(tokens).expr(0)
    assert out_idx == 5
    assert want == got

def test_block_stmt():
    tokens = lexer.tokenize("{ print x }")
    want = Node("stmts").addkid(Node("print").addkid(Node("NAME", "x")))
    got, out_idx = parser._Parser(tokens).block_stmt(0)
    assert out_idx == 4
    assert want == got

def test_function_stmt():
    tokens = lexer.tokenize("function foo(p:ptype):ftype { print x }")
    want = (
        Node("function")
            .addkid(Node("NAME", "foo"))
            .addkid(Node("params")
                .addkid(Node("param")
                    .addkid(Node("NAME", "p"))
                    .addkid(Node("TYPE", "ptype"))))
            .addkid(Node("TYPE", "ftype"))
            .addkid(Node("stmts")
                .addkid(Node("print")
                    .addkid(Node("NAME", "x")))))
    got, out_idx = parser._Parser(tokens).function_stmt(0)
    assert out_idx == 13
    assert want == got

def test_param():
    tokens = lexer.tokenize("name : type")
    want = (
        Node("param")
            .addkid(Node("NAME", "name"))
            .addkid(Node("TYPE", "type")))
    got, out_idx = parser._Parser(tokens).param(0)
    assert out_idx == 3
    assert want == got

def test_params():
    tokens = lexer.tokenize("a : b, c : d")
    want = (
        Node("params")
            .addkid(
                Node("param")
                    .addkid(Node("NAME", "a"))
                    .addkid(Node("TYPE", "b")))
            .addkid(
                Node("param")
                    .addkid(Node("NAME", "c"))
                    .addkid(Node("TYPE", "d"))))
    got, out_idx = parser._Parser(tokens).params(0)
    assert out_idx == 7
    assert want == got

def test_params_trailing_comma():
    tokens = lexer.tokenize("a : b, c : d,")
    want = (
        Node("params")
            .addkid(
                Node("param")
                    .addkid(Node("NAME", "a"))
                    .addkid(Node("TYPE", "b")))
            .addkid(
                Node("param")
                    .addkid(Node("NAME", "c"))
                    .addkid(Node("TYPE", "d"))))
    got, out_idx = parser._Parser(tokens).params(0)
    assert out_idx == 8
    assert want == got

def test_type_list():
    tokens = lexer.tokenize("a, b")
    want = (
        Node("types")
            .addkid(Node("TYPE", "a"))
            .addkid(Node("TYPE", "b")))
    got, out_idx = parser._Parser(tokens).type_list(0)
    assert out_idx == 3
    assert want == got

def test_type_list_trailing_comma():
    tokens = lexer.tokenize("a, b,")
    want = (
        Node("types")
            .addkid(Node("TYPE", "a"))
            .addkid(Node("TYPE", "b")))
    got, out_idx = parser._Parser(tokens).type_list(0)
    assert out_idx == 4
    assert want == got

def test_type_expr_function_no_params():
    tokens = lexer.tokenize("function():a")
    want = (
        Node("function-type")
            .addkid(Node("types"))
            .addkid(Node("TYPE", "a")))
    got, out_idx = parser._Parser(tokens).type_expr(0)
    assert out_idx == 5
    assert want == got

def test_type_expr_function_params():
    tokens = lexer.tokenize("function(b,c):a")
    want = (
        Node("function-type")
            .addkid(Node("types")
                .addkid(Node("TYPE", "b"))
                .addkid(Node("TYPE", "c")))
            .addkid(Node("TYPE", "a")))
    got, out_idx = parser._Parser(tokens).type_expr(0)
    assert out_idx == 8
    assert want == got

def test_while_stmt():
    tokens = lexer.tokenize("while condition { print x }")
    want = Node("while").addkid(Node("NAME", "condition")).addkid(
            Node("stmts").addkid(Node("print").addkid(Node("NAME", "x"))))
    got, out_idx = parser._Parser(tokens).while_stmt(0)
    assert out_idx == 6
    assert want == got

def test_break_stmt():
    tokens = lexer.tokenize("break")
    want = Node("break")
    got, out_idx = parser._Parser(tokens).break_stmt(0)
    assert out_idx == 1
    assert want == got

def test_continue_stmt():
    tokens = lexer.tokenize("continue")
    want = Node("continue")
    got, out_idx = parser._Parser(tokens).continue_stmt(0)
    assert out_idx == 1
    assert want == got

def test_if_stmt():
    tokens = lexer.tokenize("if condition { print x }")
    want = Node("if").addkid(Node("NAME", "condition")).addkid(
            Node("stmts").addkid(Node("print").addkid(Node("NAME", "x"))))
    got, out_idx = parser._Parser(tokens).if_stmt(0)
    assert out_idx == 6
    assert want == got
 
def test_if_else_stmt():
    tokens = lexer.tokenize("if x { print y } else { print z }")
    want = (
        Node("if")
            .addkid(Node("NAME", "x"))
            .addkid(Node("stmts")
                .addkid(Node("print").addkid(Node("NAME", "y"))))
            .addkid(Node("stmts")
                .addkid(Node("print").addkid(Node("NAME", "z"))))
            )
    got, out_idx = parser._Parser(tokens).if_stmt(0)
    assert out_idx == 11
    assert want == got

def test_if_elseif_else_stmt():
    tokens = lexer.tokenize('''
        if x { print y } else if z { print a } else { print b }''')
    want = (
        Node("if")
            .addkid(Node("NAME", "x"))
            .addkid(Node("stmts")
                .addkid(Node("print").addkid(Node("NAME", "y"))))
            .addkid(Node("stmts")
                .addkid(Node("if")
                    .addkid(Node("NAME", "z"))
                    .addkid(Node("stmts")
                        .addkid(Node("print").addkid(Node("NAME", "a"))))
                    .addkid(Node("stmts")
                        .addkid(Node("print").addkid(Node("NAME", "b")))))))
    got, out_idx = parser._Parser(tokens).if_stmt(0)
    assert out_idx == 18
    assert want == got

def test_stmt_block_stmt():
    tokens = lexer.tokenize("{ print x }")
    want = Node("stmts").addkid(Node("print").addkid(Node("NAME", "x")))
    got, out_idx = parser._Parser(tokens).stmt(0)
    assert out_idx == 4
    assert want == got

def test_return_stmt():
    tokens = lexer.tokenize("return x + y")
    want = Node("return").addkid(
            Node("+").addkid(Node("NAME", "x")).addkid(Node("NAME", "y")))
    got, out_idx = parser._Parser(tokens).return_stmt(0)
    assert out_idx == 4
    assert want == got

def test_print_stmt():
    tokens = lexer.tokenize("print x + y")
    want = Node("print").addkid(
            Node("+").addkid(Node("NAME", "x")).addkid(Node("NAME", "y")))
    got, out_idx = parser._Parser(tokens).print_stmt(0)
    assert out_idx == 4
    assert want == got

def test_assign_stmt():
    tokens = lexer.tokenize("z = x + y")
    want = Node("assign").addkid(Node("NAME", "z")).addkid(
            Node("+").addkid(Node("NAME", "x")).addkid(Node("NAME", "y")))
    got, out_idx = parser._Parser(tokens).stmt(0)
    assert out_idx == 5
    assert want == got

def test_decl_stmt():
    tokens = lexer.tokenize("var z = x + y")
    want = Node("decl").addkid(Node("NAME", "z")).addkid(
            Node("+").addkid(Node("NAME", "x")).addkid(Node("NAME", "y")))
    got, out_idx = parser._Parser(tokens).stmt(0)
    assert out_idx == 6
    assert want == got

def test_label_stmt():
    tokens = lexer.tokenize("label: while x { print y }")
    want = (
        Node("label")
            .addkid(Node("NAME", "label"))
            .addkid(Node("while")
                .addkid(Node("NAME", "x"))
                .addkid(Node("stmts")
                    .addkid(Node("print")
                        .addkid(Node("NAME", "y"))))))
    got, out_idx = parser._Parser(tokens).stmt(0)
    assert out_idx == 8
    assert want == got

def test_expr_stmt():
    tokens = lexer.tokenize("hi()")
    want = (
        Node("expr-stmt")
            .addkid(Node("call")
                .addkid(Node("NAME", "hi"))
                .addkid(Node("exprs"))))
    got, out_idx = parser._Parser(tokens).stmt(0)
    assert out_idx == 3
    assert want == got

def test_expr_stmt_2():
    tokens = lexer.tokenize("1")
    want = (
        Node("expr-stmt")
            .addkid(Node("INTEGER", 1)))
    got, out_idx = parser._Parser(tokens).stmt(0)
    assert out_idx == 1
    assert want == got

def test_expr_stmt_3():
    tokens = lexer.tokenize("1.1")
    want = (
        Node("expr-stmt")
            .addkid(Node("FLOAT", 1.1)))
    got, out_idx = parser._Parser(tokens).stmt(0)
    assert out_idx == 1
    assert want == got

def test_expr_stmt_4():
    tokens = lexer.tokenize("!1")
    want = (
        Node("expr-stmt")
            .addkid(Node("not")
                .addkid(Node("INTEGER", 1))))
    got, out_idx = parser._Parser(tokens).stmt(0)
    assert out_idx == 2
    assert want == got

def test_expr_stmt_5():
    tokens = lexer.tokenize("-1")
    want = (
        Node("expr-stmt")
            .addkid(Node("negate")
                .addkid(Node("INTEGER", 1))))
    got, out_idx = parser._Parser(tokens).stmt(0)
    assert out_idx == 2
    assert want == got

def test_expr_stmt_6():
    tokens = lexer.tokenize("(1)")
    want = (
        Node("expr-stmt")
            .addkid(Node("INTEGER", 1)))
    got, out_idx = parser._Parser(tokens).stmt(0)
    assert out_idx == 3
    assert want == got

def test_stmts():
    tokens = lexer.tokenize("var z = x + y print q/r")
    want = (
        Node("stmts")
            .addkid(Node("decl").addkid(Node("NAME", "z")).addkid(
                Node("+")
                    .addkid(Node("NAME", "x"))
                    .addkid(Node("NAME", "y"))))
            .addkid(Node("print").addkid(
                Node("/")
                    .addkid(Node("NAME", "q"))
                    .addkid(Node("NAME", "r")))))
    got, out_idx = parser._Parser(tokens).stmts(0)
    assert out_idx == len(tokens)
    assert want == got

def test_parse_dangling():
    with pytest.raises(parser.SileParseError):
        tokens = lexer.tokenize("var z = x + y print q/r print")
        parser._Parser(tokens).parse()
