import numpy as np


def validSolution(board):
    board = np.array(board)
    for i in range(0, len(board)):
        if len(list(np.unique(board[i, :], return_counts=True)[1])) != 9 or len(list(np.unique(board[:, i], return_counts=True)[1])) != 9:
            return False
    for s in [[a[i * 3:(i + 1) * 3] for a in board[j * 3:(j + 1) * 3]] for i in range(0, 3) for j in range(0, 3)]:
        s = [item for sub in s for item in sub]
        for d in range(1, 10):
            if s.count(d) > 1:
                return False
    return True
