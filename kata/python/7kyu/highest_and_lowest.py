def high_and_low(numbers):
    numlist = sorted(numbers.split(' '), key=lambda w: int(w))
    return '{} {}'.format(numlist[-1], numlist[0])