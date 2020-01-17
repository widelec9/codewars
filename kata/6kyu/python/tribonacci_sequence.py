def tribonacci(signature, n):
    tr = signature
    while len(tr) < n:
        tr.append(tr[-3] + tr[-2] + tr[-1])
    return tr[:n]