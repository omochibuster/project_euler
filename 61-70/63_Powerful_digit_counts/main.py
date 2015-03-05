#-*- coding:utf-8 -*-
#answer is 49 2015/2/9

from math import log10, ceil

def toList(number):
	list = []
	while number != 0:
		list.append(number % 10)
		number //= 10
	return list

count = 0
for i in range(1,100):
	tmp = count
	for j in range(1,10):
		if len(toList(j ** i)) == i:
			count += 1
	if tmp == count:
		print(count)
		break