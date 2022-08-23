from math import *
from time import time


def p23():
    lim, sum = 28123, 0
    ab_dict = [False]*lim

    for i in xrange(lim):
        dev_sum = 0
        for d in xrange(1, int(sqrt(i))+1):
            if i%d == 0:
                dev_sum += d if d*d==i else d + i/d
        ab_dict[i] = dev_sum-i > i

    for i in xrange(1, lim):
        add = True
        for j in xrange(1, i):
            if ab_dict[j] and ab_dict[i-j]:
                add = False
                break
        if add:
            sum += i

    return sum


def p24():
    per, digits = 1000000-1, 10
    dig_list = list(range(digits))
    fact = [1] + [i for i in xrange(1, digits)]
    for i in xrange(1, digits):
        fact[i] *= fact[i-1]
        print fact[i]
    num = ''

    for i in xrange(digits):
        digit = dig_list[per/fact[digits-1 - i]]
        dig_list.remove(digit)
        num += str(digit)
        per %= fact[digits-1 - i]

    return num


# for p26
def dig_cyc(num, search_to):
    i, n = 0, 1
    nums = []

    while i < search_to:
        nums += [n % num]
        n *= 10
        for j in xrange(i):
            if nums[i] == nums[j]:
                return i-j
        i += 1

    return search_to


def p26():
    search_to = 1000
    max_d, max_i = 1, dig_cyc(1, search_to)

    for d in xrange(2, search_to):
        i = dig_cyc(d, search_to)
        if i > max_i:
            max_i, max_d = i, d

    return max_d


def p28():
    num, sum, val = 1001, 1, 1

    for i in xrange(1, num, 2):
        for j in xrange(4):
            val += i+1
            sum += val

    return sum


def p29():
    start, end, distinct = 2, 100, 0
    have_been = []
    for i in xrange(start, end+1):
        if i not in have_been:
            max = int(log(end, i))
            power_range = [False]*(max*end+1)

            for pow_i in xrange(1, max+1):
                for power in xrange(start, end+1):
                    power_range[pow_i*power] = True
                have_been += [pow(i, pow_i)]

            for place in xrange(1, max*end+1):
                distinct += power_range[place]

    return distinct


def p30():
    start_num, p, digits = 2, 5, 10
    max_num, sum = int((p+1) * pow(digits-1, p)), 0

    for i in xrange(start_num, max_num):
        old_num, new_num = i, 0

        while old_num:
            new_num += pow(old_num % digits, p)
            old_num /= digits

        if new_num == i:
            sum += i

    return sum


def p31(wanted=200, coins=[200,100,50,20,10,5,2,1]):
    if len(coins) == 1:
        return wanted >= 0 and wanted % coins[0] == 0

    num_of_choices = 0
    for n in xrange(int(wanted / coins[0]) + 1):
        num_of_choices += p31(wanted - n * coins[0], coins[1:])

    return num_of_choices


def p32():
    min, max, sum = 1000, 10000, 0
    counted = [False]*max

    for i in xrange(1, min):
        for j in xrange(min/i, max/i):
            dig = [0]*10
            a, b, c = i, j, i*j

            while a:
                dig[a%10] += 1
                a /= 10
            while b:
                dig[b%10] += 1
                b /= 10
            while c:
                dig[c%10] += 1
                c /= 10

            pandigital = dig[0] == 0
            for digit in dig[1:]:
                if digit != 1:
                    pandigital = False
            if pandigital:
                if not counted[i*j]:
                    sum += i*j
                    counted[i*j] = True

    return sum


def gcd(m, n):
    return gcd(n, m % n) if n else m


def list_primes(n):
    if n <= 2:
        return [] if n-2 else [2]

    primes = [2, 3]
    for y in xrange(5, n + 1, 6):
        for x in [y, y + 2] if y + 2 <= n else [y]:
            square = int(sqrt(x))
            for p in primes:
                if p > square:
                    primes += [x]
                    break
                if x % p == 0:
                    break
    return primes



def list_is_prime(n, primes_too=False):
    if n <= 0:
        return [] if n else [False]

    primes, bool_primes = [2, 3], [False]*(n+1)
    for y in xrange(5, n + 1, 6):
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


