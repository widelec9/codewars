import numpy as np

kb = np.array([['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
                   ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/'], ['aA', ' ', '', '', '', '', '', '']])


def tv_remote(word):
    curr_pos = (0, 0)
    total_dist = 0
    curr_upper_mode = False
    for c in word:
        if c.isalnum() and not c.isdigit() and c.isupper() != curr_upper_mode:
            total_dist, curr_pos, curr_upper_mode = get_dist_new_pos(curr_pos, 'aA', total_dist, curr_upper_mode)
        total_dist, curr_pos, curr_upper_mode = get_dist_new_pos(curr_pos, c.lower(), total_dist, curr_upper_mode)
    return total_dist


def get_dist_new_pos(curr_pos, new_c, curr_dist, curr_upper_mode):
    if new_c == 'aA':
        curr_upper_mode ^= True
    new_pos = (np.where(kb == new_c)[0][0], np.where(kb == new_c)[1][0])
    curr_dist += abs(new_pos[0] - curr_pos[0]) + abs(new_pos[1] - curr_pos[1]) + 1
    return curr_dist, new_pos, curr_upper_mode