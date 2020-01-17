def binomial_mod3(n, k):
    out = 1
    while n > 0:
        n3 = n % 3
        k3 = k % 3
        if k3 > n3: return 0
        if k3 == 1 and n3 == 2:
            out *= 2
        n = n // 3
        k = k // 3
    return out


def triangle(row):
    colors = {'R': 0, 'G': 1, 'B': 2}
    n = len(row) - 1
    s = 0

    for k, color in enumerate(row):
        temp = colors[color]
        if temp != 0:
            s = (s + temp * binomial_mod3(n, k))

    if n % 2 == 1:
        s = -s

    return list(colors.keys())[s % 3]