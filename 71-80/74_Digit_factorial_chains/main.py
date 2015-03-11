# coding: utf-8

# 145は各桁の階乗の和が145と自分自身に一致することで有名である.
# 1! + 4! + 5! = 1 + 24 + 120 = 145
# 169の性質はあまり知られていない. これは169に戻る数の中で最長の列を成す. 
# このように他の数を経て自分自身に戻るループは3つしか存在しない.
# 169 → 363601 → 1454 → 169
# 871 → 45361 → 871
# 872 → 45362 → 872
# どのような数からスタートしてもループに入ることが示せる.
# 例を見てみよう.
# 69 → 363600 → 1454 → 169 → 363601 (→ 1454)
# 78 → 45360 → 871 → 45361 (→ 871)
# 540 → 145 (→ 145)
# 69から始めた場合, 列は5つの循環しない項を持つ. 
# また100万未満の数から始めた場合最長の循環しない項は60個であることが知られている.
# 100万未満の数から開始する列の中で, 60個の循環しない項を持つものはいくつあるか?

from math import factorial
from time import time

def factorialEachDigit(n):
	d = n
	list = []
	while n != 0:
		list.append(n % 10)
		n //= 10
			
	c = sum(map(lambda x:factorial(x), list))
	if c == d:
		return 1
	return c

def a(n, count):
	if n in loop:
		b = loop.index(n)
		if b == 0:
			return count + 1
		elif b >= 4:
			return count + 2
		else:
			return count + 3
	else:
		return a(factorialEachDigit(n), count + 1)

start = time()
end = 1000000
N = 60
count = 0
loop = (1, 169, 36301, 1454, 871, 45361, 45362, 872)

for k in range(3, end):
	b = a(k, 0)
	if b == N:
		count += 1

print(count)
end = time()
print(end - start,"秒")