def div_gen(n):
    divs = []
    for i in range(1, int(n**0.5 + 1)):
        if not n % i:
            yield i
            if i*i != n:
                divs.append(n / i)
    for d in divs[::-1]:
        yield int(d)


def list_squared(m, n):
    out = []
    for i in range(m, n+1):
        divs = list(div_gen(i))
        div_sq_sum = sum([d**2 for d in divs])
        if (div_sq_sum**0.5).is_integer():
            out += [[i, div_sq_sum]]
    return out
