def get_pf(n):
    pf = []
    n = abs(n)
    for i in range(2, n+1):
        while not n % i:
            pf += [i]
            n //= i
    return pf


def sum_for_list(lst):
    pfactors = set(sum([get_pf(n) for n in lst], []))
    return sorted([[pr, sum([k for k in lst if not k % pr])] for pr in pfactors], key=lambda x: x[0])

