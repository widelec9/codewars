def dbl_linear(n):
    y_cnt, z_cnt, eq = 0, 0, 0
    u = [1]
    while y_cnt + z_cnt < n + eq:
        y = 2 * u[y_cnt] + 1
        z = 3 * u[z_cnt] + 1
        if y < z:
            u += [y]
            y_cnt += 1
        elif y > z:
            u += [z]
            z_cnt += 1
        else:
            u += [y]
            y_cnt, z_cnt, eq = y_cnt+1, z_cnt+1, eq+1
    return u[-1]
