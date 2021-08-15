#!/usr/bin/env python2

from frontend.ast import Node
from frontend.lexer import TOKENS, TOKEN_IDS

## This file defines the recursive descent parser. You will likely
## need to make changes in this file!

def parse(tokens):
    '''
    parses a list of sile tokens into a sile ast.
    param tokens: a list of frontend.lexer.Token
    returns: frontend.ast.Node
    '''
    ## Wat.
    ##  - Creates a _Parser object (instance of the class)
    ##  - Calls the parse method
    ## This design hides the production methods.
    return _Parser(tokens).parse()

class SileParseError(Exception): pass

class _Parser(object):
    ''' _Parser - a "private" class representing the parser.  '''

    ## How this works:
    ##
    ## Most methods are "productions" of the grammar. Each production
    ## has the following form:
    ##
    ## def production_rule(self, idx):
    ##     return AST_NODE, NEW_IDX
    ##
    ## The self parameter is just the usual reference to the current _Parser
    ##   object
    ##
    ## The idx parameter is the index of next token to read from self.tokens.
    ##
    ## The return variables are interesting and specify the "contract"
    ##
    ## 1. AST_NODE: this is an ast node representing the ast built by the
    ##    function. It is of type frontend.ast.Node
    ##
    ## 2. NEW_IDX: the updated index of the next token to read after this
    ##    function returns. For instance if you had a function that matched
    ##    one token and it was given the idx=7, it would return new_idx=8.

    def __init__(self, tokens):
        self.tokens = tokens

    def parse(self):
        stmts, stmts_idx = self.stmts(0)
        if stmts_idx != len(self.tokens):
            raise SileParseError(
                    "unconsumed input: {}".format(self.tokens[stmts_idx:]))
        return stmts

    ############## PRODUCTIONS ################################################

    # Stmts -> Stmt Stmts
    #        | Stmt
    def stmts(self, idx):
        stmt, stmt_idx = self.stmt(idx)
        n = Node("stmts").addkid(stmt)
        try:
            stmts, stmts_idx = self.stmts(stmt_idx)
        except SileParseError, e:
            ## Stmts failed to match, so we must have matched the second rule.
            ## Stmts -> Stmt.
            return n, stmt_idx
        if stmts is not None:
            for kid in stmts.children:
                n.addkid(kid)
        return n, stmts_idx

    # Stmt -> DeclStmt
    #       | PrintStmt
    #       | IfStmt
    #       | BlockStmt
    #       | AssignStmt
    #       | FunctionStmt
    #       | ReturnStmt
    #       | BreakStmt
    #       | ContinueStmt
    #       | ExprStmt
    def stmt(self, idx):
        lookahead = {
            TOKEN_IDS["VAR"]: self.decl_stmt,
            TOKEN_IDS["NAME"]: self.name_start_stmts,
            TOKEN_IDS["PRINT"]: self.print_stmt,
            TOKEN_IDS["{"]: self.block_stmt,

            # DONE
            TOKEN_IDS["IF"]: self.if_stmt,

            TOKEN_IDS["FUNCTION"]: self.function_stmt,
            TOKEN_IDS["RETURN"]: self.return_stmt,
            TOKEN_IDS["WHILE"]: self.while_stmt,

            # DONE
            TOKEN_IDS["BREAK"]: self.break_stmt,
            TOKEN_IDS["CONTINUE"]: self.continue_stmt,

            # lookahead for expr-stmt
            TOKEN_IDS["!"]: self.expr_stmt,
            TOKEN_IDS["-"]: self.expr_stmt,
            TOKEN_IDS["INTEGER"]: self.expr_stmt,
            TOKEN_IDS["FLOAT"]: self.expr_stmt,
            TOKEN_IDS["("]: self.expr_stmt,
        }
        return self.dispatch(idx, lookahead)

    # DeclStmt -> VAR NAME = Expr
    def decl_stmt(self, idx):
        _, var_idx = self.consume(idx, TOKEN_IDS["VAR"])
        name_token, name_idx = self.consume(var_idx, TOKEN_IDS["NAME"])
        _, assign_idx = self.consume(name_idx, TOKEN_IDS["="])
        expr, expr_idx = self.expr(assign_idx)
        n = Node("decl").addkid(Node("NAME", name_token.lexeme)).addkid(expr)
        return n, expr_idx

    # NameStartStmts -> AssignStmt
    #                 | LabelStmt
    #                 | Expr
    def name_start_stmts(self, idx):
        name_token, name_idx = self.consume(idx, TOKEN_IDS["NAME"])
        lookahead = {
            TOKEN_IDS["="]: self.assign_stmt(name_token),
            TOKEN_IDS[":"]: self.label_stmt(name_token),
        }
        try:
            return self.dispatch(name_idx, lookahead)
        except SileParseError, e:
            return self.expr_stmt(idx)

    def expr_stmt(self, idx):
        expr, expr_idx = self.expr(idx)
        n = Node("expr-stmt").addkid(expr)
        return n, expr_idx

    # AssignStmt -> NAME = Expr
    def assign_stmt(self, name_token):
        def assign_stmt(idx):
            _, eq_idx = self.consume(idx, TOKEN_IDS["="])
            expr, expr_idx = self.expr(eq_idx)
            n = Node("assign").addkid(Node("NAME", name_token.lexeme)).addkid(expr)
            return n, expr_idx
        return assign_stmt

    # LabelStmt -> NAME: Stmt
    def label_stmt(self, name_token):
        def label_stmt(idx):
            _, colon_idx = self.consume(idx, TOKEN_IDS[":"])
            stmt, stmt_idx = self.stmt(colon_idx)
            if stmt.label not in ["while",]:
                raise SileParesError("you labeled a non-loop statement", stmt)
            n = Node("label").addkid(Node("NAME", name_token.lexeme)).addkid(stmt)
            return n, stmt_idx
        return label_stmt

    # PrintStmt -> PRINT Expr
    def print_stmt(self, idx):
        _, print_idx = self.consume(idx, TOKEN_IDS["PRINT"])
        expr, expr_idx = self.expr(print_idx)
        n = Node("print").addkid(expr)
        return n, expr_idx

    # BlockStmt -> { Stmts }
    def block_stmt(self, idx):
        _, open_curly_idx = self.consume(idx, TOKEN_IDS["{"])
        stmts, stmts_idx = self.stmts(open_curly_idx)
        _, close_curly_idx = self.consume(stmts_idx, TOKEN_IDS["}"])
        return stmts, close_curly_idx

    # IfStmt -> if Expr BlockStmt else IfStmt
    # IfStmt -> if Expr BlockStmt else BlockStmt
    # IfStmt -> if Expr BlockStmt
    def if_stmt(self, idx):
        # DONE
        _, if_idx = self.consume(idx, TOKEN_IDS["IF"])
        expr, expr_idx = self.expr(if_idx)
        blk, blk_idx = self.block_stmt(expr_idx)
        n = Node("if").addkid(expr).addkid(blk)
        try:
            els, els_idx = self.consume(blk_idx, TOKEN_IDS["ELSE"])
        except SileParseError, e:
            return n, blk_idx
        if self.matches(els_idx, TOKEN_IDS["IF"]):
            if2, if2_idx = self.if_stmt(els_idx)
            n.addkid(Node("stmts").addkid(if2))
            return n, if2_idx
        blk2, blk2_idx = self.block_stmt(els_idx)
        n.addkid(blk2)
        return n, blk2_idx

    # WhileStmt -> while condition BlockStmt
    def while_stmt(self, idx):
        _, if_idx = self.consume(idx, TOKEN_IDS["WHILE"])
        condition, condition_idx = self.expr(if_idx)
        block, block_idx = self.block_stmt(condition_idx)
        n = (Node("while")
             .addkid(condition).addkid(block))
        return n, block_idx

    # BreakStmt -> BREAK
    #            | BREAK NAME
    def break_stmt(self, idx):
        # DONE: Test break with name
        bk, bk_idx = self.consume(idx, TOKEN_IDS["BREAK"])
        n = Node("break")
        if not self.matches(bk_idx, TOKEN_IDS["NAME"]):
            return n, bk_idx
        name, name_idx = self.consume(bk_idx, TOKEN_IDS["NAME"])
        name_node = Node("NAME", name.lexeme)
        n.addkid(name_node)
        return n, name_idx

    # ContinueStmt -> CONTINUE
    #               | CONTINUE NAME
    def continue_stmt(self, idx):
        # DONE: Test continue with name
        cnt, cnt_idx = self.consume(idx, TOKEN_IDS["CONTINUE"])
        n = Node("continue")
        if not self.matches(cnt_idx, TOKEN_IDS["NAME"]):
            return n, cnt_idx
        name, name_idx = self.consume(cnt_idx, TOKEN_IDS["NAME"])
        name_node = Node("NAME", name.lexeme)
        n.addkid(name_node)
        return n, name_idx

    # FunctionStmt -> function NAME ( Params ) : TypeExpr BlockStmt
    def function_stmt(self, idx):
        _, func_idx = self.consume(idx, TOKEN_IDS["FUNCTION"])
        name, name_idx = self.consume(func_idx, TOKEN_IDS["NAME"])
        _, open_paren_idx = self.consume(name_idx, TOKEN_IDS["("])
        params, params_idx = self.params(open_paren_idx)
        _, close_paren_idx = self.consume(params_idx, TOKEN_IDS[")"])
        _, colon_idx = self.consume(close_paren_idx, TOKEN_IDS[":"])
        type_expr, type_expr_idx = self.type_expr(colon_idx)
        block, block_idx = self.block_stmt(type_expr_idx)
        n = (Node("function")
            .addkid(Node("NAME", name.lexeme))
            .addkid(params)
            .addkid(type_expr)
            .addkid(block))
        return n, block_idx

    # ReturnStmt -> RETURN Expr
    def return_stmt(self, idx):
        _, return_idx = self.consume(idx, TOKEN_IDS["RETURN"])
        expr, expr_idx = self.expr(return_idx)
        n = Node("return").addkid(expr)
        return n, expr_idx

    # TypeExpr -> NAME
    #           | function(TypeList):TypeExpr
    def type_expr(self, idx):
        lookahead = {
            TOKEN_IDS["NAME"]: self.type_expr_name,
            TOKEN_IDS["FUNCTION"]: self.type_expr_function,
        }
        return self.dispatch(idx, lookahead)

    # TypeExpr -> NAME
    def type_expr_name(self, idx):
        name, name_idx = self.consume(idx, TOKEN_IDS["NAME"])
        n = Node("TYPE", name.lexeme)
        return n, name_idx

    # TypeExpr -> function(TypeList):TypeExpr
    def type_expr_function(self, idx):
        _, func_idx = self.consume(idx, TOKEN_IDS["FUNCTION"])
        _, open_paren_idx = self.consume(func_idx, TOKEN_IDS["("])
        param_types, param_types_idx = self.type_list(open_paren_idx)
        _, close_paren_idx = self.consume(
                param_types_idx, TOKEN_IDS[")"])
        _, colon_idx = self.consume(close_paren_idx, TOKEN_IDS[":"])
        return_type, return_type_idx = self.type_expr(colon_idx)
        n = (Node("function-type")
                .addkid(param_types).addkid(return_type))
        return n, return_type_idx

    # TypeList -> TypeExpr , TypeList
    #           | TypeExpr
    #           | epsilon
    def type_list(self, idx):
        try:
            type_expr, type_expr_idx = self.type_expr(idx)
        except SileParseError, e:
            # matches epsilon, the empty string
            return Node("types"), idx
        if not self.matches(type_expr_idx, TOKEN_IDS[","]):
            n = Node("types").addkid(type_expr)
            return n, type_expr_idx
        _, comma_idx = self.consume(type_expr_idx, TOKEN_IDS[","])
        types, types_idx = self.type_list(comma_idx)
        types.children.insert(0, type_expr)
        return types, types_idx

    # Params -> Param , Params
    #         | Param
    #         | epsilon
    def params(self, idx):
        try:
            param, param_idx = self.param(idx)
        except SileParseError, e:
            # matches epsilon, the empty string
            return Node("params"), idx
        if not self.matches(param_idx, TOKEN_IDS[","]):
            n = Node("params").addkid(param)
            return n, param_idx
        _, comma_idx = self.consume(param_idx, TOKEN_IDS[","])
        params, params_idx = self.params(comma_idx)
        params.children.insert(0, param)
        return params, params_idx

    # Params -> Expr : TypeExpr
    def param(self, idx):
        expr, expr_idx = self.expr(idx)
        _, colon_idx = self.consume(expr_idx, TOKEN_IDS[":"])
        type_expr, type_expr_idx = self.type_expr(colon_idx)
        n = Node("param").addkid(expr).addkid(type_expr)
        return n, type_expr_idx

    # Expr -> AndExpr OrExpr
    def expr(self, idx):
        and_expr, and_expr_idx = self.and_expr(idx)
        or_expr, or_expr_idx = self.or_expr(and_expr_idx)
        n = self.binop_tree(and_expr, or_expr)
        return n, or_expr_idx

    # OrExpr -> || AndExpr OrExpr
    #         | epsilon
    def or_expr(self, idx):
        try:
            op, op_idx = self.consume(idx, TOKEN_IDS["||"])
        except SileParseError, e:
            # matches epsilon, the empty string
            return Node("or_expr'"), idx
        and_expr, and_expr_idx = self.and_expr(op_idx)
        or_expr, or_expr_idx = self.or_expr(and_expr_idx)
        or_expr.children.insert(0, Node(op.kind_name).addkid(and_expr))
        return or_expr, or_expr_idx

    # AndExpr -> NotExpr AndExpr'
    def and_expr(self, idx):
        not_expr, not_expr_idx = self.not_expr(idx)
        and_expr_prime, and_expr_prime_idx = \
                self.and_expr_prime(not_expr_idx)
        n = self.binop_tree(not_expr, and_expr_prime)
        return n, and_expr_prime_idx

    # AndExpr' -> && NotExpr AndExpr'
    #           | epsilon
    def and_expr_prime(self, idx):
        try:
            op, op_idx = self.consume(idx, TOKEN_IDS["&&"])
        except SileParseError, e:
            # matches epsilon, the empty string
            return Node("and_expr'"), idx
        not_expr, not_expr_idx = self.not_expr(op_idx)
        and_expr_prime, and_expr_prime_idx = \
                self.and_expr_prime(not_expr_idx)
        and_expr_prime.children.insert(0, Node(op.kind_name).addkid(not_expr))
        return and_expr_prime, and_expr_prime_idx

    # NotExpr -> ! Comparison
    #          | Comparison
    def not_expr(self, idx):
        try:
            _, op_idx = self.consume(idx, TOKEN_IDS["!"])
        except SileParseError, e:
            return self.comparison(idx)
        compare, compare_idx = self.comparison(op_idx)
        n = Node("not").addkid(compare)
        return n, compare_idx

    # Comparison -> ArithExpr (==|!=|<|>|<=|>=) ArithExpr
    #             | ArithExpr
    def comparison(self, idx):
        ae, ae_idx = self.arith_expr(idx)
        try:
            op, op_idx = self.consume(
                    ae_idx, 
                    TOKEN_IDS["=="],
                    TOKEN_IDS["!="],
                    TOKEN_IDS["<"],
                    TOKEN_IDS[">"],
                    TOKEN_IDS["<="],
                    TOKEN_IDS[">="])
        except SileParseError, e:
            return ae, ae_idx
        ae2, ae_idx2 = self.arith_expr(op_idx)
        n = Node(op.kind_name).addkid(ae).addkid(ae2)
        return n, ae_idx2

    # ArithExpr -> Term ArithExpr'
    def arith_expr(self, idx):
        term, term_idx = self.term(idx)
        ae_prime, ae_prime_idx = self.arith_expr_prime(term_idx)
        n = self.binop_tree(term, ae_prime)
        return n, ae_prime_idx

    # ArithExpr' ->  + Term ArithExpr'
    #             |  - Term ArithExpr'
    #             |  epsilon
    def arith_expr_prime(self, idx):
        try:
            op, op_idx = self.consume(
                    idx, TOKEN_IDS["+"], TOKEN_IDS["-"])
        except SileParseError, e:
            # matches epsilon, the empty string
            return Node("expr'"), idx
        term, term_idx = self.term(op_idx)
        ae_prime, ae_prime_idx = self.arith_expr_prime(term_idx)
        ae_prime.children.insert(0, Node(op.kind_name).addkid(term))
        return ae_prime, ae_prime_idx

    # Term -> Unary Term'
    def term(self, idx):
        unary, unary_idx = self.unary(idx)
        term_prime, term_prime_idx = self.term_prime(unary_idx)
        n = self.binop_tree(unary, term_prime)
        return n, term_prime_idx

    # Term' ->  * Unary Term'
    #        |  / Unary Term'
    #        |  epsilon
    def term_prime(self, idx):
        try:
            op, op_idx = self.consume(idx, TOKEN_IDS["*"], TOKEN_IDS["/"], TOKEN_IDS['%'])
        except SileParseError, e:
            # matches epsilon, the empty string
            return Node("term'"), idx
        unary, unary_idx = self.unary(op_idx)
        term_prime, term_prime_idx = self.term_prime(unary_idx)
        term_prime.children.insert(0, Node(op.kind_name).addkid(unary))
        return term_prime, term_prime_idx

    def binop_tree(self, left, primes):
        cur = left
        for kid in primes.children:
            kid.children.insert(0, cur)
            cur = kid
        return cur

    # Unary ->  - Factor
    #        |  Factor
    def unary(self, idx):
        try:
            _, dash_idx = self.consume(idx, TOKEN_IDS["-"])
        except SileParseError, e:
            return self.factor(idx)
        factor, factor_idx = self.factor(dash_idx)
        n = Node("negate").addkid(factor)
        return n, factor_idx

    # Factor ->  FactorName
    #         |  FactorInteger
    #         |  FactorFloat
    #         |  FactorParen
    def factor(self, idx):
        lookahead = {
            TOKEN_IDS["NAME"]: self.factor_name,
            TOKEN_IDS["INTEGER"]: self.factor_int,
            TOKEN_IDS["FLOAT"]: self.factor_float,
            TOKEN_IDS["("]: self.factor_paren,
        }
        return self.dispatch(idx, lookahead)

    # FactorName -> NAME
    #             | NAME Suffixes
    def factor_name(self, idx):
        name, name_idx = self.consume(idx, TOKEN_IDS["NAME"])
        name_node = Node("NAME", name.lexeme)
        try:
            suffixes, suffixes_idx = self.suffixes(name_idx)
            n = name_node
            for suffix in suffixes.children:
                suffix.children.insert(0, n)
                n = suffix
            return n, suffixes_idx
        except SileParseError, e:
            return name_node, name_idx

    # Suffixes -> Suffix Suffixes
    #           | Suffix
    def suffixes(self, idx):
        suffix, suffix_idx = self.suffix(idx)
        try:
            suffixes, suffixes_idx = self.suffixes(suffix_idx)
            suffixes.children.insert(0, suffix)
            return suffixes, suffixes_idx
        except SileParseError, e:
            n = Node("suffixes").addkid(suffix)
            return n, suffix_idx

    # Suffix -> Call
    def suffix(self, idx):
        return self.call(idx)

    # Call -> ( ExprList )
    def call(self, idx):
        _, open_paren_idx = self.consume(idx, TOKEN_IDS["("])
        exprs, exprs_idx = self.expr_list(open_paren_idx)
        _, close_paren_idx = self.consume(exprs_idx, TOKEN_IDS[")"])
        n = Node("call").addkid(exprs)
        return n, close_paren_idx

    # ExprList -> Expr , ExprList
    #           | Expr
    #           | epsilon
    def expr_list(self, idx):
        try:
            expr, expr_idx = self.expr(idx)
        except SileParseError, e:
            # matches epsilon, the empty string
            return Node("exprs"), idx
        if not self.matches(expr_idx, TOKEN_IDS[","]):
            n = Node("exprs").addkid(expr)
            return n, expr_idx
        _, comma_idx = self.consume(expr_idx, TOKEN_IDS[","])
        exprs, exprs_idx = self.expr_list(comma_idx)
        exprs.children.insert(0, expr)
        return exprs, exprs_idx

    # FactorFloat -> FLOAT
    def factor_float(self, idx):
        number, number_idx = self.consume(idx, TOKEN_IDS["FLOAT"])
        n = Node("FLOAT", number.value)
        return n, number_idx

    # FactorInteger -> INTEGER
    def factor_int(self, idx):
        number, number_idx = self.consume(idx, TOKEN_IDS["INTEGER"])
        n = Node("INTEGER", number.value)
        return n, number_idx

    # FactorParen -> ( Expr )
    def factor_paren(self, idx):
        pass
        _, lparen_idx = self.consume(idx, TOKEN_IDS["("])
        expr, expr_idx = self.expr(lparen_idx)
        _, rparen_idx = self.consume(expr_idx, TOKEN_IDS[")"])
        return expr, rparen_idx

    ############## HELPER FUNCTIONS ###########################################

    def dispatch(self, idx, kinds_to_production):
        '''
        dispatch looks ahead one token (the token at idx) and calls
        the corresponding function in the kinds_to_production dictionary.
        param idx: current index into tokens
        param kinds_to_production: token kind -> function
        returns: Node, new_idx, error
        '''
        names = [TOKENS[kind] for kind in kinds_to_production.iterkeys()]
        if idx >= len(self.tokens):
            raise SileParseError("unexpected EOS, want one of: {}".format(names))
        tk = self.tokens[idx]
        for kind, func in kinds_to_production.iteritems():
            if tk.kind == kind:
                return func(idx)
        raise SileParseError("got {}, want one of: {}".format(tk, names))

    def consume(self, idx, *kinds):
        '''
        consume - tries to match one of the token kinds to the token at idx.
        the match is successful it returns that token and moves idx forward one.
        param idx: current index into tokens
        param kinds: allowed token kinds
        returns: Token, new_idx, error
        '''
        names = [TOKENS[kind] for kind in kinds]
        if idx >= len(self.tokens):
            raise SileParseError("unexpected EOS, want one of: {}".format(names))
        tk = self.tokens[idx]
        for kind in kinds:
            if tk.kind == kind:
                return tk, idx+1
        raise SileParseError("got {}, want one of: {}".format(tk, names))

    def matches(self, idx, kind):
        '''
        matches - checks if the token at idx is of the given kind. If there
        is an EOS it returns False.
        param idx: current index into tokens
        param kind: allowed token kind
        returns: boolean (true match, false doesn't match)
        '''
        if idx >= len(self.tokens):
            return False
        tk = self.tokens[idx]
        return tk.kind == kind


