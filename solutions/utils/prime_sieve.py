def prime_sieve(lim, reverse=False):
    primes = [True] * (lim + 1)

    primes[0], primes[1] = False, False

    for i in range(2, int(lim**0.5)+1):
        if primes[i]:
            for j in range(i * i, lim + 1, i):
                primes[j] = False
    if reverse:
        return [i for i in range(lim, -1, -1) if primes[i]]
    return [i for i in range(0, lim+1, 1) if primes[i]]
