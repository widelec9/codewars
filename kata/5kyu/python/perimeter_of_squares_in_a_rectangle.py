def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def perimeter(n):
    return 4 * sum(list(fib(n+2))[1:])
