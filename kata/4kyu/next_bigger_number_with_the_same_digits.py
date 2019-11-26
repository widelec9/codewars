def next_bigger(n):
    nlst = [int(n) for n in str(n)]
    pivot_loc = -1
    for i in range(len(nlst) - 1, 0, -1):
        if nlst[i-1] < nlst[i]:
            pivot_loc = i - 1
            pivot = nlst[pivot_loc]
            break
    if pivot_loc == -1:
        return pivot_loc
    lt_side, rt_side = nlst[:pivot_loc+1], nlst[pivot_loc+1:]
    for r in sorted(rt_side):
        if r > pivot:
            break
    subst = r
    subst_loc = rt_side.index(subst)
    lt_side[pivot_loc], rt_side[subst_loc] = subst, pivot
    return int(''.join(map(str, lt_side + sorted(rt_side))))
