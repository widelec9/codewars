def ride_of_fortune(artifact, explorers):
    artifact = [list(row) for row in artifact]
    dim = (len(artifact), len(artifact[0]))
    dirs = {'W': (0, -1), 'E': (0, 1), 'N': (-1, 0), 'S': (1, 0)}
    sw_A = {'W': 'N', 'E': 'S', 'S': 'E', 'N': 'W'}
    sw_B = {'W': 'S', 'E': 'N', 'S': 'W', 'N': 'E'}
    exits = []
    while explorers:
        ex = explorers.pop(0)
        x, y = ex, 0
        d = 'E'
        while True:
            if 0 <= x < dim[0] and 0 <= y < dim[1] and artifact[x][y] != ' ':
                if artifact[x][y] == 'A':
                    d = sw_A[d]
                    artifact[x][y] = 'B'
                else:
                    d = sw_B[d]
                    artifact[x][y] = 'A'
            x, y = x + dirs[d][0], y + dirs[d][1]
            if y == -1:
                exits += [None]
                break
            elif x == -1:
                exits += [[0, y]]
                break
            elif x == dim[0]:
                exits += [[x - 1, y]]
                break
            elif y == dim[1]:
                exits += [[x, y - 1]]
                break
    return exits
