#-*- coding:utf-8 -*-
#answer is 972 (0.3秒) 2015/2/3

from time import time

def toList(number):
	list = []
	while number != 0:
		list.append(number % 10)
		number //= 10
	list.reverse()
	return list

def digitSum(list):
	sum = 0
	for index in range(len(list)):
		sum += list[index]
	return sum

start = time()
max = 0
for a in range(100):
	for b in range(100):
		number = a ** b
		sum = digitSum(toList(number))
		if max < sum:
			max = sum
print(max)
end = time()
print(end - start,"秒")