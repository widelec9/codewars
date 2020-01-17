def gcd(a, b):
    if not b:
        return a
    return gcd(b, a % b)


def mixed_fraction(s):
    num, den = int(s.split('/')[0]), int(s.split('/')[1])
    if not den:
        raise ZeroDivisionError
    if not num:
        return '0'
    num_sign, den_sign = [-1, 1][num > 0], [-1, 1][den > 0]
    num, den = abs(num), abs(den)
    d, m = divmod(num, den)
    g = gcd(m, den)
    if g > 1:
        m, den = m // g, den // g
    if d and m:
        out = '{} {}/{}'.format(d, m, den)
    elif d and not m:
        out = str(d)
    else:
        out = '{}/{}'.format(m, den)
    if num_sign != den_sign:
        out = '-' + out
    return out
