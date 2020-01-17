def doubles(maxk, maxn):
    return sum([((n+1)**(-2*k))/k for n in range(1, maxn+1) for k in range(1, maxk+1)])
