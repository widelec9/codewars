def max_sumDig(nMax, maxs):
    n = 0
    data = []
    s = 0
    for i in range(1000, nMax + 1):
        if cons_sum_below_max(i, maxs):
            n += 1
            data += [i]
            s += i
    diffs = [abs(d - (s / (n * 1.0))) for d in data]
    return [n, data[diffs.index(min(diffs))], s]


def cons_sum_below_max(n, maxs):
    if n <= 9999:
        return sum(map(int, str(n))) <= maxs
    else:
        for i in range(0, len(str(n)) - 4 + 1):
            if sum(map(int, str(n)[i:i+4])) > maxs:
                return False
        return True