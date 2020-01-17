import re


def differentiate(equation, point):
    equation = re.sub(r'([\+\-])', r' \1', equation).lstrip().split(' ')
    res = 0
    for term in equation:
        term = re.sub(r'(^|[\+\-])x', r'\g<1>1x', term)
        powsplit = term.split('^')
        if len(powsplit) > 1:
            term = int(powsplit[0].rstrip('x'))
            pow = int(powsplit[1])
            res += term * pow * point ** (pow - 1)
        else:
            if 'x' in term:
                res += int(term.rstrip('x'))
    return res