def witness_prime(num):
    """
    Returns whether a number is prime using 'witness numbers.' Inspired by the numberphile video at
    https://www.youtube.com/watch?v=_MscGSN5J6o

    :param num: int
    :return: boolean
    """

    # If number is 1, it is not prime
    if num == 1:
        return False
    # If number is 2, it is prime
    if num == 2:
        return True
    # If number is even, it is not prime
    if num % 2 == 0:
        return False

    # Change into form 2^m * d + 1
    d = num - 1
    m = 0
    while d % 2 == 0:
        d //= 2
        m += 1

    # Get 'star witnesses'
    if num < 1_373_653:
        a = [2, 3]
    elif num < 25_326_001:
        a = [2, 3, 5]
    elif num < 1_122_004_669_633:
        a = [2, 13, 23, 1_662_803]

    # Prime test
    def negmod(a):
        nonlocal m
        nonlocal d
        return -1 if pow(a, d, num) == num - 1 else pow(a, d, num)

    if not {1, -1} & set(map(negmod, a)):
        return False
    return True
