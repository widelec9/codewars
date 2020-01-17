from itertools import combinations

keypad = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']


def check1800(s):
    NUMS = [[[i for i, k in enumerate(keypad) if c in k][0] for c in W] for W in WORDS]
    nums = [[i for i, k in enumerate(keypad) if c in k][0] for w in s.split('-')[2:] for c in w]
    return {'1-800-{}-{}'.format(pair[0], pair[1]) for c in [list(combinations(nw, 2)) for nw in [
        [WORDS[i] for l in comb for i, x in enumerate(NUMS) if x == l] for comb in
        [[nums[:3], nums[3:]], [nums[:4], nums[4:]]]]] for pair in c if len(pair[0]) + len(pair[1]) == 7}
