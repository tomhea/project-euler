import numpy as np
import math
import primesieve as ps
from itertools import combinations, product
from utils import is_prime, choose
from string import ascii_lowercase
from tqdm import tqdm



def p51():
    # indexes = where the replicated digits will be.
    # result = False if None,
    def get_smallest_prime_with_8prime_family(num_of_digits, indexes):
        curr_min = None
        for p in product((str(i) for i in range(10)), repeat=num_of_digits - len(indexes)):
            p_str = ''
            for i in range(num_of_digits):  # p_str will be 'd2d3d3' for indexes=(0,2,4), p=(2,3,3) and num_of_digits=6
                if i in indexes:
                    p_str += 'd'
                else:
                    p_str += p[0]
                    p = p[1:]
            start = 1 if 0 in indexes else 0
            num_of_primes = sum([is_prime(int(p_str.replace('d', str(d)))) for d in range(start, 10)])
            if num_of_primes >= 8:
                for maybe_prime in (int(p_str.replace('d', d)) for d in ('0', '1', '2')):
                    if is_prime(maybe_prime):
                        if curr_min is None or curr_min > maybe_prime:
                            curr_min = maybe_prime
                        break
        return curr_min
        # 3 at a time, not the last one.
        # print(''.join(['*' if i in indexes else '_' for i in range(num_of_digits)]))

    num_of_digits = 1
    while True:
        for num_of_indexes in range(3, num_of_digits, 3):
            for indexes in combinations(range(num_of_digits-1), num_of_indexes):    # indexes are good only if the number of them is divisable by 3 (so that it may be that None of the tested numbers will be divided by 3), and should leave the Least-Significant-Digit not in indexes, because of even numbers..
                res = get_smallest_prime_with_8prime_family(num_of_digits, indexes)
                if res:
                    return res
        num_of_digits += 1


