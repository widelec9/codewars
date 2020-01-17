def isSolved(board):
    bt = board + list(zip(*board))
    for rc in bt:
        if len(set(rc)) == 1 and rc[0]:
            return rc[0]
    if board[1][1] and ((board[0][0] == board[1][1] == board[2][2]) or (board[0][2] == board[1][1] == board[2][0])):
        return board[1][1]
    for rc in bt:
        if 0 in rc:
            return -1
    return 0
