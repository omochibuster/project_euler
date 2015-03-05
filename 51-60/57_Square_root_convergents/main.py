#-*- coding:utf-8 -*-
#answer is 153 2015/2/3

from time import time

def countDigit(number):
	list = []
	while number != 0:
		list.append(number % 10)
		number //= 10
	return len(list)

def harf():
	dominator = 2
	numerator = 1
	count = 0
	for x in range(1000):
		if x % 2 == 0:
			numerator += dominator
		else:
			dominator += numerator
		if countDigit(numerator) > countDigit(dominator) or countDigit(numerator) < countDigit(dominator):
			count += 1
		if x % 2 == 0:
			numerator += dominator
		else:
			dominator += numerator
	return count

start = time()
print(harf())
end = time()
print(end - start,"秒")