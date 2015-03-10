﻿# coding: utf-8

#nとdを正の整数として, 分数 n/d を考えよう. n<d かつ HCF(n,d)=1 のとき,
# 真既約分数と呼ぶ.d <= 8 について既約分数を大きさ順に並べると, 以下を得る:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# 1/3と1/2の間には3つの分数が存在することが分かる.
# では, d <= 12,000 について真既約分数をソートした集合では, 1/3 と 1/2 の間に何個の分数があるか?

from fractions import gcd

def primeFactorization(number):
	list = []
	for i in range(2, number):
		if number % i == 0:
			list.append(i)
			number //= i
			while number % i == 0:
				number //= i

end = 12000
ans = 0

for i in range(4, end + 1):
	l = [x for x in range(1, i)]
	for j in range(i // 3 + 1, i // 2 + 1):
		if gcd(i, j) == 1:
			ans += 1
			print("%d/%d" % (j , i))
print(ans)