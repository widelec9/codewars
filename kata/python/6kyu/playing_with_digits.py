def dig_pow(n, p):
    s = 0
    for dig in str(n):
        s += pow(int(dig), p)
        p += 1
    return int(s / n) if s % n == 0 else -1