# coding: utf-8

# オイラーのトーティエント関数 φ(n) (ファイ関数とも呼ばれる) とは, 
# n 未満の正の整数で n と互いに素なものの個数を表す. 
# 例えば, 1, 2, 4, 5, 7, 8 は9未満で9と互いに素であるので, φ(9) = 6 となる. 
# 1 は全ての正の整数と互いに素であるとみなされる. よって φ(1) = 1 である.
# 面白いことに, φ(87109)=79180 であり, 87109は79180を置換したものとなっている.
# 1 < n < 107 で φ(n) が n を置換したものになっているもののうち,
# n/φ(n) が最小となる n を求めよ.

from functools import reduce
import time

def sieve(max_n):
    a = list(range(max_n + 1))
    for p in filter(lambda n: a[n] == n, range(2, max_n // 2 + 1)):
        for k in filter(lambda k: a[k] == k, range(p * 2, max_n + 1, p)):
            a[k] = p
    return a

def div_pow(n, p):
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return n, e

def calc_phi(a):
    for n in range(2, len(a)):
        if a[n] == n:   # prime
            a[n] -= 1
        else:
            p = a[n]
            m, e = div_pow(n, p)
            a[n] = a[p] * p ** (e - 1) * a[m]
    return a

def gen_digits(n):
    while n:
        yield n % 10
        n //= 10

def is_permutation(m, n):
    def normalize(n):
        return reduce(lambda x, y: x * 10 + y,
                    sorted(gen_digits(n), key = lambda e: -e))
    return normalize(m) == normalize(n)

def min_f(x, y):
    return x if x[0] * y[1] <= x[1] * y[0] else y

N = 10 ** 7
phi = calc_phi(sieve(N))
#print(time.clock() - t)
g = filter(lambda n: is_permutation(n, phi[n]), range(2, N + 1))
print(reduce(min_f, map(lambda n: (n, phi[n]), g), (9, 1)))