def next_smaller(n):
    nlst = [int(n) for n in str(n)]
    for i in range(len(nlst) - 1, 0, -1):
        if nlst[i-1] > nlst[i]:
            pivot_loc = i - 1
            pivot = nlst[pivot_loc]
            lt_side, rt_side = nlst[:pivot_loc+1], nlst[pivot_loc+1:]
            for r in sorted(rt_side, reverse=True):
                if r < pivot:
                    subst_loc = rt_side.index(r)
                    lt_side[pivot_loc], rt_side[subst_loc] = r, pivot
                    ret = ''.join(map(str, lt_side + sorted(rt_side, reverse=True)))
                    if ret[0] == '0':
                        return -1
                    return int(ret)
    return -1
