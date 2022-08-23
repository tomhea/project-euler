from math import *
from time import time


def p23():
    lim, sum_of = 28123, 0
    ab_dict = [False] * lim

    for i in range(lim):
        dev_sum = 0
        for d in range(1, int(sqrt(i)) + 1):
            if i % d == 0:
                dev_sum += d if d * d == i else d + i // d
        ab_dict[i] = dev_sum - i > i

    for i in range(1, lim):
        add = True
        for j in range(1, i):
            if ab_dict[j] and ab_dict[i - j]:
                add = False
                break
        if add:
            sum_of += i

    return sum_of


def p24():
    per, digits = 1000000 - 1, 10
    dig_list = list(range(digits))
    fact = [1] + [i for i in range(1, digits)]
    for i in range(1, digits):
        fact[i] *= fact[i - 1]
    num = ''

    for i in range(digits):
        digit = dig_list[per // fact[digits - 1 - i]]
        dig_list.remove(digit)
        num += str(digit)
        per %= fact[digits - 1 - i]

    return num


# for p26
def dig_cyc(num, search_to):
    i, n = 0, 1
    nums = []

    while i < search_to:
        nums += [n % num]
        n *= 10
        for j in range(i):
            if nums[i] == nums[j]:
                return i - j
        i += 1

    return search_to


def p26():
    search_to = 1000
    max_d, max_i = 1, dig_cyc(1, search_to)

    for d in range(2, search_to):
        i = dig_cyc(d, search_to)
        if i > max_i:
            max_i, max_d = i, d

    return max_d


def p28():
    num, sum_of, val = 1001, 1, 1

    for i in range(1, num, 2):
        for j in range(4):
            val += i + 1
            sum_of += val

    return sum_of


def p29():
    start, end, distinct = 2, 100, 0
    have_been = []
    for i in range(start, end + 1):
        if i not in have_been:
            max_of = int(log(end, i))
            power_range = [False] * (max_of * end + 1)

            for pow_i in range(1, max_of + 1):
                for power in range(start, end + 1):
                    power_range[pow_i * power] = True
                have_been += [pow(i, pow_i)]

            for place in range(1, max_of * end + 1):
                distinct += power_range[place]

    return distinct


def p30():
    start_num, p, digits = 2, 5, 10
    max_num, sum_of = int((p + 1) * pow(digits - 1, p)), 0

    for i in range(start_num, max_num):
        old_num, new_num = i, 0

        while old_num:
            new_num += pow(old_num % digits, p)
            old_num //= digits

        if new_num == i:
            sum_of += i

    return sum_of


def timed_run():
    start = time()
    print(p30())
    print(f"{time() - start:0.2f}s")


if __name__ == '__main__':
    timed_run()
