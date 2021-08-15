#!/usr/bin/env python2

from collections import namedtuple

# This file defines the types in SILE. There are two kinds
#
# 1. primitive types (called basic types)
# 2. function types

BasicTuple = namedtuple("Basic", ("name"))
class Basic(BasicTuple):

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.name

UNIT = Basic("unit") # the empty type
BOOLEAN = Basic("boolean")
INT = Basic("int")
FLOAT = Basic("float")

# type for a branch label
# NOTE: not an allowed type name in a user program
LABEL = Basic("label")

# mapping of allowed basic type names to their type
Basics = {
    UNIT.name: UNIT,
    BOOLEAN.name: BOOLEAN,
    INT.name: INT,
    FLOAT.name: FLOAT,
}


FunctionTuple = namedtuple("Function", ("params", "returns"))
class Function(FunctionTuple):

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        params = [str(param) for param in self.params]
        return "function({}):{}".format(", ".join(params), self.returns)

