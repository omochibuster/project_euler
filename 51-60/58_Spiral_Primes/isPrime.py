from math import sqrt
def isPrime(number):
	if number == 0:return 0
	if number == 1:return 0
	if number == 2:return 1
	if number % 2 == 0:return 0
	end = int(sqrt(number)) + 1
	for i in range(3,end,2):
		if number % i == 0:return 0
	return 1