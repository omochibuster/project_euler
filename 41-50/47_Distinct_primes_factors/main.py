#-*-coding:utf-8-*-
#answer is 134043(83.5秒) 2015/2/1

from time import time

def isPrime(number):
	if number == 2:return 1
	if number % 2 == 0:return 0
	for i in range(3,number,2):
		if number % i == 0:return 0
	return 1

def getPrimeFactors(number):
	global NUMBER
	primeFactorsList = []
	if number % 2 == 0:
		primeFactorsList.append(2)
	while number % 2 == 0:number //= 2

	for x in range(3,number,2):
		if number % x == 0:
			primeFactorsList.append(x)
			if len(primeFactorsList) > NUMBER:
				return []
			number //= x
		while number % x == 0:
			number //= x
		if number == 1:
			break
	return primeFactorsList

start = time()
NUMBER = 4
x = 2

while x < 134099:
	for i in range(3, -1, -1):
		if isPrime(x + i):
			x += i + 1
			continue
	for i in range(3, -1, -1):
		if len(getPrimeFactors(x + i)) != NUMBER:
			x += i + 1
			break
	else:
		print(x)
		break

end = time()
print(end - start,"秒")