# -*- coding:utf-8 -*-
#answer is 932718654(0.06秒) 2015/1/30

def EachDigitToList(number):
	list = []
	while number != 0:
		list.append(number % 10)
		number //= 10
	list.reverse()
	return list

def IsPandigital(digitList):
	for num in list(range(1, 10)):
		if digitList.count(num) != 1:
			return 0
	return 1

def ToValue(digitList):
	number = 0
	while digitList != []:
		number = number * 10 + digitList.pop(0)
	return number

import time

start = time.time()
answer = 0
for number in list(range(1,10000)):
	digitList = []
	for multipliedNum in list(range(1, 10)):
		digitList += EachDigitToList(number * multipliedNum)
		if len(digitList) >= 9:
			break
	if len(digitList) == 9:
		if IsPandigital(digitList):
			num = ToValue(digitList)
			if answer < num:
				answer = num

print(answer)
end = time.time()
print(end - start,"秒")