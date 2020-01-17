def find_ball(scales):
    w1 = scales.get_weight([0, 1, 2], [3, 4, 5])
    if not w1:
        return 6 if scales.get_weight([6], [7]) < 0 else 7
    else:
        if w1 < 0:
            w2 = scales.get_weight([0], [1])
            return 2 if not w2 else 0 if w2 < 0 else 1
        else:
            w2 = scales.get_weight([3], [4])
            return 5 if not w2 else 3 if w2 < 0 else 4
