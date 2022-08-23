from math import *
from time import time

from math_utils import list_is_prime


def p31(wanted=200, coins=(200, 100, 50, 20, 10, 5, 2, 1)):
    if len(coins) == 1:
        return wanted >= 0 and wanted % coins[0] == 0

    num_of_choices = 0
    for n in range(int(wanted // coins[0]) + 1):
        num_of_choices += p31(wanted - n * coins[0], coins[1:])

    return num_of_choices


def p32():
    min_of, max_of, sum_of = 1000, 10000, 0
    counted = [False] * max_of

    for i in range(1, min_of):
        for j in range(min_of // i, max_of // i):
            dig = [0] * 10
            a, b, c = i, j, i * j

            while a:
                dig[a % 10] += 1
                a //= 10
            while b:
                dig[b % 10] += 1
                b //= 10
            while c:
                dig[c % 10] += 1
                c //= 10

            pandigital = dig[0] == 0
            for digit in dig[1:]:
                if digit != 1:
                    pandigital = False
            if pandigital:
                if not counted[i * j]:
                    sum_of += i * j
                    counted[i * j] = True

    return sum_of


def gcd(m, n):
    return gcd(n, m % n) if n else m


def list_primes(n):
    if n <= 2:
        return [] if n - 2 else [2]

    primes = [2, 3]
    for y in range(5, n + 1, 6):
        for x in [y, y + 2] if y + 2 <= n else [y]:
            square = int(sqrt(x))
            for p in primes:
                if p > square:
                    primes += [x]
                    break
                if x % p == 0:
                    break
    return primes


def p33():
    x, y = 1, 1
    for a in range(11, 100):
        for b in range(a + 1, 100):
            if a % 10 and a % 10 == b // 10:
                if (a // 10) * b == a * (b % 10):
                    x, y = a * x, b * y
    return y // gcd(x, y)


def p35():
    n = 1000000
    (bool_primes, primes), have_been = list_is_prime(n, True), [False] * (n + 1)
    val, valc, counter = 1, 0, 3
    if n <= 5:
        return sum(bool_primes.values())

    for p in primes[counter:]:  # 2,3,5 already counted
        if not have_been[p]:
            if p > val:
                val *= 10
                valc += 1
            s, proceed, num = str(p), True, p

            while num:
                if not num % 2 and num % 5:
                    proceed = False
                    break
                num //= 10

            temp_counter = 1
            have_been[p] = True
            for i in range(valc):
                s = s[1:] + s[0]
                if not bool_primes[int(s)]:
                    proceed = False
                    break
                temp_counter += not have_been[int(s)]
                have_been[int(s)] = True
            if proceed:
                counter += temp_counter

    return counter


def is_prime(x):
    if x <= 3:
        return x >= 2
    if x % 2 == 0 or x % 3 == 0:
        return False

    for p in range(5, int(sqrt(x)) + 1, 6):
        if x % p == 0 or x % (p + 2) == 0:
            return False

    return True


def p35s():
    n = 1000000
    have_been = [False] * (n + 1)
    val, valc, counter = 1, 0, 4
    if n <= 7:
        return 0 if n <= 1 else (n + 1) // 2

    for p in range(11, n + 1, 2):  # 2,3,5 already counted
        if not have_been[p]:
            if not is_prime(p):
                continue
            if p > val:
                val *= 10
                valc += 1

            s, proceed, num = str(p), True, p

            while num:
                if num % 2 == 0 or num % 5 == 0:
                    proceed = False
                    break
                num //= 10

            temp_counter = 1

            for i in range(1, valc):
                p = int(s[1:] + s[0])
                s = str(p)
                if not proceed or not is_prime(p):
                    proceed = False
                temp_counter += not have_been[p]
                have_been[p] = True

            if proceed:
                counter += temp_counter

    return counter


def is_palindrome(s):
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - 1 - i]:
            return False
    return True


def p36():
    counter = 0

    for x in range(1000000):
        if is_palindrome(str(x)) and is_palindrome(bin(x)[2:]):
            counter += x

    return counter


def p37():
    counter, sum_of, x = 0, 0, 10
    primes = list_is_prime(x - 1)

    while counter < 11:
        if is_prime(x):
            primes += [1]
            a, b = x // 10, str(x)[1:]
            proceed = True
            while proceed and a:
                if not primes[a]:
                    proceed = False
                a //= 10

            while proceed and b:
                if not primes[int(b)]:
                    proceed = False
                b = str(b)[1:]

            if proceed:
                counter += 1
                sum_of += x
        else:
            primes += [0]
        x += 1

    return sum_of


def p38():
    max_pan, wanted = 123456789, sorted('123456789')

    for x in range(2, 10000):
        s, n = '', 1
        while len(s) < 9:
            s += str(x * n)
            n += 1

        if sorted(s) == wanted:
            pan = int(s)
            if pan > max_pan:
                max_pan = pan

    return max_pan


def p39():
    max_p, max_sol, n = 0, 0, 1000

    for p in range(n + 1):
        sols = 0

        for c in range(5, p // 2):
            delta = 4 * c ** 2 + 8 * p * c - 4 * p ** 2
            if delta >= 0 and sqrt(delta) == int(sqrt(delta)):
                sols += 1

        if sols > max_sol:
            max_sol = sols
            max_p = p

    return max_p


def p40():
    d = ''
    for x in range(500005):
        d += str(x)

    mul = 1
    for n in range(7):
        mul *= ord(d[10 ** n]) - ord('0')

    return mul


def timed_run():
    start = time()
    print(p40())
    print(f"{time() - start:0.2f}s")


if __name__ == '__main__':
    timed_run()
