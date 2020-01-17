import re
from operator import add, sub, mul, truediv


class Calculator(object):
    def __init__(self):
        self.op_dict = {'+': add, '-': sub, '*': mul, '/': truediv}
        self.regex_general = r'(\-*\d*\.?\d*(e?[\+\-]?\d{2,3})?)'
        self.regex_single = r'(\-*\d*\.?\d*e?[\+\-]?\d{2,3})'

    def eval_brackets(self, string):
        while True:
            op = re.search(r'\(([^()]+)\)', string)
            if op is None: break
            string = string.replace(op.group(0), str(self.evaluate(op.group(1), cont=1)))
        return string

    def ev(self, string, ops):
        string = self.strip_neg_sign(string)
        while True:
            op = re.search(self.regex_general + r'\s?([' + ops + r'])\s?' + self.regex_general, string)
            if op is None or op.group(1) == '' or (re.search(self.regex_single, op.group(0)) is not None and re.search(self.regex_single, op.group(0)) == re.search(self.regex_single, op.group(1))): break
            string = string.replace(str(op.group()), str(self.op_dict[op.group(3)](float(self.strip_neg_sign(op.group(1))), float(self.strip_neg_sign(op.group(4))))))
        return string

    def strip_neg_sign(self, string):
        search = re.search(r'^(\-*)(\d*\.?\d*)$', string)
        if search is not None:
            string = string.strip('-') if len(search.group(1)) % 2 == 0 else '-' + string.strip('-')
        return string

    def evaluate(self, string, cont=0):
        if string == '':
            return string
        else:
            if not cont:
                string = self.eval_brackets(string)
            string = self.ev(string, '\*\/')
            string = self.ev(string, '\+\-')
            return float(re.sub(r'(^e[\+\-]?\d*$)', r'1\1', string))


def calc(string):
    return Calculator().evaluate(string)