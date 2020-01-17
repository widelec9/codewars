def separate_liquids(glass):
    if not glass:
        return []
    order = [e for e in ['O', 'A', 'W', 'H'] if e in set(sum(glass, []))]
    cnt = {k: sum(glass, []).count(k) for k in order}
    h, w = len(glass), len(glass[0])
    glass = [['' for y in range(w)] for x in range(h)]
    row = 0
    while row < h:
        n_empty = glass[row].count('')
        for k in order:
            if n_empty and cnt[k]:
                n = min(n_empty, cnt[k])
                glass[row] = glass[row][:w-n_empty] + [k]*n + glass[row][n+w-n_empty:]
                cnt[k], n_empty = cnt[k] - n, n_empty - n
                if not n_empty:
                    row += 1
                    break
    return glass