def p33():
    x, y = 1, 1
    for a in xrange(11, 100):
        for b in xrange(a+1, 100):
            if a%10 and a%10 == b/10:
                if (a/10) * b == a * (b%10):
                    x, y = a*x, b*y
    return y / gcd(x, y)


def p35():
    n = 1000000
    start = time()
    (bool_primes, primes), have_been = list_is_prime(n, True), [False]*(n+1)
    print time() - start
    val, valc, counter = 1, 0, 3
    if n <= 5:
        return sum(bool_primes.values())

    for p in primes[counter:]:        # 2,3,5 already counted
        if not have_been[p]:
            if p > val:
                val *= 10
                valc += 1
            s, proceed, num = str(p), True, p

            while num:
                if not num%2 and num%5:
                    proceed = False
                    break
                num /= 10

            temp_counter = 1
            have_been[p] = True
            for i in xrange(valc):
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
    if x%2 == 0 or x%3 == 0:
        return False

    for p in xrange(5, int(sqrt(x))+1, 6):
        if x%p == 0 or x%(p+2) == 0:
            return False

    return True


def p35s():
    n = 1000000
    have_been = [False] * (n + 1)
    val, valc, counter = 1, 0, 4
    if n <= 7:
        return 0 if n <= 1 else (n+1)/2

    for p in xrange(11, n+1, 2):  # 2,3,5 already counted
        if p%100000==1:
            print p-1
        if not have_been[p]:
            if not is_prime(p):
                continue
            if p > val:
                val *= 10
                valc += 1

            s, proceed, num = str(p), True, p

            while num:
                if num%2==0 or num%5==0:
                    proceed = False
                    break
                num /= 10

            if p == 101:
                print proceed

            temp_counter = 1

            for i in xrange(1, valc):
                p = int(s[1:] + s[0])
                s = str(p)
                if not proceed or not is_prime(p):
                    proceed = False
                temp_counter += not have_been[p]
                have_been[p] = True

            if proceed:
                counter += temp_counter

    return counter


def p43(num=0, digits=[1]*10, passed=0):
    if passed == 10:
        num = str(num)
        for i in xrange(7):
            if int(num[i+1:i+4]) % (2,3,5,7,11,13,17)[i]:
                return 0
        return int(num)

    counter = 0
    for n in xrange(10):
        if digits[n]:
            digits[n] = 0
            counter += p43(num*10+n, digits, passed+1)
            digits[n] = 1

    return counter


def is_palindrom(s):
    l = len(s)
    for i in xrange(l/2):
        if s[i] != s[l-1-i]:
            return False
    return True


def p36():
    counter = 0

    for x in xrange(1000000):
        if is_palindrom(str(x)) and is_palindrom(bin(x)[2:]):
            counter += x

    return counter


def p37():
    counter, sum, x = 0, 0, 10
    primes = list_is_prime(x-1)

    while counter < 11:
        if is_prime(x):
            primes += [1]
            a, b = x/10, str(x)[1:]
            proceed = True
            while proceed and a:
                if not primes[a]:
                    proceed = False
                a /= 10

            while proceed and b:
                if not primes[int(b)]:
                    proceed = False
                b = str(b)[1:]

            if proceed:
                counter += 1
                sum += x
        else:
            primes += [0]
        x += 1

    return sum


def p38():
    max_pan, wanted = 123456789, sorted('123456789')

    for x in xrange(2, 10000):
        s, n = '', 1
        while len(s) < 9:
            s += str(x*n)
            n += 1

        if sorted(s) == wanted:
            pan = int(s)
            if pan > max_pan:
                max_pan = pan

    return max_pan


def p39():
    max_p, max_sol, n = 0, 0, 1000

    for p in xrange(n + 1):
        sols = 0

        for c in xrange(5, p/2):
            delta = 4*c**2 + 8*p*c - 4*p**2
            if delta >= 0 and sqrt(delta) == int(sqrt(delta)):
                sols += 1

        if sols > max_sol:
            max_sol = sols
            max_p = p

    return max_p


def p40():
    d = ''
    for x in xrange(500005):
        d += str(x)

    mul = 1
    for n in xrange(7):
        mul *= ord(d[10 ** n]) - ord('0')

    return mul


