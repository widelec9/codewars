import re
from math import factorial


def expand(expr):
    tokens = re.search(r'^\((\-?\d*([a-z]))([\+\-]\d*)\)\^(\d*)$', expr)
    a = int(tokens.group(1)[:-1]) if tokens.group(1)[:-1] not in ['', '-'] else int(tokens.group(1)[:-1] + '1')
    varname = tokens.group(2)
    b = int(tokens.group(3).strip('+'))
    n = int(tokens.group(4))
    if n == 0:
        return '1'
    else:
        coeffs = [str(int(factorial(n) / (factorial(n-i) * factorial(i)) * a**(n-i) * b**i)) for i in range(n+1)]
        out = '+'.join([val + varname + '^' + str(len(coeffs)-1-i) for i, val in enumerate(coeffs)]).replace('+-', '-').replace('^1', '')
        out = re.sub(r'^(.*)[a-z]\^0', r'\1', re.sub(r'^([\+\-])?1([a-z].*)', r'\1\2', out))
    return out