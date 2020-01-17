import numpy as np

kb = np.array([['a', 'b', 'c', 'd', 'e', '1', '2', '3'], ['f', 'g', 'h', 'i', 'j', '4', '5', '6'], ['k', 'l', 'm', 'n', 'o', '7', '8', '9'],
               ['p', 'q', 'r', 's', 't', '.', '@', '0'], ['u', 'v', 'w', 'x', 'y', 'z', '_', '/'], ['aA#', ' ', '', '', '', '', '', '']])

kb_sym = np.array([['^', '~', '?', '!', "'", '"', '(', ')'], ['-', ':', ';', '+', '&', '%', '*', '='], ['<', '>', '€', '£', '$', '¥', '¤', '\\'],
                   ['[', ']', '{', '}', ',', '.', '@', '§'], ['#', '¿', '¡', '', '', '', '_', '/'], ['aA#', ' ', '', '', '', '', '', '']])


def tv_remote(word):
    curr_pos = (0, 0)
    total_dist = 0
    curr_mode = 1
    for c in word:
        new_mode = 1 if c.islower() or (c in kb and not ((curr_mode == 2 and c in kb) or (curr_mode == 3 and c in kb_sym))) else 2 if c.isupper() or (curr_mode == 2 and c in kb) else 3
        if not c.isspace() and curr_mode != new_mode:
            total_dist, curr_pos, curr_mode = get_dist_new_pos(curr_pos, 'aA#', total_dist, curr_mode, new_mode)
        total_dist, curr_pos, curr_mode = get_dist_new_pos(curr_pos, c.lower(), total_dist, curr_mode, new_mode)
    return total_dist


def get_dist_new_pos(curr_pos, new_c, curr_dist, curr_mode, new_mode):
    keyb = kb_sym if curr_mode == 3 else kb
    new_pos = (np.where(keyb == new_c)[0][0], np.where(keyb == new_c)[1][0])
    curr_dist += min((keyb.shape[0] - abs(new_pos[0] - curr_pos[0])) % keyb.shape[0], abs(new_pos[0] - curr_pos[0])) + \
                 min((keyb.shape[1] - abs(new_pos[1] - curr_pos[1])) % keyb.shape[1], abs(new_pos[1] - curr_pos[1]))
    if new_c == 'aA#':
        while curr_mode != new_mode:
            curr_mode = (curr_mode % 3) + 1
            curr_dist += 1
    else:
        curr_dist += 1
    return curr_dist, new_pos, curr_mode