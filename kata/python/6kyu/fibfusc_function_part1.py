def cache(f):
    fibfusc_cache = {}

    def wrapper(n):
        if n not in fibfusc_cache:
            fibfusc_cache[n] = f(n)
        return fibfusc_cache[n]
    return wrapper


@cache
def fibfusc(n):
    if n in [0, 1]:
        return [(1, 0), (0, 1)][n]
    elif n % 2:
        x, y = fibfusc(int((n - 1) / 2))
        return -1*y * (2*x + 3*y), (x + 2*y) * (x + 4*y)
    else:
        x, y = fibfusc(int(n / 2))
        return (x + y) * (x - y), y * (2*x + 3*y)
