def prime_generator(lim):
    primes = [2, 3]
    i = 6  # All primes one more or one less than a multiple of 6
    while len(primes) < lim:
        if not any(filter(lambda x: (i-1) % x == 0, list(filter(lambda x: x <= (i**0.5)+1, primes)))):
            primes.append(i-1)
        if len(primes) < lim and not any(filter(lambda x: (i+1) % x == 0,
                                                list(filter(lambda x: x <= (i**0.5)+1, primes)))):
            primes.append(i+1)
        i += 6
    return primes
