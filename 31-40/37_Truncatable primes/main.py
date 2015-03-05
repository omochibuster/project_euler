# -*- coding:utf-8 -*-
#answer is 748317(1.8秒) 2015/1/30

def ToList(number):
	list = []
	while number != 0:
		list.append(number % 10)
		number //= 10
	list.reverse()
	return list

def isPrime(number):
	if number == 2:
		return 2
	if number == 1 or number % 2 == 0:
		return 0
	end = (int)(math.sqrt(number))
	for num in list(range(3, end + 1, 2)):
		if number % num == 0:
			return 0
	return number

def ToNumber(numList):
	number = 0
	List = numList[:]
	while List != []:
		number = number * 10 + List.pop(0)
	return number

def ExistEvenNum(numList):
	num = numList[1:]
	for number in list(range(0,10,2)):
		if num.count(number) > 0:
			return 1
	return 0

import math, time

start = time.time()
answer = 0
count = 0

for number in list(range(11, 1000000,2)):
	numList = ToList(number)

	if ExistEvenNum(numList):
		continue
	rightTruncationNum = ToNumber(numList[:])

	while numList != []:
		if isPrime(rightTruncationNum) == 0 or isPrime(ToNumber(numList)) == 0:
			break
		rightTruncationNum //= 10
		numList.pop(0)
	else:
		print(number)
		answer += number
		count += 1
	if count == 11:
		break

print(answer)
end = time.time()
print(end - start, "秒")