def p52():
    nods = 6
    while True:
        for x in range(10**(nods-1), 10**nods//6+1):
            if len(set(sum(10**int(d) for d in str(n*x)) for n in range(1, 6+1))) == 1:
                return x
        nods += 1


def p53():
    counter = 0
    for n in range(1, 100+1):
        for k in range(n):
            if choose(n, k) > 10**6:
                counter += n+1-2*k
                break
    return counter


def p54(path='Data/p054_poker.txt'):
    # curr[0] = (High Card, One Pair, Two Pairs, Three of a Kind, Straight, Flush, Full House, Four of a Kind, Straight Flush, Royal Flush)
    def get_points(hand):
        curr = (0,0)
        nums, colors = [c[0] for c in hand], [c[1] for c in hand]
        if len(set(colors)) == 1:
            h = max(nums)
            if sorted(nums) == [h-4, h-3, h-2, h-1, h]:
                return (9,) if h == 14 else (8,h)
            else:
                curr = (5, sorted(nums)[::-1])
        if len(set(nums)) == 2:
            if len(set(sorted(nums)[1:-1])) == 1:
                return (7, sorted(nums)[2], sorted(nums)[::-1])
            else:
                return (6, sorted(nums)[2], sorted(nums)[::-1])
        if curr[0] == 5:
            return curr
        h = max(nums)
        if sorted(nums) == [h - 4, h - 3, h - 2, h - 1, h]:
            return (4, sorted(nums)[::-1])
        hist = [sum(n==d for n in nums) for d in range(14+1)]
        if 3 in hist:
            n = hist.index(3)
            return (3, n, sorted(nums)[::-1])
        if 2 in hist:
            l, r = hist.index(2), len(hist)-1 - hist[::-1].index(2)
            if l != r:
                return (2, max(l,r), min(l,r), sorted(nums)[::-1])
            else:
                return (1, l, sorted(nums)[::-1])
        return (0, sorted(nums)[::-1])

    def who_wins(str_hands):
        cards = [('__23456789TJQKA'.index(c[0]), c[1]) for c in str_hands.split()]
        return get_points(cards[:5]) > get_points(cards[5:])

    return sum(who_wins(line) for line in open(path).read().splitlines())


def p55():
    def is_lychrel(n, iterations_left=50, first_iter=True):
        if iterations_left == 0:
            return True
        if not first_iter and str(n) == str(n)[::-1]:
            return False
        return is_lychrel(n + int(str(n)[::-1]), iterations_left-1, False)

    return sum(is_lychrel(n) for n in range(10000))


def p56():
    return max([sum(int(c) for c in str(a**b)) for a in range(100) for b in range(100)])


def p57(bound=1000):
    counter = 0
    a,b = 1,1
    for i in range(bound):
        a, b = a+2*b, a+b
        counter += len(str(a)) > len(str(b))
    return counter


def p58(prime_density=0.1):
    side_length = 3
    primes = 3
    total = 5
    last = 9
    while primes >= total*prime_density:
        side_length += 2
        total += 4
        jmp = side_length-1
        start, last = last+jmp, last+4*jmp
        primes += sum(is_prime(p) for p in range(start, last+1, jmp))

    return side_length


def p59(path='Data/p059_cipher.txt'):
    nums = [int(x) for x in open(path).readline().split(',')]
    max_count, max_s = 0, ''
    for password in product(ascii_lowercase, repeat=3):
        s = ''.join([chr(nums[i]^ord(password[i%3])) for i in range(len(nums))])
        count = s.lower().count('the')  # the most frequently used word in english
        if count > max_count:
            max_count, max_s = count, s

    return sum(ord(c) for c in max_s)


def p60_find_5primes(low, high):
    primes = ps.primes(100000)[1:]
    n = len(primes)
    primes_set = set(primes)
    primes1 = [p for p in primes if p%3==1]
    primes2 = [p for p in primes if p%3==2]

    res = set()
    for i1 in tqdm(range(n)):
        p1 = primes[i1]
        if p1 * 5 >= high: break
        for i2 in range(i1+1, n):
            p2 = prines[i2]
            if (p1+p2)*5/2 >= high: break
            for i3 in range(i2+1, n):
                p3 = primes[i3]
                if (p1+p2+p3)*5/3 >= high: break
                for i4 in range(i3+1, n):
                    p4 = primes[i4]
                    if (p1+p2+p3)*5/4 >= high: break
                    for i5 in range(i4 + 1, n):
                        p5 = primes[i5]
                        sums = p1 + p2 + p3 + p4 + p5
                        if sums < low: continue
                        if sums >= high: break
                        if all(int(str(p)+str(q)) in primes_set for p,q in combinations([p1,p2,p3,p4,p5])):
                            res.add([p1,p2,p3,p4,p5])
    return res

def p60():
    i = 0
    while True:
        print(f'{i} - {i+99}:')
        res = p60_find_5primes(i, i+100)
        if res:
            min_sum, min = sum(res[0]), res[0]
            for p in res[1:]:
                if sum(p) < min_sum:
                    min_sum, min = sum(p), p
            return min
        i += 100





    sums = 1
    while True:
        print('curr sums:',sums)
        for primesk in (primes1, primes2):
            for p1 in [3] + primesk:
                if p1 > sums: break
                for p2 in primesk:
                    if p1>=p2 or p1+p2 > sums: break
                    for p3 in primesk:
                        if p2>=p3 or p1+p2+p3 > sums: break
                        for p4 in primesk:
                            p5 = sums-(p1+p2+p3+p4)
                            if p4>=p5 or p5 not in primesk: break
                            if all(p != q or int(str(p)+str(q)) in primes_set for p,q in product((p1,p2,p3,p4,p5),repeat=2)):
                                return sums
        sums += 2


    # or 3 and four x=1(mod 3) or four x=2(mod 3), or all x=1(mod 3), or all x=2(mod 3)



def p99(path='Data/p099_base_exp.txt'):
    nums = [[int(a) for a in num.split(',')] for num in open(path).read().splitlines()]
    return np.argmax([np.log(a) * b for a, b in nums]) + 1


print(p60())
