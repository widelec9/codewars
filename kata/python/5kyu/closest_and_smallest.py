def closest(strng):
    if strng != '':
        idx_num_wt = sorted([[sum(map(int, [d for d in str(num)])), i, int(num)] for i, num in enumerate(strng.split())], key=lambda x: x[0])
        wt_diffs = [idx_num_wt[i+1][0] - idx_num_wt[i][0] for i, tup in enumerate(idx_num_wt[:-1])]
        dm = wt_diffs.index(min(wt_diffs))
        return [idx_num_wt[dm], idx_num_wt[dm+1]]
    else:
        return []