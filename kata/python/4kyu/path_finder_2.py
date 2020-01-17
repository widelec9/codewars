def path_finder(maze):
    maze = maze.split('\n')
    end = (len(maze)-1, len(maze)-1)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = [(0, 0)]
    nodes_left_in_layer = 1
    nodes_in_next_layer = 0
    visited = [[False for r in range(len(maze))] for i in range(len(maze))]
    dist = 0

    while len(queue) > 0:
        (pr, pc) = queue.pop(0)
        if (pr, pc) == end:
            return dist

        for i in range(4):
            rr = pr + dr[i]
            cc = pc + dc[i]

            if 0 <= rr <= end[0] and 0 <= cc <= end[1] and not visited[rr][cc] and maze[rr][cc] != 'W':
                queue += [(rr, cc)]
                visited[rr][cc] = True
                nodes_in_next_layer += 1

        nodes_left_in_layer -= 1

        if nodes_left_in_layer == 0:
            nodes_left_in_layer = nodes_in_next_layer
            nodes_in_next_layer = 0
            dist += 1
    return False