#-*- coding:utf-8 -*-
#answer is 249 (0.2秒) 2015/2/3

from time import time

def toList(number):
	list = []
	while number != 0:
		list.append(number % 10)
		number //= 10
	return list

def add(list,list2):
	number = 0
	for index in range(len(list)):
		number = number * 10 + list[index] + list2[index]
	return number

def isLychrelNumber(number):
	for i in range(50):
		reverse = toList(number)
		nomal = reverse[:]
		nomal.reverse()
		number = add(nomal,reverse)
		if isPalindrome(number):
			return False
	return True

def isPalindrome(number):
	list = toList(number)
	revlist = list[:]
	revlist.reverse()
	for index in range(len(list)):
		if list[index] != revlist[index]:
			return False
	return True

start = time()
count = 0
for number in range(1, 10000):
	count += isLychrelNumber(number)

print(count)
end = time()
print(end - start,"秒")