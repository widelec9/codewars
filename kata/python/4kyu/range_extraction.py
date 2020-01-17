import numpy as np


def solution(args):
    diffs = np.array([args[i + 1] - args[i] for i in range(0, len(args) - 1)])
    out = []
    i = 0
    while i < len(args):
        if np.any(np.array(np.where(diffs == 1)) == i):
            try:
                stop = int(np.nonzero(diffs[i:] - 1)[0][0] + i)
            except IndexError:
                stop = len(args) - 1
            if stop - i > 1:
                out.append('{}-{}'.format(str(args[i]), str(args[stop])))
                i = stop + 1
                continue
        out.append(str(args[i]))
        i += 1
    return ','.join(out)
