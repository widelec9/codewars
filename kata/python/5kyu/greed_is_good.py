def score(dice):
    pt = 0
    dc = {k: dice.count(k) for k in set(dice)}
    for k, v in dc.items():
        if v >= 3:
            if k == 1:
                pt += 1000 + (v - 3) * 100
            elif k == 5:
                pt += 500 + (v - 3) * 50
            else:
                pt += k * 100
        elif k == 1:
            pt += v * 100
        elif k == 5:
            pt += v * 50
    return pt
