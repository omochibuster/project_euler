from math import sqrt

def isPrime(number = 1):
	if number <= 1:return False
	if number == 2:return True
	if number % 2 == 0:return False

	end = int(sqrt(number)) + 1
	for i in range(3, end, 2):
		if number % i == 0:return False
	return True

def getPrimeList(end = 100):
	primeList = [number for number in range(2, end + 1) if isPrime(number)]
	return primeList

def getPrime(number = 2):
	for i in range(2, 10000000):
		if isPrime(i):
			yield i

if __name__ == '__main__':
	print(getPrimeList(100))