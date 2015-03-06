# coding: utf-8

# オイラーのトーティエント関数 φ(n) (ファイ関数とも呼ばれる) とは, 
# n 未満の正の整数で n と互いに素なものの個数を表す. 
# 例えば, 1, 2, 4, 5, 7, 8 は9未満で9と互いに素であるので, φ(9) = 6 となる. 
# 1 は全ての正の整数と互いに素であるとみなされる. よって φ(1) = 1 である.
# 面白いことに, φ(87109)=79180 であり, 87109は79180を置換したものとなっている.
# 1 < n < 107 で φ(n) が n を置換したものになっているもののうち,
# n/φ(n) が最小となる n を求めよ.

from fractions import gcd
from prime import getPrime
from math import sqrt
from itertools import combinations

"""
	ｎとφ(n)が置換かどうかはのコードはまだ作成していない
"""

a = getPrime()
primeList = [next(a)]
for i in range(2, 10000000):
	if i >= primeList[-1]:
		primeList.append(next(a))
	count = 1
	pl = [primeList[x] for x in range(len(primeList)) if i % primeList[x] == 0]
	# iの中で互いに素でないものの数を数える
	for j in range(1, len(pl) + 1):
		for k in combinations(pl, j):
			multi = 1
			for l in range(len(k)):
				multi *= k[l]
			if len(k) % 2 == 1:
				count += (i - 1) // multi
			else:
				count -= (i - 1) // multi
	print(i, i - count)