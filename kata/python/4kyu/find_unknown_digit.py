import re
import operator


def to_eq(str_):
	splt = re.match(r'(\-?[\?\d]*)([+\-*])(\-?[\?\d]*)=(.*)', str_)
	return int(splt.group(1)), splt.group(2), int(splt.group(3)), int(splt.group(4))


def solve_runes(runes):
	ops = {'+': operator.add, '-': operator.sub, '*': operator.mul}
	for i in range(0, 10):
		newstr = re.sub(r'\?', str(i), runes)
		if str(i) not in runes and re.search(r'[+\-*=]00', newstr) is None:
			n1, op, n2, n3 = to_eq(newstr)
			if ops[op](n1, n2) == n3:
				return i
	return -1