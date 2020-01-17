def path_finder(maze):
    maze = maze.split('\n')
    end = (len(maze)-1, len(maze)-1)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = [(0, 0)]
    visited = [(0, 0)]

    while True:
        (pr, pc) = queue.pop()

        for i in range(4):
            if (pr, pc) == end:
                return True

            rr = pr + dr[i]
            cc = pc + dc[i]

            if rr < 0 or rr > end[0] or cc < 0 or cc > end[1] or (rr, cc) in visited or maze[rr][cc] == 'W':
                continue
            queue += [(rr, cc)]
            visited += [(rr, cc)]

        if len(queue) == 0:
            return False