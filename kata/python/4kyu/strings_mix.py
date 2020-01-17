from collections import Counter


def mix(s1, s2):
    c1 = Counter(''.join([s for s in s1 if s.isalpha() and s.islower()]))
    c1 = Counter({k: v for k, v in c1.items() if c1[k] > 1})
    c2 = Counter(''.join([s for s in s2 if s.isalpha() and s.islower()]))
    c2 = Counter({k: v for k, v in c2.items() if c2[k] > 1})
    gr_tuples = sorted([(c, '1', c1[c]) if c1[c] > c2[c] else (c, '=', c1[c]) if c1[c] == c2[c] else (c, '2', c2[c]) for c in set(list(c1.keys()) + list(c2.keys()))], key=lambda x: (-x[2], ord(x[1]), x[0]))
    return '/'.join([tup[1] + ':' + tup[2] * tup[0] for tup in gr_tuples])