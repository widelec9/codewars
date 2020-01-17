import numpy as np


def get_ngbrs(f, pt):
    return np.reshape([f[pt[0] + i][pt[1] + j] if 0 <= pt[0] + i < 10 and 0 <= pt[1] + j < 10 and (pt[0] + i, pt[1] + j) != pt 
                       else '' 
                       for i in range(-1, 2) for j in range(-1, 2)], (3, 3))


def validate_battlefield(field):
    ships = {'4': 1, '3': 2, '2': 3, '1': 4}
    field = np.array(field)
    ones = list(zip(np.where(field == 1)[0], np.where(field == 1)[1]))
    if len(ones) != 20:
        return False

    while len(ones):
        pt = ones[0]
        ngbrs = get_ngbrs(field, pt)
        ngbr_ones = np.count_nonzero(ngbrs == '1')
        if ngbr_ones > 1:
            return False
        elif ngbr_ones == 0:
            ships['1'] -= 1
            ones.pop(0)
        else:
            length = 1
            while True:
                length += 1
                if length == 2:
                    one = (np.where(ngbrs == '1')[0][0], np.where(ngbrs == '1')[1][0])
                    detected_dir = (one[0] - 1, one[1] - 1)
                newpt = (pt[0] + detected_dir[0], pt[1] + detected_dir[1])
                newngbrs = get_ngbrs(field, newpt)
                if np.count_nonzero(newngbrs == '1') > 2 or length > 4:
                    return False
                elif np.count_nonzero(newngbrs == '1') == 2:
                    if field[newpt[0] + detected_dir[0]][newpt[1] + detected_dir[1]] == 0:
                        return False
                    ones.pop(ones.index(pt))
                    pt = newpt
                    ngbrs = newngbrs
                else: 
                    ships[str(length)] -= 1
                    ones.pop(ones.index(pt))
                    ones.pop(ones.index(newpt))
                    break
    return list(ships.values()) == 4 * [0]