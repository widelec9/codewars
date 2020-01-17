import numpy as np


def tv_remote(word):
    kb = np.array([['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
                   ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/']])
    curr_pos = (0, 0)
    total_dist = 0
    for c in word:
        new_pos = (np.where(kb == c)[0][0], np.where(kb == c)[1][0])
        total_dist += abs(new_pos[0] - curr_pos[0]) + abs(new_pos[1] - curr_pos[1]) + 1
        curr_pos = new_pos
    return total_dist