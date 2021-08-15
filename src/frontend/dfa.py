

def tokenize(input):
    return _Scanner(input).tokenize()

class Match(object):

    def __init__(self, match_id, lexeme):
        self.match_id = match_id
        self.lexeme = lexeme

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "Match({}, {})".format(self.match_id, repr(self.lexeme))

class _Scanner(object):

    def __init__(self, input):
        self.input = input
        self.idx = 0
        self.buf = list()
        self.tokens = list()

    def tokenize(self):
        state = self.start()
        while state != None:
            state = state()
        if self.idx != len(self.input):
            self.eosError()
        return self.tokens

    def mvto(self, next_state):
        if self.idx >= len(self.input):
            raise Exception("internal DFA error, index out of bounds")
        self.buf.append(self.input[self.idx])
        self.idx += 1
        return next_state

    def match(self, match_id):
        self.tokens.append(Match(match_id, ''.join(self.buf)))
        self.buf = list()
        if self.idx < len(self.input):
            return self.start()
        return None

    def eosError(self, state=None):
        raise Exception("UnconsumedInput, {}".format(repr(self.input[self.idx-len(self.buf):])))

    def error(self, state, expected):
        raise Exception("UnexpectedInput, {}. expected one of: {}".format(
            repr(self.input[self.idx]), 
            [chr(x) for x in expected]))

    def start(self):
        return self.state_87

    def state_0(self):
        self.error(0, [])

    def state_1(self):
        if self.idx >= len(self.input):
            return self.match(9)
        return self.match(9)

    def state_2(self):
        if self.idx >= len(self.input):
            return self.match(10)
        return self.match(10)

    def state_3(self):
        if self.idx >= len(self.input):
            return self.match(11)
        return self.match(11)

    def state_4(self):
        if self.idx >= len(self.input):
            return self.match(13)
        return self.match(13)

    def state_5(self):
        if self.idx >= len(self.input):
            return self.match(15)
        return self.match(15)

    def state_6(self):
        if self.idx >= len(self.input):
            return self.match(16)
        return self.match(16)

    def state_7(self):
        if self.idx >= len(self.input):
            return self.match(17)
        return self.match(17)

    def state_8(self):
        if self.idx >= len(self.input):
            return self.match(18)
        return self.match(18)

    def state_9(self):
        if self.idx >= len(self.input):
            return self.match(20)
        return self.match(20)

    def state_10(self):
        if self.idx >= len(self.input):
            return self.match(21)
        return self.match(21)

    def state_11(self):
        if self.idx >= len(self.input):
            self.eosError(11)
            return
        if   ord(self.input[self.idx]) == 38:
            return self.mvto(self.state_12)
        self.error(11, [38])

    def state_12(self):
        if self.idx >= len(self.input):
            return self.match(22)
        return self.match(22)

    def state_13(self):
        if self.idx >= len(self.input):
            self.eosError(13)
            return
        if   ord(self.input[self.idx]) == 124:
            return self.mvto(self.state_14)
        self.error(13, [124])

    def state_14(self):
        if self.idx >= len(self.input):
            return self.match(23)
        return self.match(23)

    def state_15(self):
        if self.idx >= len(self.input):
            return self.match(24)
        return self.match(24)

    def state_16(self):
        if self.idx >= len(self.input):
            return self.match(25)
        return self.match(25)

    def state_17(self):
        if self.idx >= len(self.input):
            return self.match(28)
        return self.match(28)

    def state_18(self):
        if self.idx >= len(self.input):
            return self.match(29)
        return self.match(29)

    def state_19(self):
        if self.idx >= len(self.input):
            self.eosError(19)
            return
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_30)
        self.error(19, [48, 49, 50, 51, 52, 53, 54, 55, 56, 57])

    def state_20(self):
        if self.idx >= len(self.input):
            self.eosError(20)
            return
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_27)
        self.error(20, [48, 49, 50, 51, 52, 53, 54, 55, 56, 57])

    def state_21(self):
        if self.idx >= len(self.input):
            return self.match(35)
        return self.match(35)

    def state_22(self):
        if self.idx >= len(self.input):
            return self.match(36)
        return self.match(36)

    def state_23(self):
        if self.idx >= len(self.input):
            return self.match(14)
        if   ord(self.input[self.idx]) == 61:
            return self.mvto(self.state_15)
        return self.match(14)

    def state_24(self):
        if self.idx >= len(self.input):
            return self.match(19)
        if   ord(self.input[self.idx]) == 61:
            return self.mvto(self.state_16)
        return self.match(19)

    def state_25(self):
        if self.idx >= len(self.input):
            return self.match(26)
        if   ord(self.input[self.idx]) == 61:
            return self.mvto(self.state_17)
        return self.match(26)

    def state_26(self):
        if self.idx >= len(self.input):
            return self.match(27)
        if   ord(self.input[self.idx]) == 61:
            return self.mvto(self.state_18)
        return self.match(27)

    def state_27(self):
        if self.idx >= len(self.input):
            return self.match(34)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_27)
        return self.match(34)

    def state_28(self):
        if self.idx >= len(self.input):
            return self.match(12)
        if   ord(self.input[self.idx]) == 42:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 47:
            return self.mvto(self.state_33)
        return self.match(12)

    def state_29(self):
        if self.idx >= len(self.input):
            self.eosError(29)
            return
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_32)
        self.error(29, [48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 65, 66, 67, 68, 69, 70, 97, 98, 99, 100, 101, 102])

    def state_30(self):
        if self.idx >= len(self.input):
            return self.match(34)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_30)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_31)
        return self.match(34)

    def state_31(self):
        if self.idx >= len(self.input):
            self.eosError(31)
            return
        if   ord(self.input[self.idx]) == 43:
            return self.mvto(self.state_20)
        elif ord(self.input[self.idx]) == 45:
            return self.mvto(self.state_20)
        elif ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_27)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_27)
        self.error(31, [43, 45, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57])

    def state_32(self):
        if self.idx >= len(self.input):
            return self.match(32)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_32)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_32)
        return self.match(32)

    def state_33(self):
        if self.idx >= len(self.input):
            return self.match(35)
        if   ord(self.input[self.idx]) == 0:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 1:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 2:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 3:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 4:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 5:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 6:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 7:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 8:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 9:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 10:
            return self.mvto(self.state_21)
        elif ord(self.input[self.idx]) == 11:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 12:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 13:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 14:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 15:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 16:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 17:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 18:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 19:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 20:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 21:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 22:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 23:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 24:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 25:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 26:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 27:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 28:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 29:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 30:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 31:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 32:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 33:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 34:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 35:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 36:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 37:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 38:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 39:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 40:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 41:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 42:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 43:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 44:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 45:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 46:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 47:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 58:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 59:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 60:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 61:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 62:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 63:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 64:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 91:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 92:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 93:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 94:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 96:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 123:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 124:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 125:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 126:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 127:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 128:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 129:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 130:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 131:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 132:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 133:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 134:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 135:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 136:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 137:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 138:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 139:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 140:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 141:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 142:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 143:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 144:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 145:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 146:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 147:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 148:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 149:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 150:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 151:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 152:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 153:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 154:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 155:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 156:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 157:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 158:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 159:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 160:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 161:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 162:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 163:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 164:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 165:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 166:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 167:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 168:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 169:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 170:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 171:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 172:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 173:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 174:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 175:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 176:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 177:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 178:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 179:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 180:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 181:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 182:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 183:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 184:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 185:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 186:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 187:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 188:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 189:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 190:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 191:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 192:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 193:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 194:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 195:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 196:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 197:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 198:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 199:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 200:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 201:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 202:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 203:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 204:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 205:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 206:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 207:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 208:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 209:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 210:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 211:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 212:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 213:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 214:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 215:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 216:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 217:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 218:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 219:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 220:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 221:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 222:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 223:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 224:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 225:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 226:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 227:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 228:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 229:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 230:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 231:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 232:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 233:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 234:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 235:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 236:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 237:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 238:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 239:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 240:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 241:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 242:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 243:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 244:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 245:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 246:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 247:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 248:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 249:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 250:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 251:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 252:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 253:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 254:
            return self.mvto(self.state_33)
        elif ord(self.input[self.idx]) == 255:
            return self.mvto(self.state_33)
        return self.match(35)

    def state_34(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_35(self):
        if self.idx >= len(self.input):
            return self.match(37)
        if   ord(self.input[self.idx]) == 9:
            return self.mvto(self.state_35)
        elif ord(self.input[self.idx]) == 10:
            return self.mvto(self.state_35)
        elif ord(self.input[self.idx]) == 13:
            return self.mvto(self.state_35)
        elif ord(self.input[self.idx]) == 32:
            return self.mvto(self.state_35)
        return self.match(37)

    def state_36(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_37)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_37(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_38)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_38(self):
        if self.idx >= len(self.input):
            return self.match(0)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(0)

    def state_39(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_40)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_40(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_41)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_41(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_42)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_42(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_43)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_43(self):
        if self.idx >= len(self.input):
            return self.match(1)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(1)

    def state_44(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_45)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_45(self):
        if self.idx >= len(self.input):
            return self.match(2)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(2)

    def state_46(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_47)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_47(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_48)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_48(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_49)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_49(self):
        if self.idx >= len(self.input):
            return self.match(3)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(3)

    def state_50(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_51)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_51(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_52)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_52(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_53)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_53(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_54)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_54(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_55)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_55(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_56)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_56(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_57)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_57(self):
        if self.idx >= len(self.input):
            return self.match(4)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(4)

    def state_58(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_59)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_59(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_60)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_60(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_61)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_61(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_62)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_62(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_63)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_63(self):
        if self.idx >= len(self.input):
            return self.match(5)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(5)

    def state_64(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_65)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_65(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_66)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_66(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_67)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_67(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_68)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_68(self):
        if self.idx >= len(self.input):
            return self.match(6)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(6)

    def state_69(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_70)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_70(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_71)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_71(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_72)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_72(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_73)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_73(self):
        if self.idx >= len(self.input):
            return self.match(7)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(7)

    def state_74(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_75)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_75(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_76)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_76(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_77)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_77(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_78)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_78(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_79)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_79(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_80)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_80(self):
        if self.idx >= len(self.input):
            return self.match(30)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_81)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(30)

    def state_81(self):
        if self.idx >= len(self.input):
            return self.match(8)
        if   ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        return self.match(8)

    def state_82(self):
        if self.idx >= len(self.input):
            self.eosError(82)
            return
        if   ord(self.input[self.idx]) == 0:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 1:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 2:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 3:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 4:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 5:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 6:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 7:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 8:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 9:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 10:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 11:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 12:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 13:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 14:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 15:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 16:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 17:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 18:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 19:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 20:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 21:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 22:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 23:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 24:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 25:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 26:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 27:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 28:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 29:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 30:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 31:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 32:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 33:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 34:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 35:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 36:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 37:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 38:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 39:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 40:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 41:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 42:
            return self.mvto(self.state_84)
        elif ord(self.input[self.idx]) == 43:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 44:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 45:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 46:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 47:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 58:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 59:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 60:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 61:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 62:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 63:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 64:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 91:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 92:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 93:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 94:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 96:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 123:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 124:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 125:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 126:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 127:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 128:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 129:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 130:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 131:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 132:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 133:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 134:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 135:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 136:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 137:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 138:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 139:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 140:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 141:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 142:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 143:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 144:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 145:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 146:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 147:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 148:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 149:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 150:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 151:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 152:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 153:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 154:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 155:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 156:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 157:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 158:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 159:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 160:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 161:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 162:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 163:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 164:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 165:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 166:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 167:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 168:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 169:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 170:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 171:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 172:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 173:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 174:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 175:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 176:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 177:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 178:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 179:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 180:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 181:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 182:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 183:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 184:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 185:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 186:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 187:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 188:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 189:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 190:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 191:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 192:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 193:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 194:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 195:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 196:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 197:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 198:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 199:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 200:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 201:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 202:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 203:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 204:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 205:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 206:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 207:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 208:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 209:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 210:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 211:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 212:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 213:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 214:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 215:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 216:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 217:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 218:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 219:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 220:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 221:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 222:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 223:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 224:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 225:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 226:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 227:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 228:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 229:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 230:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 231:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 232:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 233:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 234:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 235:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 236:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 237:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 238:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 239:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 240:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 241:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 242:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 243:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 244:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 245:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 246:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 247:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 248:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 249:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 250:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 251:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 252:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 253:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 254:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 255:
            return self.mvto(self.state_82)
        self.error(82, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255])

    def state_83(self):
        if self.idx >= len(self.input):
            return self.match(33)
        if   ord(self.input[self.idx]) == 46:
            return self.mvto(self.state_19)
        elif ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_31)
        return self.match(33)

    def state_84(self):
        if self.idx >= len(self.input):
            self.eosError(84)
            return
        if   ord(self.input[self.idx]) == 0:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 1:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 2:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 3:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 4:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 5:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 6:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 7:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 8:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 9:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 10:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 11:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 12:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 13:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 14:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 15:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 16:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 17:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 18:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 19:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 20:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 21:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 22:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 23:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 24:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 25:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 26:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 27:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 28:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 29:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 30:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 31:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 32:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 33:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 34:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 35:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 36:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 37:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 38:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 39:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 40:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 41:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 42:
            return self.mvto(self.state_84)
        elif ord(self.input[self.idx]) == 43:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 44:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 45:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 46:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 47:
            return self.mvto(self.state_22)
        elif ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 58:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 59:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 60:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 61:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 62:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 63:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 64:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 91:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 92:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 93:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 94:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 95:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 96:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 123:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 124:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 125:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 126:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 127:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 128:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 129:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 130:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 131:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 132:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 133:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 134:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 135:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 136:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 137:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 138:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 139:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 140:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 141:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 142:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 143:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 144:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 145:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 146:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 147:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 148:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 149:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 150:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 151:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 152:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 153:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 154:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 155:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 156:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 157:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 158:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 159:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 160:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 161:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 162:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 163:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 164:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 165:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 166:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 167:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 168:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 169:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 170:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 171:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 172:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 173:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 174:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 175:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 176:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 177:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 178:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 179:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 180:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 181:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 182:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 183:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 184:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 185:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 186:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 187:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 188:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 189:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 190:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 191:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 192:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 193:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 194:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 195:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 196:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 197:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 198:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 199:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 200:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 201:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 202:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 203:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 204:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 205:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 206:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 207:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 208:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 209:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 210:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 211:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 212:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 213:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 214:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 215:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 216:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 217:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 218:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 219:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 220:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 221:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 222:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 223:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 224:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 225:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 226:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 227:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 228:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 229:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 230:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 231:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 232:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 233:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 234:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 235:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 236:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 237:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 238:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 239:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 240:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 241:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 242:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 243:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 244:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 245:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 246:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 247:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 248:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 249:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 250:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 251:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 252:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 253:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 254:
            return self.mvto(self.state_82)
        elif ord(self.input[self.idx]) == 255:
            return self.mvto(self.state_82)
        self.error(84, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255])

    def state_85(self):
        if self.idx >= len(self.input):
            return self.match(31)
        if   ord(self.input[self.idx]) == 46:
            return self.mvto(self.state_19)
        elif ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_31)
        return self.match(31)

    def state_86(self):
        if self.idx >= len(self.input):
            return self.match(33)
        if   ord(self.input[self.idx]) == 46:
            return self.mvto(self.state_19)
        elif ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_85)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_31)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_29)
        return self.match(33)

    def state_87(self):
        if self.idx >= len(self.input):
            self.eosError(87)
            return
        if   ord(self.input[self.idx]) == 9:
            return self.mvto(self.state_35)
        elif ord(self.input[self.idx]) == 10:
            return self.mvto(self.state_35)
        elif ord(self.input[self.idx]) == 13:
            return self.mvto(self.state_35)
        elif ord(self.input[self.idx]) == 32:
            return self.mvto(self.state_35)
        elif ord(self.input[self.idx]) == 33:
            return self.mvto(self.state_24)
        elif ord(self.input[self.idx]) == 37:
            return self.mvto(self.state_4)
        elif ord(self.input[self.idx]) == 38:
            return self.mvto(self.state_11)
        elif ord(self.input[self.idx]) == 40:
            return self.mvto(self.state_5)
        elif ord(self.input[self.idx]) == 41:
            return self.mvto(self.state_6)
        elif ord(self.input[self.idx]) == 42:
            return self.mvto(self.state_3)
        elif ord(self.input[self.idx]) == 43:
            return self.mvto(self.state_1)
        elif ord(self.input[self.idx]) == 44:
            return self.mvto(self.state_10)
        elif ord(self.input[self.idx]) == 45:
            return self.mvto(self.state_2)
        elif ord(self.input[self.idx]) == 46:
            return self.mvto(self.state_19)
        elif ord(self.input[self.idx]) == 47:
            return self.mvto(self.state_28)
        elif ord(self.input[self.idx]) == 48:
            return self.mvto(self.state_86)
        elif ord(self.input[self.idx]) == 49:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 50:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 51:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 52:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 53:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 54:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 55:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 56:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 57:
            return self.mvto(self.state_83)
        elif ord(self.input[self.idx]) == 58:
            return self.mvto(self.state_9)
        elif ord(self.input[self.idx]) == 60:
            return self.mvto(self.state_25)
        elif ord(self.input[self.idx]) == 61:
            return self.mvto(self.state_23)
        elif ord(self.input[self.idx]) == 62:
            return self.mvto(self.state_26)
        elif ord(self.input[self.idx]) == 65:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 66:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 67:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 68:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 69:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 70:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 71:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 72:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 73:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 74:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 75:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 76:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 77:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 78:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 79:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 80:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 81:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 82:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 83:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 84:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 85:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 86:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 87:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 88:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 89:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 90:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 97:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 98:
            return self.mvto(self.state_69)
        elif ord(self.input[self.idx]) == 99:
            return self.mvto(self.state_74)
        elif ord(self.input[self.idx]) == 100:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 101:
            return self.mvto(self.state_46)
        elif ord(self.input[self.idx]) == 102:
            return self.mvto(self.state_50)
        elif ord(self.input[self.idx]) == 103:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 104:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 105:
            return self.mvto(self.state_44)
        elif ord(self.input[self.idx]) == 106:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 107:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 108:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 109:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 110:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 111:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 112:
            return self.mvto(self.state_39)
        elif ord(self.input[self.idx]) == 113:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 114:
            return self.mvto(self.state_58)
        elif ord(self.input[self.idx]) == 115:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 116:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 117:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 118:
            return self.mvto(self.state_36)
        elif ord(self.input[self.idx]) == 119:
            return self.mvto(self.state_64)
        elif ord(self.input[self.idx]) == 120:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 121:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 122:
            return self.mvto(self.state_34)
        elif ord(self.input[self.idx]) == 123:
            return self.mvto(self.state_7)
        elif ord(self.input[self.idx]) == 124:
            return self.mvto(self.state_13)
        elif ord(self.input[self.idx]) == 125:
            return self.mvto(self.state_8)
        self.error(87, [9, 10, 13, 32, 33, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 60, 61, 62, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125])
