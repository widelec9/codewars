from collections import Counter


def scramble(s1, s2):
    s1c = Counter(s1)
    s2c = Counter(s2)
    for ch in s2:
        if s2c[ch] > s1c[ch]:
            return False
    return True
