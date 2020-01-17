import numpy as np


def spiralize(size):
    array = np.array([[0 for i in range(size)] for j in range(size)])
    rowlen = size
    row = size - rowlen
    shift, turn = 0, 0
    while True:
        for i in range(4):
            if rowlen == size:
                if i == 3:
                    rowlen -= 2
                array[row] = [1] * rowlen + list(array[row][rowlen:])
            else:
                if i == 0:
                    if rowlen != size - 2:
                        shift += 2
                    array[row] = list(array[row][:shift]) + [1] * rowlen + list(array[row][rowlen+shift:])
                    rowlen -= 2
                else:
                    if i == 3:
                        rowlen -= 2
                    array[row] = list(array[row][:row]) + [1] * rowlen + list(array[row][row+rowlen:])
            if rowlen < 4 and (array[row+1][row+rowlen-2] == 1 or array[row+2][row+rowlen-1] == 1):
                return np.rot90(array, k=4-turn).tolist()
            array = np.rot90(array)
            turn = (turn + 1) % 4
        row += 2