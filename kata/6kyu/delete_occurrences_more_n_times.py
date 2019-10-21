def delete_nth(order, max_e):
    newlist = list()
    i = 0
    while i < len(order):
        while newlist.count(order[i]) < max_e and order.count(order[i]) > 0:
            newlist.append(order[i])
            order.pop(order.index(order[i]))
            if i >= len(order):
                break
        i += 1
    return newlist