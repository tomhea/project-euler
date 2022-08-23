from itertools import combinations, product
from time import time

import numpy as np


def p97():
    big_mod = 10 ** 10

    res = 1
    for _ in range(783045):
        res = (res << 10) % big_mod

    return (28433 * (1 << 7) * res + 1) % big_mod


def p99(path='Data/p099_base_exp.txt'):
    nums = [[int(a) for a in num.split(',')] for num in open(path).read().splitlines()]
    return np.argmax([np.log(a) * b for a, b in nums]) + 1


def timed_run():
    start = time()
    print(f"Result: {p97()}")
    print(f"The run took {time() - start:0.2f}s")


if __name__ == '__main__':
    timed_run()
