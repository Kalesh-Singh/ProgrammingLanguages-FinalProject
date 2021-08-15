#!/usr/bin/env python2

import sys
import collections
import json

import il
import frontend
import sile_types
from sile_types.check import TypeError
from frontend.ast import Node

## Implements the top level interface for SILE. you will not need to
## edit this file.

Config = collections.namedtuple("Config", ("input", "mode", "visualize"))

def run(config):
    try:
        tokens = frontend.tokenize(config.input)
    except frontend.SileLexError, e:
        print >>sys.stderr, e
        return 1

    if config.mode == TOKENS:
        for token in tokens:
            print token
        return 0

    try:
        ast = frontend.parse(tokens)
    except frontend.SileParseError, e:
        print >>sys.stderr, e
        return 2

    if config.mode == AST and config.visualize:
        print ast.dotty()
        return 0
    elif config.mode == AST:
        print ast.serialize()
        return 0

    try:
        typed = sile_types.check(ast)
    except TypeError, e:
        print >>sys.stderr, e
        return 3

    if config.mode == TYPED and config.visualize:
        print typed.dotty()
        return 0
    elif config.mode == TYPED:
        print typed.serialize()
        return 0

    try:
        mods = il.generate(typed)
    except il.IlGenException, e:
        print >>sys.stderr, e
        return 4

    if config.mode == IL and config.visualize:
        for mod in mods.modules.values():
            for fn in mod.functions:
                print fn.dotty()
        return 0
    elif config.mode == IL:
        print mods
        return 0

    il.run(mods)
    return 0

def indent(string, prefix):
    return '\n'.join(
        prefix + line
        for line in string.split("\n"))

def dotty(config):
    try:
        tokens = frontend.tokenize(config.input)
    except frontend.SileLexError, e:
        print >>sys.stderr, e
        return 1
    try:
        ast = frontend.parse(tokens)
    except frontend.SileParseError, e:
        print >>sys.stderr, e
        return 2

    print ast.dotty()

    module = il.generate(ast)
    for fn in module.functions:
        print fn.dotty()

    return 0

ModeTuple = collections.namedtuple("Mode", ("name", "visualizable"))
class Mode(ModeTuple):

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name

EXEC = Mode("exec", False)
TOKENS = Mode("tokens", False)
AST = Mode("ast", True)
TYPED = Mode("typed", True)
IL = Mode("il", True)

