def productFib(prod):
    f = [0, 1]
    while f[-2] * f[-1] < prod:
        f += [f[-2] + f[-1]]
    return [f[-2], f[-1], f[-2] * f[-1] == prod]
