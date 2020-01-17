def unique_in_order(iterable):
    rl = []
    j = None
    for i in iterable:
        if i != j:
            rl += [i]
        j = i
    return rl