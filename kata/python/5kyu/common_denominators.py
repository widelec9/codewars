def gcd(x, y):
    while y:
        x, y = y, x % y
    return x


def lcm(x, y):
    return (x * y) // gcd(x, y)


def convertFracts(lst):
    if not lst:
        return []
    den = [x[1] for x in lst]
    while len(den) > 1:
        den[0] = lcm(den[0], den[1])
        den.pop(1)
    return [[l[0] * (den[0] // l[1]), l[1] * (den[0] // l[1])] for l in lst]
