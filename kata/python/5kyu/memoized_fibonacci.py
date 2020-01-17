def cache(f):
    fib_cache = {}

    def wrapper(n):
        if n not in fib_cache:
            fib_cache[n] = f(n)
        return fib_cache[n]
    return wrapper


@cache
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
