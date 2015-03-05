#-*-coding:utf-8-*-
#http://d.hatena.ne.jp/inamori/20100116/p1

from itertools import count, takewhile, islice
from math import sqrt

def is_prime(n):
    for p in filter(lambda p: p * p <= n, primes):
        if n % p == 0:
            return False
    return True

def prime(k):
    if k == len(primes):
        for n in islice(filter(is_prime, count(primes[-1] + 1)), 1):
            primes.append(n)
    return primes[k]

class conssecutive_primes:
    def __init__(self, k0):
        n = 0
        for k in takewhile(lambda k: n + prime(k) <= N, count(k0)):
            n += prime(k)
        self.k0 = k0
        self.n = n
        self.l = k - k0 + 1
    
    def next(self):
        n = self.n
        self.n -= prime(self.l-self.k0-1)
        self.l -= 1
        return n
    
    def length(self):
        return self.l

def gen_long_prime_sum():
    for l in range(glist[0].length(), 0, -1):
        for g in takewhile(lambda g: g.length() == l, glist):
            yield g.next()
        
        while glist[-1].length() >= l - 1:
            glist.append(conssecutive_primes(len(glist)))

N = 10 ** 6
primes = [ 2 ]
glist = [ conssecutive_primes(k) for k in range(3) ]
for n in islice(filter(is_prime, gen_long_prime_sum()), 1):
    print (n)
