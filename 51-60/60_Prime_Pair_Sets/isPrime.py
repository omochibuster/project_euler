from math import sqrt
def isPrime(number):
	if number == 0:return False
	if number == 1:return False
	if number == 2:return True
	if number % 2 == 0:return False
	end = int(sqrt(number)) + 1
	for i in range(3,end,2):
		if number % i == 0:return False
	return True