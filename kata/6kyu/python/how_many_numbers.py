def sel_number(n, d):
    return sum([1 for i in range(10, n + 1) if is_increasing_order_maxdiff(i, d)])


def is_increasing_order_maxdiff(x, d):
    x = [int(dig) for dig in str(x)]
    for i in range(0, len(x) - 1):
        if x[i+1] - x[i] <= 0 or x[i+1] - x[i] > d:
            return False
    return True