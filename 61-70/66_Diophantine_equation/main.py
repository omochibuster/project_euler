#-*-coding:utf-8 -*-
#http://blog.dreamshire.com/project-euler-66-solution/
from math import sqrt

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False] * ((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in range(1,n//2) if sieve[i]]

def pell(d):
    p, k, x1, y, sd = 1, 1, 1, 0, sqrt(d)
 
    while k != 1 or y == 0:
        p = k * (p//k+1) - p
        p = p - int((p - sd)//k) * k
 
        x = (p*x1 + d*y) // abs(k)
        y = (p*y + x1) // abs(k)
        k = (p*p - d) // k
        x1 = x
    return x
 
L = 1000
print("Project Euler 66 Solution:", max((pell(d),d) for d in prime_sieve(L)))