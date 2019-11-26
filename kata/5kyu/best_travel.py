from itertools import combinations


def choose_best_sum(t, k, ls):
    dists = [d for d in [sum(list(c)) for c in list(combinations(ls, k))] if d <= t]
    return sorted(dists)[-1] if dists else None
