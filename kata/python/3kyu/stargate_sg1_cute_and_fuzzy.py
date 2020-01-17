import heapq


def wire_DHD_SG1(grid):
    grid = [[c for c in row] for row in grid.split('\n')]
    grid_len = (len(grid)-1, len(grid[0])-1)
    start, end = (0, 0), (0, 0)
    for i, row in enumerate(grid):
        if 'S' in row:
            start = (i, row.index('S'))
        if 'G' in row:
            end = (i, row.index('G'))
    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]
    queue = []
    heapq.heappush(queue, (0, start))  # cost, (x,y)
    came_from = {start: None}
    cost_from_start = {start: 0}
    while queue:
        rc_current = heapq.heappop(queue)[1]
        if rc_current == end:
            break
        for i in range(len(dr)):
            rc_next = (rc_current[0] + dr[i], rc_current[1] + dc[i])
            if 0 <= rc_next[0] <= grid_len[0] and 0 <= rc_next[1] <= grid_len[1] and grid[rc_next[0]][rc_next[1]] != 'X':
                new_cost = cost_from_start[rc_current] + ((rc_next[0] - rc_current[0])**2 + (rc_next[1] - rc_current[1])**2)**0.5
                if rc_next not in cost_from_start or new_cost < cost_from_start[rc_next]:
                    cost_from_start[rc_next] = new_cost
                    f = cost_from_start[rc_next] + ((end[0] - rc_current[0])**2 + (end[1] - rc_current[1])**2)**0.5
                    heapq.heappush(queue, (f, rc_next))
                    came_from[rc_next] = rc_current
    rc_current = end
    if rc_current not in came_from.keys():
        return "Oh for crying out loud..."
    else:
        while True:
            if grid[rc_current[0]][rc_current[1]] != 'G':
                grid[rc_current[0]][rc_current[1]] = 'P'
            if came_from[rc_current] == start:
                return '\n'.join([''.join(row) for row in grid])
            rc_current = came_from[rc_current]
