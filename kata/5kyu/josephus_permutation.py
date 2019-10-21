def josephus(items, k):
    res_list = []
    items = [None] + items
    i = 0
    while len(items) > 1:
        if i == 0:
            i += k
        else:
            if len(items) == 2:
                i = 1
            elif i + k > len(items):
                i += k - len(items)
            else:
                i += k - 1

        while i >= len(items):
            i -= (len(items) - 1)

        res_list += [items.pop(i)]
    return res_list