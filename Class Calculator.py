class Calculator:
    last = None
    def __init__(self):
        self.result = 0
        self.histlist = []
    def sum(self, a, b):
        self.result = a + b
        self.histlist.append("sum({}, {}) == {}".format(a, b, round(self.result, 1)))
        Calculator.last = ("sum({}, {}) == {}".format(a, b, round(self.result, 1)))
        return self.result
    def sub(self, a, b):
        self.result = a - b
        self.histlist.append("sub({}, {}) == {}".format(a, b, round(self.result, 1)))
        Calculator.last = ("sub({}, {}) == {}".format(a, b, round(self.result, 1)))
        return self.result
    def mul(self, a, b):
        self.result = a * b
        self.histlist.append("mul({}, {}) == {}".format(a, b, round(self.result, 1)))
        Calculator.last = ("mul({}, {}) == {}".format(a, b, round(self.result, 1)))
        return self.result
    def div(self, a, b, mod=False):
        if mod:
            self.result = a % b
        else:
            self.result = a / b
        self.histlist.append("div({}, {}) == {}".format(a, b, round(self.result, 1)))
        Calculator.last = ("div({}, {}) == {}".format(a, b, round( self.result, 1)))
        return self.result
    def history(self, n):
        if n <= len(self.histlist):
            return self.histlist[-n]
        else:
            return None

    @classmethod
    def clear(cls):
        Calculator.last = None
#a = Calculator()
#print(a.mul(20, 10))
#print(a.history(1))
#print(a.last)
#Calculator.clear()
