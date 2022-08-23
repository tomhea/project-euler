from functools import reduce
from math import sqrt
from operator import mul


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def list_is_prime(n, primes_too=False):
    if n <= 0:
        return [] if n else [False]

    primes, bool_primes = [2, 3], [False] * (n + 1)
    for y in range(5, n + 1, 6):
        for x in [y, y + 2] if y + 2 <= n else [y]:
            square = int(sqrt(x))
            for p in primes:
                if p > square:
                    primes += [x]
                    bool_primes[x] = True
                    break
                if x % p == 0:
                    break

    if primes_too:
        return bool_primes, primes
    return bool_primes


def choose(n, k):
    return reduce(mul, range(n-k+1, n+1), 1) // reduce(mul, range(1, k+1), 1)