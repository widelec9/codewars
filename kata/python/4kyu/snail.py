def snail(smap):
    if smap == [[]]:
        return []
    else:
        n = len(smap)
        start = 0
        i_g, j_g = 0, 0
        right_down = 1
        ret = [smap[i_g][j_g]]
        while len(ret) != n ** 2:
            if right_down == 1:
                for j in range(j_g + 1, n):
                    ret.append(smap[i_g][j])
                for i in range(i_g + 1, n):
                    ret.append(smap[i][j])
                for j in range(j - 1, start - 1, -1):
                    ret.append(smap[i][j])
                i_g, j_g = i, j
                n -= 1
                start += 1
            else:
                for i in range(i_g - 1, start - 1, -1):
                    ret.append(smap[i][j_g])
                for j in range(j_g + 1, n):
                    ret.append(smap[i][j])
                for i in range(i_g + 1, n):
                    ret.append(smap[i][j])
                i_g, j_g = i, j
            right_down ^= 1
        return ret
