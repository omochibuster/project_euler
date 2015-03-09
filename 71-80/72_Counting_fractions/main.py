#coding: utf-8

# nとdを正の整数として, 分数 n/d を考えよう. n<d かつ HCF(n,d)=1 のとき,
# 真既約分数と呼ぶ.d <= 8について真既約分数を大きさ順に並べると, 以下を得る:
# 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
# この集合は21個の要素をもつことが分かる.
# d <= 1,000,000について, 真既約分数の集合は何個の要素を持つか?

import prime
from functools import reduce
from time import time

def primeFactorization(number, plist):
	list = [number]
	for i in plist:
		if number % i == 0:
			list.append(i)
			number //= i
			while number % i == 0:
				number //= i
			if number == 1:
				break
	return list

end = 1000000
ans = 0
p = prime.getPrime(2)
plist = [next(p)]
start = time()

for i in range(2, end + 1):
	if plist[-1] < i:
		plist.append(next(p))
	if i == plist[-1]:
		ans += i - 1
	else:
		ans += int(reduce(lambda x, y: x * (1 - 1 / y), primeFactorization(i, plist)))
print(ans)
end = time()
print(end - start)