from itertools import combinations, product
from string import ascii_lowercase
from time import time

import numpy as np
from tqdm import tqdm

from math_utils import is_prime, choose


def p85():
    result_rects = 2000000
    closest_area = None
    closest_rects_diff = None

    s = [(n * (n + 1)) // 2 for n in range(2001)]

    for m in tqdm(range(1, 2001)):
        for n in range(1, 2001):
            if closest_rects_diff is None or abs(s[n] * s[m] - result_rects) < closest_rects_diff:
                closest_rects_diff = abs(s[n] * s[m] - result_rects)
                closest_area = m * n

    return closest_area


def timed_run():
    start = time()
    print(f"Result: {p85()}")
    print(f"The run took {time() - start:0.2f}s")


if __name__ == '__main__':
    timed_run()
