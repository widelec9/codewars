import numpy as np


def determinant(matrix):
    matrix = np.array(matrix)
    if matrix.shape == (1, 1):
        return matrix[0][0]
    elif matrix.shape == (2, 2):
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        return sum([(-1) ** i * matrix[0][i] * determinant(np.delete(np.delete(matrix, 0, axis=0), i, axis=1)) for i in range(0, matrix.shape[1])])
