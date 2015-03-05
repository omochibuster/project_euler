# -*- coding:utf-8 -*-
#answer is 7652413 (3秒)2015/1/31

from itertools import permutations
from math import sqrt
from time import time

def isPrime(number):
	if number % 2 == 0:
		return 0
	s = int(sqrt(number)) + 1
	for num in range(3,number):
		if number % num == 0:
			return 0
	return number

def toNumber(tapl):
	number = 0
	for x in range(0,len(tapl)):
		number = number * 10 + int(tapl[x])
	return number

def isPandigitalPrime(list):
	for x in range(len(list)):
		if isPrime(toNumber(list[x])) != 0:
			print(toNumber(list[x]))
			return 1
	return 0


start = time()
b = 0
pandigital = [str(x) for x in range(9,0,-1)]
for y in range(len(pandigital) , 0 , -1):
	a = list(permutations(pandigital, y))
	if isPandigitalPrime(a):
		break
	abc.pop(0)

end = time()
print(end - start,"秒")