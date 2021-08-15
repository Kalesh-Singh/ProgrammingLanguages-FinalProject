#!/usr/bin/env python2

import functools

import dfa
import genlexer

## This is the file you want to import to use the lexer. It has the 
## lists of tokens and the token-name to id reverse map.

TOKENS = genlexer.tokens
TOKEN_IDS = genlexer.token_ids

class SileLexError(Exception): pass

@functools.total_ordering
class Token(object):

    def __init__(self, kind, kind_name, lexeme, value):
        self.kind = kind
        self.kind_name = kind_name
        self.lexeme = lexeme
        self.value = value

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        return (
            self.kind == other.kind and
            self.lexeme == other.lexeme
        )

    def __lt__(self, other):
        return (self.kind, self.lexeme) < (other.kind, other.lexeme)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.lexeme == self.kind_name:
            return '"{}"'.format(repr(self.lexeme)[1:-1])
        return '{}:"{}"'.format(self.kind_name, repr(self.lexeme)[1:-1])

def tokenize(text):
    '''tokenizes a string according to the sile grammar.'''
    tokens = list()
    try:
        matches = dfa.tokenize(text)
    except Exception, e:
        raise SileLexError(e)
    for match in matches:
        if   match.match_id == TOKEN_IDS["WHITESPACE"]: continue
        elif match.match_id == TOKEN_IDS["LINE_COMMENT"]: continue
        elif match.match_id == TOKEN_IDS["COMMENT"]: continue
        value = match.lexeme
        if match.match_id == TOKEN_IDS["FLOAT"]:
            value = float(match.lexeme)
        elif match.match_id == TOKEN_IDS["INTEGER"]:
            value = int(match.lexeme)
        elif match.match_id == TOKEN_IDS["INTEGER_hex"]:
            value = int(match.lexeme, 16)
            match.match_id = TOKEN_IDS["INTEGER"]
        elif match.match_id == TOKEN_IDS["INTEGER_octal"]:
            value = int(match.lexeme, 8)
            match.match_id = TOKEN_IDS["INTEGER"]
        token = Token(match.match_id, TOKENS[match.match_id], match.lexeme, value)
        tokens.append(token)
    return tokens

