import numpy as np


def matrix_mult(a, b):
    return list(map(list, np.matmul(np.array(a), np.array(b))))
