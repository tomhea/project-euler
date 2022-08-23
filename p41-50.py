import math
from time import time

from math_utils import is_prime, list_is_prime


def p40():
    d = ''
    for x in range(500005):
        d += str(x)

    mul = 1
    for n in range(7):
        mul *= ord(d[10 ** n]) - ord('0')

    return mul


def max_prime_pan(num, digits, used, n):
    if used == n:
        num = int(num)
        return num if is_prime(num) else 0

    max_pan = 0
    for d in range(1, n + 1):
        if digits[d]:
            digits[d] = 0
            max_pan = max(max_pan, max_prime_pan(num + str(d), digits, used + 1, n))
            digits[d] = 1

    return max_pan


def p41():
    max_pan = 0

    for n in range(2, 7 + 1):
        max_pan = max(max_pan, max_prime_pan('', [0] + [1] * n, 0, n))

    return max_pan


def p43(num=0, digits=None, passed=0):
    if digits is None:
        digits = [1] * 10

    if passed == 10:
        num = str(num)
        for i in range(7):
            if int(num[i + 1:i + 4]) % (2, 3, 5, 7, 11, 13, 17)[i]:
                return 0
        return int(num)

    counter = 0
    for n in range(10):
        if digits[n]:
            digits[n] = 0
            counter += p43(num * 10 + n, digits, passed + 1)
            digits[n] = 1

    return counter


def p44():
    pent, bool_pent = [0], [0]
    start_from, end = [1], 1

    while True:
        start, end = end, end * 2

        for n in range(start, end):
            pent += [n * (3 * n - 1) // 2]
            bool_pent += 3 * (n - 1) * [0] + [1]
            start_from += [n + 1]

        upper_bound = len(bool_pent) - 1
        for j in range(1, end):
            for k in range(start_from[j], end):
                diff, sum_of = pent[k] - pent[j], pent[k] + pent[j]
                if sum_of > upper_bound:
                    start_from[j] = k
                    break
                if bool_pent[diff] and bool_pent[sum_of]:
                    return diff
            if pent[end - 1] + pent[j] <= upper_bound:
                start_from[j] = end - 1


def p45():
    n_hexa = 144

    while True:
        x = n_hexa * (2 * n_hexa - 1)
        n_penta = (math.sqrt(24 * x + 1) + 1) // 6

        if int(n_penta) == n_penta:
            return x

        n_hexa += 1


def four_distinct_factors(x, primes):
    counter = 0
    for p in primes:
        if p > x or counter > 4:
            return counter == 4
        if x % p == 0:
            counter += 1
            while x % p == 0:
                x //= p


def p47_opt1():
    end = 5
    primes = [2, 3]
    counter = 0

    while True:
        start, end = end, end + 10000

        for x in range(start, end, 2):
            for p in primes:
                if p > int(math.sqrt(x)):
                    primes += [x]
                    break
                if x % p == 0:
                    break

        for d in range(start, end):
            counter = counter + 1 if four_distinct_factors(d, primes) else 0
            if counter == 4:
                return d - 3


def p47_opt2():
    wanted, n = [4] * 4, 1000

    while True:
        factors = [0] * n
        for p in range(2, n):
            if factors[p] == 0:
                for x in range(2 * p, n, p):
                    factors[x] += 1

        for i in range(n - 4):
            if factors[i:i + 4] == wanted:
                return i

        n *= 2


def p47(smarter=True):
    return p47_opt2() if smarter else p47_opt1()


def p48_opt1():
    return sum(x ** x for x in range(1, 1001)) % 10 ** 10


def mod_pow(a, b, m):
    s = 1
    for i in range(b):
        s = s * a % m
    return s


def p48_opt2():
    return sum(mod_pow(x, x, 10 ** 10) for x in range(1, 1001)) % 10 ** 10


def p48(smarter=True):
    return p48_opt2() if smarter else p48_opt1()


def p49():
    primes = list_is_prime(10000)

    for x in range(1000, 10000):
        sorted_x = sorted(str(x))
        if primes[x] and x != 1487:
            for jump in range(1, (10000 - x) // 2):
                x1, x2 = x + jump, x + 2 * jump
                if primes[x1] and primes[x2]:
                    if sorted(str(x2)) == sorted_x and sorted(str(x1)) == sorted_x:
                        return '%d%d%d\n' % (x, x1, x2)


def p50():
    n = 1000000
    max_counter, max_prime_sum = 21, 953
    bool_primes, primes = list_is_prime(n, True)
    max_p = sum(bool_primes[:n // max_counter]) + 1

    for i in range(max_p):
        prime_sum, counter = 0, 0
        while prime_sum + primes[i + counter] < n:
            prime_sum += primes[i + counter]
            counter += 1
            if counter > max_counter and bool_primes[prime_sum]:
                max_counter, max_prime_sum = counter, prime_sum

    return max_prime_sum


def timed_run():
    start = time()
    print(p50())
    print(f"{time() - start:0.2f}s")


if __name__ == '__main__':
    timed_run()
