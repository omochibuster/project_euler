from itertools import filterfalse, takewhile, count, islice

def all(f, a):
    for e in filterfalse(f, a):
        return False
    return True

def is_prime(n):
    b = all(lambda p: n % p != 0, takewhile(lambda p: p * p <= n, primes))
    if b:
        p = primes[-1]
        while p * p < n:
            p = next_prime()
            if n % p == 0:
                return False
        return True
    else:
        return False

def next_prime():
    for n in filter(is_prime, count(primes[-1] + 1)):
        primes.append(n)
        return n

def prime(k):
    if k < len(primes):
        return primes[k]
    else:
        return next_prime()

def cat(p, q):
    n = 10
    while q > n:
        n *= 10
    return p * n + q

def is_cat_prime(p, q):
    return is_prime(cat(p, q)) and is_prime(cat(q, p))

def is_all_pair(p, g):
    return (g[-1], p) in prime_groups[2] \
                and g[:-1] + (p,) in prime_groups[len(g)]

# n-prime group
def calc_prime_group(n, m):
    p = prime(m)
    if n == 2:
        for g in [ (q, p) for q in filter(lambda q: is_cat_prime(q, p),
                                    takewhile(lambda q: q < p, primes)) ]:
            prime_groups[2].add(g)
    else:
        calc_prime_group(n - 1, m)
        for g in map(lambda g: g + (p,),
                filter(lambda g: is_all_pair(p, g), prime_groups[n-1])):
            prime_groups[n].add(g)

N = 5
primes = [ 2 ]
prime_groups = [ set() for k in range(N + 1) ]
for m in count(1):
    calc_prime_group(N, m)
    if len(prime_groups[N]):
        for g in prime_groups[N]:
            min_sum = sum(g)
            print(g, min_sum)
        break

b = list(prime_groups[N-1])
b.sort(key = lambda e: sum(e))
while prime(m) < min_sum:
    p = primes[m]
    for e in takewhile(lambda e: sum(e) < min_sum - p, b):
        if all(lambda q: is_cat_prime(p, q), e):
            min_sum = sum(e) + p
            print (e + (p,), min_sum)
    m += 1
print(min_sum)