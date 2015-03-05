# -*-coding:utf-8-*-
#answer is 5777 (0.5秒) 2015/2/1

from math import sqrt
from time import time

def isPrime(number):
	if number == 2:
		return 1
	if number % 2 == 0:
		return 0
	for i in range(3,number,2):
		if number % i == 0:
			return 0
	return 1

def isNumberOfOddSynthesis(number):
	if not isPrime(number):
		if number % 2 == 1:
			return 1
	return 0

def calc(number):
	for i in range(1, number):
		if (number - 2 * (i ** 2)) <= 0:
			return 1
		if isPrime((number - 2 * (i ** 2))):
			return 0
	return 1


start = time()
for number in range(2, 100000):
	if isNumberOfOddSynthesis(number):
		if calc(number):
			print(number)
			break
end = time()
print(end - start,"秒")