def max_prime_pan(num, digits, used, n):
    if used == n:
        num = int(num)
        return num if is_prime(num) else 0

    max_pan = 0
    for d in xrange(1, n+1):
        if digits[d]:
            digits[d] = 0
            max_pan = max(max_pan, max_prime_pan(num+str(d), digits, used+1, n))
            digits[d] = 1

    return max_pan


def p41():
    max_pan = 0

    for n in xrange(2, 7+1):
        max_pan = max(max_pan, max_prime_pan('', [0]+[1]*n, 0, n))

    return max_pan


def p44():
    pent, bool_pent = [0], [0]
    start_from, end = [1], 1

    while True:
        start, end = end, end*2

        for n in xrange(start, end):
            pent += [n * (3*n - 1) / 2]
            bool_pent += 3 * (n-1) * [0] + [1]
            start_from += [n+1]

        upper_bound = len(bool_pent) - 1
        for j in xrange(1, end):
            for k in xrange(start_from[j], end):
                diff, sum = pent[k] - pent[j], pent[k] + pent[j]
                if sum > upper_bound:
                    start_from[j] = k
                    break
                if bool_pent[diff] and bool_pent[sum]:
                    return diff
            if pent[end-1] + pent[j] <= upper_bound:
                start_from[j] = end-1


def p45():
    n_hexa = 144

    while True:
        x = n_hexa * (2*n_hexa - 1)
        n_penta = (sqrt(24*x+1) + 1) / 6

        if int(n_penta) == n_penta:
            return x

        n_hexa += 1


def four_distinct_factors(x, primes):
    counter = 0
    for p in primes:
        if p > x or counter > 4:
            return counter == 4
        if x%p == 0:
            counter += 1
            while x%p == 0:
                x /= p



def p47_opt1():
    end = 5
    primes = [2, 3]
    counter = 0

    while True:
        start, end = end, end + 10000
        print start-5

        for x in xrange(start, end, 2):
            for p in primes:
                if p > int(sqrt(x)):
                    primes += [x]
                    break
                if x % p == 0:
                    break

        for d in xrange(start, end):
            counter = counter + 1 if four_distinct_factors(d, primes) else 0
            if counter == 4:
                return d-3


def p47_opt2():
    wanted, n = [4]*4, 1000

    while True:
        factors = [0]*n
        for p in range(2, n):
            if factors[p] == 0:
                for x in xrange(2*p, n, p):
                    factors[x] += 1

        for i in xrange(n-4):
            if factors[i:i+4] == wanted:
                return i

        n *= 2


def p47(smarter=True):
    return p47_opt2() if smarter else p47_opt1()


def p48_opt1():
    return sum(x**x for x in xrange(1,1001)) % 10**10


def mod_pow(a, b, m):
    s = 1
    for i in xrange(b):
        s = s*a % m
    return s


def p48_opt2():
    return sum(mod_pow(x,x,10**10) for x in xrange(1,1001)) % 10**10


def p48(smarter=True):
    return p48_opt2() if smarter else p48_opt1()


def p49():
    primes = list_is_prime(10000)

    for x in xrange(1000, 10000):
        sorted_x = sorted(str(x))
        if primes[x] and x != 1487:
            for jump in xrange(1, (10000 - x) / 2):
                x1, x2 = x+jump, x+2*jump
                if primes[x1] and primes[x2]:
                    if sorted(str(x2)) == sorted_x and sorted(str(x1)) == sorted_x:
                        return '%d%d%d\n' % (x, x1, x2)


def p50():
    n = 1000000
    max_counter, max_prime_sum = 21, 953
    bool_primes, primes = list_is_prime(n, True)
    max_p = sum(bool_primes[:n/max_counter]) + 1

    for i in xrange(max_p):
        prime_sum, counter = 0, 0
        while prime_sum + primes[i + counter] < n:
            prime_sum += primes[i + counter]
            counter += 1
            if counter > max_counter and bool_primes[prime_sum]:
                max_counter, max_prime_sum = counter, prime_sum

    return max_prime_sum


start = time()
print p50()
print time()-start
