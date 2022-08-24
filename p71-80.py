from itertools import combinations, product
from string import ascii_lowercase
from time import time

import numpy as np
from tqdm import tqdm

from math_utils import is_prime, choose


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def p71():
    max_numerator = None
    max_fraction = None

    for denominator in tqdm(range(1, 1000001)):
        if denominator % 7 == 0:
            continue

        numerator = (denominator * 3) // 7
        if gcd(numerator, denominator) != 1:
            continue

        if not max_fraction or numerator / denominator > max_fraction:
            max_fraction = numerator / denominator
            max_numerator = numerator

    return max_numerator


def timed_run():
    start = time()
    print(f"Result: {p71()}")
    print(f"The run took {time() - start:0.2f}s")


if __name__ == '__main__':
    timed_run()
