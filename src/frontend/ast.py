#!/usr/bin/env python2

import collections
import itertools


## This file contains the AST representation. You should not need to edit it :-)
## It is very similar to previous asts I have presented in class. It has some
## quality of life improvements by supporting serialization/deserialization.

class DeserializeException(Exception): pass

class Node(object):

    def __init__(self, label, value=None, type=None, children=None):
        self.label = label
        self.value = value
        self.type = type
        self.children = children if children is not None else list()

    def addkid(self, node):
        self.children.append(node)
        return self

    def kid(self, label, default=None):
        for kid in self.children:
            if kid.label == label:
                return kid
        return default

    def __eq__(self, other):
        if not isinstance(other, Node):
            return False
        for a, b in itertools.izip(self, other):
            if a.label != b.label or a.value != b.value:
                return False
        return True

    def __iter__(self):
        queue = collections.deque()
        queue.append(self)
        while len(queue) > 0:
            n = queue.popleft()
            for c in n.children:
                queue.append(c)
            yield n

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        value = ""
        if self.value is not None:
            value += ":" + str(self.value)
        if self.type is not None:
            value += ":" + str(self.type)
        label = "{}{}".format(self.label, value)
        kids = list()
        for child in self.children:
            kids.append(str(child))
        if len(kids) <= 0:
            return label
        return "({} {})".format(label, ' '.join(kids))

    def dotty(self):
        def string(n):
            value = ''
            if n.value is not None:
                value += ' : {}'.format(n.value)
            if self.type is not None:
                value += " : {}".format(self.type)
            label = '{}{}'.format(n.label, value)
            return repr(label)[1:-1]
        node = '%(name)s [label="%(label)s"];'
        leaf = '%(name)s [label="%(label)s" style="filled" fillcolor="#dddddd"];'
        edge = '%s -> %s;'
        nodes = list()
        edges = list()

        i = 0
        queue = collections.deque()
        queue.append((i, self))
        i += 1
        while len(queue) > 0:
            c, n = queue.popleft()
            name = 'n%d' % c
            label = string(n)
            if not hasattr(n, 'children'): nodes.append(leaf % locals())
            elif not n.children: nodes.append(leaf % locals())
            else: nodes.append(node % locals())
            if not hasattr(n, 'children'): continue
            for c in n.children:
                edges.append(edge % (name, ('n%d' % i)))
                queue.append((i, c))
                i += 1
        dot = 'digraph {\nnode[shape=rect]\n'
        dot += '\n'.join(nodes) + '\n' + '\n'.join(edges) + '\n}\n'
        return dot

    def serialize(self):
        return "\n".join(self._serialize())

    def _serialize(self):
        value = ""
        if self.value is not None:
            value = str(self.value)
        type = ""
        if self.type is not None:
            type = str(self.type)
        lines = ['{}:{}:{}:{}'.format(len(self.children), self.label, value, type)]
        for kid in self.children:
            lines.extend(kid._serialize())
        return lines

    @staticmethod
    def deserialize(string):
        import lexer
        import parser
        import frontend
        from sile_types import types
        from sile_types.check import TypeChecker, TypeError

        def parse_type(line_idx, line, type_str):
            try:
                type_tokens = lexer.tokenize(type_str)
            except frontend.SileLexError, e:
                raise DeserializeException("line {} invalid type name: {}: {}".format(line_idx, line, e))
            try:
                type_node, idx = parser._Parser(type_tokens).type_expr(0)
                if idx != len(type_tokens):
                    raise DeserializeException("line {} invalid type name: {}".format(line_idx, line))
            except frontend.SileParseError, e:
                raise DeserializeException("line {} invalid type name: {}: {}".format(line_idx, line, e))
            try:
                return TypeChecker().type_expr(type_node).type
            except TypeError, e:
                raise DeserializeException("line {} invalid type name: {}: {}".format(line_idx, line, e))

        def parse_line(line_idx, line):
            line = line.strip()
            kids, label, value, type = line.split(":", 3)
            try:
                kids = int(kids)
            except ValueError, e:
                raise DeserializeException("line {} child count must be int: {}".format(line_idx, line))
            type = parse_type(line_idx, line, type)
            try:
                if label == 'INTEGER':
                    value = int(value)
                elif label == 'FLOAT':
                    value = float(value)
                if value == '':
                    value = None
            except ValueError, e:
                raise DeserializeException("line {} invalid value: {}".format(line_idx, line))
            return Node(label, value, type=type), kids

        lines = string.strip().splitlines()
        stack = list()
        root = None
        for idx, line in enumerate(lines):
            n, kids = parse_line(idx, line)
            if root is None:
                root = n
            elif len(stack) <= 0:
                raise DeserializeException("multi-root tree!")
            else:
                parent, count = stack.pop()
                parent.addkid(n)
                if count - 1 > 0:
                    stack.append((parent, count-1))
            if kids > 0 :
                stack.append((n, kids))
        if len(stack) > 0:
            raise DeserializeException("malformed tree!")
        return root

