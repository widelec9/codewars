def iq_test(numbers):
    evenness = [int(n) % 2 for n in numbers.split(' ')]
    return evenness.index(1) + 1 if evenness.count(0) > 1 else evenness.index(0) + 1
