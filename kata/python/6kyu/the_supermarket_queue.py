def queue_time(customers, n):
    qs = [0] * n
    while customers:
        qs[qs.index(min(qs))] += customers.pop(0)
    return max(qs)
