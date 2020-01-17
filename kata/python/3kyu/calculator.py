import re
from operator import add, sub, mul, truediv


class Calculator(object):
    def eval_brackets(self, string):
        while True:
            op = re.search(r'\(([^()]+)\)', string)
            if op is None: break
            string = string.replace(op.group(0), str(self.evaluate(op.group(1), cont=1)))
        return string

    def ev(self, string, ops):
        op_dict = {'+': add, '-': sub, '*': mul, '/': truediv}
        while True:
            op = re.search(r'(\-?\d*\.?\d*)\s([' + ops + '])\s(\-?\d*\.?\d*)', string)
            if op is None: break
            string = string.replace(str(op.group()), str(op_dict[op.group(2)](float(op.group(1)), float(op.group(3)))))
        return string

    def evaluate(self, string, cont=0):
        if not cont:
            string = self.eval_brackets(string)
        string = self.ev(string, '\*\/')
        string = self.ev(string, '\+\-')
        return float(string)