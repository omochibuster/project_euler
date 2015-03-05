# -*- coding:utf-8 -*-
# http://d.hatena.ne.jp/inamori/20091224/p1

from fractions import gcd
from functools import reduce

N = 10 ** 3 #求めるpの値
M = N // 2
a = [ 0 ] * (M + 1)
for l in range(1, M // 6 + 1):
    for m in range(2, int( (M // l) ** 0.5) + 1):
        begin = (m + 1) // 2 * 2 + 1         # odd
        end = min(m * 2, M // (l * m) + 1)
        for mn in range(begin, end, 2):
            if gcd(m, mn) == 1:
                k = l * m * mn
                a[k] += 1
print (reduce(lambda x, y: x if a[x] >= a[y] else y, range(M + 1)) * 2)