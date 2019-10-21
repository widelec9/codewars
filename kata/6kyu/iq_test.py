def iq_test(numbers):
    nums = ['e' if int(n) % 2 == 0 else 'o' for n in numbers.split(' ')]
    return nums.index('e') + 1 if nums.count('e') < nums.count('o') else nums.index('o') + 1
