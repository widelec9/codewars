def primes1(n):
    sieve = [True] * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]


primes = set(primes1(10000000))


def find_emirp(n):
    emirps = {i for i in range(13, n+1) if int(str(i)[::-1]) != i and i in primes and int(str(i)[::-1]) in primes}
    return [len(emirps), max(emirps), sum(emirps)] if len(emirps) > 0 else [0, 0, 0]