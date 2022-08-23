from itertools import combinations, product
from string import ascii_lowercase
from time import time

import numpy as np

from math_utils import is_prime, choose


def p63():
    # note that 9**21 is 21 digits, and 9**22 is also 21 digits.
    # note that this feature can only be with bases of 1-9.
    return sum(1 for base in range(1, 10) for exp in range(1, 22) if len(str(base ** exp)) == exp)


def timed_run():
    start = time()
    print(f"Result: {p63()}")
    print(f"The run took {time() - start:0.2f}s")


if __name__ == '__main__':
    timed_run()
