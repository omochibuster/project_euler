#coding:utf-8

# ある長さの鉄線を折り曲げて3辺の長さが整数の直角三角形を作るとき,
# その方法が1通りしかないような最短の鉄線の長さは12cmである. 他にも沢山の例が挙げられる.
# 12 cm: (3,4,5)
# 24 cm: (6,8,10)
# 30 cm: (5,12,13)
# 36 cm: (9,12,15)
# 40 cm: (8,15,17)
# 48 cm: (12,16,20)
# それとは対照的に, ある長さの鉄線 (例えば20cm) は3辺の長さが整数の
# 直角三角形に折り曲げることができない. また2つ以上の折り曲げ方があるものもある.
# 2つ以上ある例としては, 120cmの長さの鉄線を用いた場合で, 3通りの折り曲げ方がある.
# 120 cm: (30,40,50), (20,48,52), (24,45,51)
# Lを鉄線の長さとする. 直角三角形を作るときに1通りの折り曲げ方しか存在しないような
# L <= 1,500,000 の総数を答えよ.

from fractions import gcd
from time import time, clock
from math import sqrt

start = time()
t = clock()
L = 15 * 10 ** 5
M = L // 2
a = [ 0 ] * (M + 1)
for m in range(2, int(sqrt(M)) + 1):
    for n in range(m + 2 if m & 1 else m + 1, min(M // m + 1, m * 2), 2):
        if gcd(m, n) == 1:
            p = m * n
            for r in range(p, M, p):
                a[r] += 1

print(sum(map(lambda n: a[n] == 1, range(M + 1))))
end = time()
print(end - start)