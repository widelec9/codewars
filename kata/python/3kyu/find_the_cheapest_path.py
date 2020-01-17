import heapq


def cheapest_path(grid, start, end):
    if start == end:
        return []
    else:
        grid_len = (len(grid)-1, len(grid[0])-1)
        dr = [-1, 1, 0, 0]
        dc = [0, 0, 1, -1]
        dirs = {(-1, 0): 'up', (1, 0): 'down', (0, 1): 'right', (0, -1): 'left'}
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
                if 0 <= rc_next[0] <= grid_len[0] and 0 <= rc_next[1] <= grid_len[1]:
                    new_cost = cost_from_start[rc_current] + grid[rc_current[0]][rc_current[1]]
                    if rc_next not in cost_from_start or new_cost < cost_from_start[rc_next]:
                        cost_from_start[rc_next] = new_cost
                        f = cost_from_start[rc_next] + (end[0] - rc_next[0]) + (end[1] - rc_next[1])  # f(x) = g(x) + h(x) -> cost_from_start + straight distance to end
                        heapq.heappush(queue, (f, rc_next))
                        came_from[rc_next] = rc_current
        rc_current = end
        path = []
        while True:
            path += [dirs[(rc_current[0]-came_from[rc_current][0], rc_current[1]-came_from[rc_current][1])]]
            if came_from[rc_current] == start:
                return path[::-1]
            rc_current = came_from[rc_current]
