# coding: utf-8

# nとdを正の整数として, 分数 n/d を考えよう. n<d かつ gcd(n,d)=1 のとき, 真既約分数と呼ぶ.
# d <= 8について既約分数を大きさ順に並べると, 以下を得る:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# 3/7のすぐ左の分数は2/5である.
# d <= 1,000,000について真既約分数を大きさ順に並べたとき, 3/7のすぐ左の分数の分子を求めよ.

from fractions import gcd
from time import time

start = time()
a = 3 / 7
b = 0
c = 0
d = []
end = 1000000

for i in range(2, end + 1):
	for j in range(int(i * b), int(i * a) + 1):
		if gcd(j, i) == 1 and b < j / i < a:
			b = j / i
			c = j
			d = [j, i]
print("answer = %d, numerator = %d, denominator = %d" % (c, d[0], d[1]))
stop = time()
print("実行時間: %f秒" % (stop - start))