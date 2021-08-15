#!/usr/bin/env python2

import os
import subprocess

## This file does two things
##
## 1. It defines the token kinds and patterns
## 2. It generates the lexer when run:
##    $ python src/frontend/genlexer.py
##
## if you add/remove a token, you must regenerate the lexer. if you don't
## you will get weird errors.

DIR=os.path.dirname(__file__)

patterns = (
    ('VAR', r'var'),
    ('PRINT', r'print'),
    ('IF', r'if'),
    ('ELSE', r'else'),
    ('FUNCTION', r'function'),
    ('RETURN', r'return'),
    ('WHILE', r'while'),
    ('BREAK', r'break'),
    ('CONTINUE', r'continue'),
    ('+', r'\+'),
    ('-', r'\-'),
    ('*', r'\*'),
    ('/', r'\/'),
    ('%', r'\%'),
    ('=', r'\='),
    ('(', r'\('),
    (')', r'\)'),
    ('{', r'\{'),
    ('}', r'\}'),
    ('!', r'\!'),
    (':', r'\:'),
    (',', r'\,'),
    ('&&', r'\&\&'),
    ('||', r'\|\|'),
    ('==', r'\=\='),
    ('!=', r'\!\='),
    ('<', r'\<'),
    ('>', r'\>'),
    ('<=', r'\<\='),
    ('>=', r'\>\='),
    ('NAME', r'[a-zA-Z][a-zA-Z0-9_]*'),
    ('INTEGER_octal', r'0[0-7]+'),
    ('INTEGER_hex', r'0x[0-9a-fA-F]+'),
    ('INTEGER', r'[0-9]+'),
    ('FLOAT', r'[0-9]*(\.?)[0-9]+(e(\+|-)?[0-9]+)?'),
    ('LINE_COMMENT', r'//[^\n]*\n?'),
    ('COMMENT', r'/\*([^*]|\r|\n|(\*+([^*/]|\r|\n)))*\*+/'),
    ('WHITESPACE', r'( |\t|\n|\r)+'),
)

tokens = [name for name, pattern in patterns]
token_ids = {name:i for i, name in enumerate(tokens)}


def generate_lexer():
    args = [
        '--pattern={}'.format(pattern)
        for name, pattern in patterns
    ]
    with open(os.path.join(DIR, "dfa.py"), "w") as f:
        subprocess.check_call(['lexgen'] + args, stdout=f)

if __name__ == '__main__':
    generate_lexer()
    for i, token in enumerate(tokens):
        print i, token
