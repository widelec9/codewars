def beeramid(bonus, price):
    lvl = [0]
    while bonus >= (sum(lvl) + len(lvl)**2) * price:
        lvl += [len(lvl)**2]
    return len(lvl) - 1
