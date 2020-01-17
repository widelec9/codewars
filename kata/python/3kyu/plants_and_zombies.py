def plants_and_zombies(lawn, zombies):
    lawn = [[j for j in i] for i in lawn]
    shooters = [(i, j, int(lawn[i][j])) for i, l in enumerate(lawn) for j, c in enumerate(l) if ord('1') <= ord(lawn[i][j]) <= ord('9')] + \
               sorted(sorted([(i, j, 'S') for i, l in enumerate(lawn) for j, c in enumerate(l) if lawn[i][j] == 'S'], key=lambda x: x[0]), key=lambda x: x[1], reverse=True)
    zomb_lawn = []

    i = 0
    while True:
        for k, z in enumerate(zomb_lawn):
            if z[1] == 0:
                return i
            if lawn[z[0]][z[1]-1] != ' ':
                shooters.pop([(sh[0], sh[1]) for sh in shooters].index((z[0], z[1]-1)))
            lawn[z[0]][z[1]-1] = lawn[z[0]][z[1]]
            lawn[z[0]][z[1]] = ' '
            zomb_lawn[k] = (z[0], z[1]-1)

        while len(zombies) > 0 and zombies[0][0] == i:
            lawn[zombies[0][1]][-1] = zombies[0][2]
            zomb_lawn += [(zombies[0][1], len(lawn[zombies[0][1]])-1)]
            zombies.pop(0)

        shooters_num_copy = sorted([list(sh) for sh in shooters if sh[2] != 'S' and any(type(el) == int for el in lawn[sh[0]])], key=lambda x: x[2], reverse=True)
        while len(shooters_num_copy) > 0:
            for s, sh in enumerate(shooters_num_copy):
                zos_in_row = sorted([z for z in zomb_lawn if z[0] == sh[0]], key=lambda x: x[1])
                if len(zos_in_row) > 0:
                    zo_hit = (zos_in_row[0][0], zos_in_row[0][1])
                    lawn[zo_hit[0]][zo_hit[1]] -= 1
                    shooters_num_copy[s][2] -= 1

                    if lawn[zo_hit[0]][zo_hit[1]] <= 0:
                        lawn[zo_hit[0]][zo_hit[1]] = ' '
                        zomb_lawn.remove(zo_hit)

                    if shooters_num_copy[s][2] == 0:
                        shooters_num_copy.pop(s)
                else:
                    shooters_num_copy.pop(s)

        for s, sh in enumerate([sh for sh in shooters if sh[2] == 'S']):
            zo_hit = []
            zos_in_row = sorted([z for z in zomb_lawn if z[0] == sh[0] and z[1] > sh[1]], key=lambda x: x[1])
            if len(zos_in_row) > 0:
                zo_hit += [(zos_in_row[0][0], zos_in_row[0][1])]
            zos_in_diags = [z for z in zomb_lawn if abs(z[0] - sh[0]) == abs(z[1] - sh[1]) and z[1] > sh[1]]
            if len(zos_in_diags) > 0:
                zo_hit_diag_up = sorted([z for z in zos_in_diags if z[0] < sh[0]], key=lambda x: x[0] - sh[0], reverse=True)
                if len(zo_hit_diag_up) > 0:
                    zo_hit += [zo_hit_diag_up[0]]
                zo_hit_diag_down = sorted([z for z in zos_in_diags if z[0] > sh[0]], key=lambda x: abs(x[0] - sh[0]))
                if len(zo_hit_diag_down) > 0:
                    zo_hit += [zo_hit_diag_down[0]]

            for z in zo_hit:
                lawn[z[0]][z[1]] -= 1
                if lawn[z[0]][z[1]] <= 0:
                    lawn[z[0]][z[1]] = ' '
                    zomb_lawn.remove(z)

        if len(zomb_lawn) == 0 and len(zombies) == 0:
            return None
        i += 1
