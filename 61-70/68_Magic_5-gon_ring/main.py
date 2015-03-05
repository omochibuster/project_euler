from itertools import permutations, combinations
from functools import reduce

def head(a):
    for e in a:
        return e

def gen_sum(a):
    yield a[0] + a[1] + a[2]
    for k in range(3, M - 1, 2):
        yield a[k] + a[k-1] + a[k+1]
    yield a[M-1] + a[M-2] + a[1]

def is_valid(a):
    g = gen_sum(a)
    n = next(g)
    return all(map(lambda m: m == n, g))

def is_on_inner_circle(k):
    return k == 1 or k % 2 == 0

def gen_perm(a = 0, k = 0, r0 = 0, start = 0):
    if k == M:
        yield ()
    if k == 0:
        a = list(range(M - 1, 0, -1)) + [ M ]
    for i in range(len(a)):
        n = a[i]
        if k == 0:
            r = N + 1 - n
            start = n
        else:
            r = r0
            if is_on_inner_circle(k):
                if n > start:
                    r -= 1
                    if r < 0:
                        continue
            else:
                if n < start:
                    continue
        for b in gen_perm(a[:i] + a[i+1:], k + 1, r, start):
            yield (n,) + b

def gen_solutions():
    for a in filter(is_valid, gen_perm()):
        yield a

def numerize(a):
    def g(a):
        yield a[0]
        yield a[1]
        for k in range(2, M, 2):
            yield a[k]
            yield a[k+1]
            yield a[k]
        yield a[1]
    
    return reduce(lambda x, y: x * (100 if y > 9 else 10) + y, g(a))

N = 5
M = N * 2
print(head(map(numerize, gen_solutions())))
