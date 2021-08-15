#!/usr/bin/env python2

from frontend import lexer

def test_punctutation():
    tokens = lexer.tokenize("+ - * / ( ) = { } ! : , && || == != < > <= >=")
    expected = [
        lexer.Token(lexer.TOKEN_IDS['+'], '+', '+', '+'),
        lexer.Token(lexer.TOKEN_IDS['-'], '-', '-', '-'),
        lexer.Token(lexer.TOKEN_IDS['*'], '*', '*', '*'),
        lexer.Token(lexer.TOKEN_IDS['/'], '/', '/', '/'),
        lexer.Token(lexer.TOKEN_IDS['('], '(', '(', '('),
        lexer.Token(lexer.TOKEN_IDS[')'], ')', ')', ')'),
        lexer.Token(lexer.TOKEN_IDS['='], '=', '=', '='),
        lexer.Token(lexer.TOKEN_IDS['{'], '{', '{', '{'),
        lexer.Token(lexer.TOKEN_IDS['}'], '}', '}', '}'),
        lexer.Token(lexer.TOKEN_IDS['!'], '!', '!', '!'),
        lexer.Token(lexer.TOKEN_IDS[':'], ':', ':', ':'),
        lexer.Token(lexer.TOKEN_IDS[','], ',', ',', ','),
        lexer.Token(lexer.TOKEN_IDS['&&'], '&&', '&&', '&&'),
        lexer.Token(lexer.TOKEN_IDS['||'], '||', '||', '||'),
        lexer.Token(lexer.TOKEN_IDS['=='], '==', '==', '=='),
        lexer.Token(lexer.TOKEN_IDS['!='], '!=', '!=', '!='),
        lexer.Token(lexer.TOKEN_IDS['<'], '<', '<', '<'),
        lexer.Token(lexer.TOKEN_IDS['>'], '>', '>', '>'),
        lexer.Token(lexer.TOKEN_IDS['<='], '<=', '<=', '<='),
        lexer.Token(lexer.TOKEN_IDS['>='], '>=', '>=', '>='),
    ]
    assert tokens == expected

def test_keywords():
    tokens = lexer.tokenize("var print if else function return")
    expected = [
        lexer.Token(lexer.TOKEN_IDS['VAR'], 'VAR', 'var', 'var'),
        lexer.Token(lexer.TOKEN_IDS['PRINT'], 'PRINT', 'print', 'print'),
        lexer.Token(lexer.TOKEN_IDS['IF'], 'IF', 'if', 'if'),
        lexer.Token(lexer.TOKEN_IDS['ELSE'], 'ELSE', 'else', 'else'),
        lexer.Token(
            lexer.TOKEN_IDS['FUNCTION'], 'FUNCTION', 'function', 'function'),
        lexer.Token(
            lexer.TOKEN_IDS['RETURN'], 'RETURN', 'return', 'return'),
    ]
    assert tokens == expected

def test_name():
    tokens = lexer.tokenize("hi HI hI Ih hI_1")
    expected = [
        lexer.Token(lexer.TOKEN_IDS['NAME'], 'NAME', 'hi', 'hi'),
        lexer.Token(lexer.TOKEN_IDS['NAME'], 'NAME', 'HI', 'HI'),
        lexer.Token(lexer.TOKEN_IDS['NAME'], 'NAME', 'hI', 'hI'),
        lexer.Token(lexer.TOKEN_IDS['NAME'], 'NAME', 'Ih', 'Ih'),
        lexer.Token(lexer.TOKEN_IDS['NAME'], 'NAME', 'hI_1', 'hI_1'),
    ]
    assert tokens == expected

def test_number():
    tokens = lexer.tokenize("0 016 0xa 123 1.0 .23 .01e-3 113.2e2 13.33e+2")
    expected = [
        lexer.Token(lexer.TOKEN_IDS['INTEGER'], 'INTEGER', '0', 0),
        lexer.Token(lexer.TOKEN_IDS['INTEGER'], 'INTEGER', '016', 14),
        lexer.Token(lexer.TOKEN_IDS['INTEGER'], 'INTEGER', '0xa', 10),
        lexer.Token(lexer.TOKEN_IDS['INTEGER'], 'INTEGER', '123', 123),
        lexer.Token(lexer.TOKEN_IDS['FLOAT'], 'FLOAT', '1.0', 1.0),
        lexer.Token(lexer.TOKEN_IDS['FLOAT'], 'FLOAT', '.23', .23),
        lexer.Token(lexer.TOKEN_IDS['FLOAT'], 'FLOAT', '.01e-3', .01e-3),
        lexer.Token(lexer.TOKEN_IDS['FLOAT'], 'FLOAT', '113.2e2', 113.2e2),
        lexer.Token(lexer.TOKEN_IDS['FLOAT'], 'FLOAT', '13.33e+2', 13.33e+2),
    ]
    assert tokens == expected

def test_comments():
    tokens = lexer.tokenize('''
    hi
    // asdfwo
    /* sadf 
    sdfw
    */ bye
    ''')
    expected = [
        lexer.Token(lexer.TOKEN_IDS['NAME'], 'NAME', 'hi', 'hi'),
        lexer.Token(lexer.TOKEN_IDS['NAME'], 'NAME', 'bye', 'bye'),
    ]
    assert tokens == expected
