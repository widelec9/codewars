import heapq


def path_finder(maze):
    maze = [[int(dig) for dig in row] for row in maze.split('\n')]
    end = (len(maze)-1, len(maze)-1)
    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]
    queue = []
    heapq.heappush(queue, ((0, 0), 0))  # (x,y), cost)
    cost_from_start = {(0, 0): 0}
    while queue:
        pr, pc = heapq.heappop(queue)[0]
        if (pr, pc) == end:
            break
        curr_alt = maze[pr][pc]
        for i in range(4):
            rr, cc = pr + dr[i], pc + dc[i]
            if 0 <= rr <= end[0] and 0 <= cc <= end[1]:
                new_cost = cost_from_start[(pr, pc)] + abs(maze[rr][cc] - curr_alt)
                if (rr, cc) not in cost_from_start or new_cost < cost_from_start[(rr, cc)]:
                    cost_from_start[(rr, cc)] = new_cost
                    f = new_cost + (end[0] - rr) + (end[1] - cc)  # f(x) = g(x) + h(x) -> cost_from_start + straight distance to end
                    heapq.heappush(queue, ((rr, cc), f))
    return cost_from_start[end]
