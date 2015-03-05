# coding:utf-8
# 13195 の素因数は 5, 7, 13, 29 である.
# 600851475143 の素因数のうち最大のものを求めよ.

from math import sqrt

def devideN(number, factor):
	number //= factor
	while number % factor == 0:
		number //= factor;
	return number

num = N = 600851475143
maxFactor = 0

if num % 2 == 0:
	num = devideN(num, 2)

factor = 3
maxFactor = sqrt(num)

while num > 1 and factor <= maxFactor:
	if num % factor == 0:
		num = devideN(num, factor)
		maxFactor = sqrt(num)
	factor += 2

print(N, "の素因数の中で最大のものは", num, "です")