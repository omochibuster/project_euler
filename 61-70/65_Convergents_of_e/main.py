# -*- coding:utf-8 -*-
#answer is 272

def toList(number):
	list = []
	while number != 0:
		list.append(number % 10)
		number //= 10
	return list

convergent = 100
numerator = 0
denominator = 1

while convergent != 1:
	if convergent % 3 == 0:
		numerator += denominator * 2 * (convergent // 3)
	else:
		numerator += denominator
	#print(numerator, denominator)
	convergent -= 1
	numerator, denominator = denominator, numerator

numerator += denominator * 2

print(sum(toList(numerator)))