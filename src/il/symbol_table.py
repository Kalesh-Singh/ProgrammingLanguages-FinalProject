#!/usr/bin/env python2

# The symbol table implementation. You will not need to edit this file.

class SymbolTable(object):

    def __init__(self, parent=None):
        self.parent = parent
        self.symbols = dict()
        self.scope_level = 0
        if parent is not None:
            self.scope_level = parent.scope_level + 1

    def pop(self):
        return self.parent

    def push(self):
        return SymbolTable(self)

    def tophas(self, name):
        return name in self.symbols

    def has(self, name):
        table = self
        while table is not None:
            if name in table.symbols:
                return True
            table = table.parent
        return False

    def get(self, name):
        table = self
        while table is not None:
            if name in table.symbols:
                return table.symbols[name]
            table = table.parent
        raise KeyError("name `{}` is not in the symbol table".format(name))

    def put(self, name, value):
        self.symbols[name] = value

    def set_current(self, name, value):
        table = self
        while table is not None:
            if name in table.symbols:
                table.symbols[name] = value
                return
            table = table.parent
        raise KeyError("name `{}` is not in the symbol table".format(name))

    def __getitem__(self, name):
        return self.get(name)

    def __setitem__(self, name, value):
        self.put(name, value)

    def __contains__(self, name):
        return self.has(name)

    def __repr__(self): return self.__str__()

    def __str__(self):
        tables = list()
        table = self
        while table is not None:
            tables.append(str(table.symbols))
            table = table.parent
        return ' -> '.join(tables)
