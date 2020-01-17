def queue_time(customers, n):
    if not n:
        return 0
    qs = [0 for _ in range(n)]
    while customers:
        qs[qs.index(min(qs))] += customers.pop(0)
    return max(qs)
