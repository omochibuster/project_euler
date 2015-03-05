#-*- coding:utf-8 -*-
#answer is 142857 (0.06秒) 2015/2/3

from time import time

def toList(number):
	dividedDigitList = []
	while number != 0:
		dividedDigitList.insert(0, number % 10)
		number //= 10
	return dividedDigitList

def sameNumberInList(a,b):
	if len(a) != len(b):
		return 0
	for index in range(len(a)):
		if a[index] not in b:
			return 0
	return 1

start = time()

number = 1
while number <= 10000000:
	if toList(number)[0] >= 2:#最初の桁が2以上だと桁上がりして同じ値を含まなくなる
		number = number + (10 ** (len(toList(number))- 1)) * 8
		continue
	for multiple in range(2,7):
		if not sameNumberInList(toList(number),toList(number * multiple)):
			break
	else:
		print(number)
		break
	number += 1

end = time()
print(end - start, "秒")