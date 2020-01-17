from math import pi


def iter_pi(epsilon):
    pi_div4_approx = 0
    sign, den = 1, 1
    i = 0
    while abs(pi - 4 * pi_div4_approx) >= epsilon:
        pi_div4_approx += [-1, 1][sign] / den
        sign ^= 1
        den += 2
        i += 1
    return [i, round(4 * pi_div4_approx, 10)]
