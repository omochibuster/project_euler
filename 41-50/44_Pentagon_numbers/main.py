# -*- coding:utf-8 -*-
#answer is 5482660 2015/2/1
#http://d.hatena.ne.jp/inamori/20100105/p1

from itertools import takewhile, count
from math import sqrt
import time

def is_pentagonal(n):
    p = 1 + 24 * n
    q = int(sqrt(p))
    return q * q == p and q % 6 == 5

def P(n):
    return n * (3 * n - 1) / 2

def gen_prime_candidates():
    yield 2
    yield 3
    n = 5
    while True:
        yield n
        yield n + 2
        n += 6

def index(f, p):
    for k in range(len(f)):
        if f[k][0] == p:
            return k
    return -1

def pop_p(f, p):
    k = index(f, p)
    if k == -1:
        return f, 0
    else:
        return f[:k] + f[k+1:], f[k][1]

def calc_exp(n, p):
    e = 0
    while n % p == 0:
        e += 1
        n /= p
    return e, n

def factorize(n):
    f = ()
    for p in takewhile(lambda p: p * p <= n, gen_prime_candidates()):
        e, n = calc_exp(n, p)
        if e:
            f = f + ( (p, e),)
    
    if n > 1:
        f = f + ( (n, 1),)
    return f

def gen_divisors(f, k = 0):
    if k == len(f):
        yield 1, 1
    else:
        p, e0 = f[k]
        for d1, d2 in gen_divisors(f, k + 1):
            for e in range(e0 + 1):
                yield d1 * p ** e, d2 * p ** (e0 - e)

def gen_divs(l):
    f = factorize(l) + factorize(3 * l - 1) # coprime
    f, e2 = pop_p(f, 2)
    f, e3 = pop_p(f, 3)
    n2 = 2 ** e2
    n3 = 3 ** e3
    for d1, d2 in gen_divisors(f):
        if e2 == 0:
            yield n3 * d1, d2
        else:
            yield n2 * n3 * d1, d2
            yield n3 * d1, n2 * d2

def solve():
    for l in count(1):
        for d1, d2 in gen_divs(l):
            if d1 * 3 < d2 and d2 % 3 == 2:
                d3 = (d2 + 1) / 3
                n = (d1 + d3) / 2
                m = d3 - n
                if is_pentagonal(P(n) + P(m)):
                    return P(l)

t = time.clock()
print (solve())
print (time.clock() - t)