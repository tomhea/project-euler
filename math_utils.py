from functools import reduce
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


def choose(n, k):
    return reduce(mul, range(n-k+1, n+1), 1) // reduce(mul, range(1, k+1), 1)