# -*- coding:utf-8 -*-
#answer is 16695334890(4.4秒)2015/1/31

from itertools import permutations
from time import time

def toNumber(tapl):
	number = 0
	for x in range(0,len(tapl)):
		number = number * 10 + int(tapl[x])
	return number

def ableDividPrime(pandigital):
	if int(pandigital[1] + pandigital[2] + pandigital[3]) % 2 != 0:
		return 0
	if int(pandigital[2] + pandigital[3] + pandigital[4]) % 3 != 0:
		return 0
	if int(pandigital[3] + pandigital[4] + pandigital[5]) % 5 != 0:
		return 0
	if int(pandigital[4] + pandigital[5] + pandigital[6]) % 7 != 0:
		return 0
	if int(pandigital[5] + pandigital[6] + pandigital[7]) % 11 != 0:
		return 0
	if int(pandigital[6] + pandigital[7] + pandigital[8]) % 13 != 0:
		return 0
	if int(pandigital[7] + pandigital[8] + pandigital[9]) % 17 != 0:
		return 0
	return 1

start = time()
answer = 0
basedpandigital = [str(x) for x in range(0,10)]
pandigital = list(permutations(basedpandigital, 10))
for index in range(len(pandigital)):
	if ableDividPrime(pandigital[index]):
		answer += toNumber(pandigital[index])
print(answer)
end = time()
print(end - start,"秒")