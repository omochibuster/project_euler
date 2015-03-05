#-*-coding:utf-8-*-
#バグっている？

from itertools import takewhile, islice, count

def gen_prime_candidates():
    yield 2
    yield 3
    n = 5
    while True:
        yield n
        yield n + 2
        n += 6

def is_prime(n):
    for p in takewhile(lambda p: p * p <= n, gen_prime_candidates()):
        if n % p == 0:
            return False
    return True

def gen_digits(n):
    while n:
        yield n % 10
        n /= 10

def gen_comb(a, k = 0):
    if k == len(a) - 1:
        yield 0, 0
        yield 10 ** a[k], 1
    else:
        for n, l in gen_comb(a, k + 1):
            yield n, l
            yield n + 10 ** a[k], l + 1

def gen_mask(digits, d):
    def is_valid(t): return t[0] and t[0] % 30 == 0
    a0 = filter(lambda k: digits[k] == d, range(len(digits)))
    if len(a0):
        for n, l in filter(is_valid, gen_comb(a0)):
            yield n

def gen_diff(n):
    digits = list(gen_digits(n))
    for d in filter(lambda d: digits.count(d) >= 3, range(3)):
        for m in gen_mask(digits, d):
            yield m, d

def back_check(n, diff, d):
    for m in range(d):
        if not is_prime(n - diff * m):
            return False
    return True

def is_valid(n):
    if not is_prime(n):
        return False
    
    for diff, d0 in gen_diff(n):
        counter = 1
        for d in range(d0 + 1, 10):
            if is_prime(n + diff * (d - d0)):
                counter += 1
            elif counter == d - 2:
                break
        if counter == N:
            return back_check(n, diff, d0)
    
    return False

# generate m-digit numbers with l or more d
def gen_candidates_core(m, d0, l = 3, begin = 1):
    if m == 0:
        yield 0
    elif m == l:
        yield d0 * (10 ** l - 1) / 9
    else:
        for d in range(begin, 10):
            for n in gen_candidates_core(m - 1, d0, l - (d == d0), 0):
                yield d * 10 ** (m - 1) + n

def gen_candidates():
    for k in count(6):
        a = [ ]
        for d in range(3):
            a.extend(filter(is_valid, gen_candidates_core(k, d)))
        for n in sorted(a):
            yield n

def gen_candidates2(d):
    for k in count(6):
        for n in gen_candidates_core(k, d):
            yield n

def which_min(n0, n1, n2):
    if n0 < n1:
        min_n = n0
        flag = 1
    elif n0 > n1:
        min_n = n1
        flag = 2
    else:
        min_n = n0
        flag = 3
    
    if min_n > n2:
        flag = 4
    elif min_n == n2:
        flag |= 4
    
    return flag, min_n

def gen_candidates():
    g0 = gen_candidates2(0)
    g1 = gen_candidates2(1)
    g2 = gen_candidates2(2)
    n0 = next(g0)
    n1 = next(g1)
    n2 = next(g2)
    while True:
        flag, n = which_min(n0, n1, n2)
        yield n
        if flag & 1:
            n0 = next(g0)
        if flag & 2:
            n1 = next(g1)
        if flag & 4:
            n2 = next(g2)

N = 8
for n in islice(filter(is_valid, gen_candidates()), 1):
    print(n)