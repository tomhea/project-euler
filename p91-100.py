from itertools import combinations, product
from time import time
from typing import Optional, List

import numpy as np
from tqdm import tqdm


def p92():
    biggest_square_sum = (9**2) * 7
    solutions: List[Optional[bool]] = [None] * (biggest_square_sum + 1)
    solutions[1] = False
    solutions[89] = True

    for x in range(1, biggest_square_sum + 1):
        numbers_chain = []
        while solutions[x] is None:
            numbers_chain.append(x)
            x = sum(int(x)**2 for x in str(x))
        for number in numbers_chain:
            solutions[number] = solutions[x]

    count89 = 0
    digits_sums_under_1000 = [sum(int(x)**2 for x in str(x)) for x in range(1000)]
    for x in tqdm(range(10 ** 4)):
        sum_4 = sum(int(x) ** 2 for x in str(x))
        for i in range(1000):
            if solutions[sum_4 + digits_sums_under_1000[i]]:
                count89 += 1

    return count89


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
    print(f"Result: {p92()}")
    print(f"The run took {time() - start:0.2f}s")


if __name__ == '__main__':
    timed_run()
