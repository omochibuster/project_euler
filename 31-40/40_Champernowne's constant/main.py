# -*- coding:utf-8 -*-
#http://d.hatena.ne.jp/inamori/20091228/p1
#2015/1/31

def calc_digit(n):
    k = 0
    m = n
    while m > 0:
        k += 1
        m -= k * 9 * 10 ** (k - 1)
    
    m += k * 9 * 10 ** (k - 1)
    if m == 0:
        return 9
    p = 10 ** (k - 1) + (m - 1) // k # number
    q = (m - 1) % k + 1             # position
    return p // 10 ** (k - q) % 10



from functools import reduce

N = 6
print(reduce(lambda x, y: x * calc_digit(10 ** y), range(N + 1), 1))