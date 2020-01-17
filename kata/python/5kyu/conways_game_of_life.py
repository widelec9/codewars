def next_gen(cells):
    if not cells:
        return []
    else:
        cells_next = [[0 for i in range(len(cells[0]))] for j in range(len(cells))]
        dr = (-1, -1, 0, 1, 1, 1, 0, -1)
        dc = (0, 1, 1, 1, 0, -1, -1, -1)
        for i, row in enumerate(cells):
            for j, col in enumerate(row):
                live_ngbr_count = 0
                for k in range(len(dr)):
                    if 0 <= i+dr[k] <= len(cells)-1 and 0 <= j+dc[k] <= len(cells[0])-1 and cells[i+dr[k]][j+dc[k]] == 1:
                        live_ngbr_count += 1
                cells_next[i][j] = (1 if 2 <= live_ngbr_count <= 3 else 0) if cells[i][j] == 1 else (1 if live_ngbr_count == 3 else 0)
        return cells_next
