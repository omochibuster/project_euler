#-*- coding:utf-8 -*-
#answer is 127035954683 2015/2/8

from math import ceil,log10
from itertools import permutations

def getNDigitCubicNumber(digit = 1):
	cubic = []
	for i in range(1,10000000):
		if int(log10(i ** 3)) + 1 == digit:
			cubic.append(i ** 3)
		elif log10(i ** 3) + 1 > digit:
			break
	return cubic

def toList(number):
	list = []
	while number != 0:
		list.append(number % 10)
		number //= 10
	return list

def isNumberOfReplacement(list):
	aaa = list[:]
	bbb = []
	for i in map(toList,aaa):
		bbb.append(i)
	for i in range(len(bbb)):
		bbb[i].sort()
	for i in range(len(bbb)):
		answer = 1
		for j in range(i + 1, len(bbb)):
			for k in range(len(bbb[0])):
				if bbb[i][k] != bbb[j][k]:
					break
			else:
				answer += 1
				if answer == N:
					return aaa[i]

N = 5

for digit in range(1, 13):
	digitCubic = getNDigitCubicNumber(digit)
	a = isNumberOfReplacement(digitCubic)
	if a:
		print(a)
		break
