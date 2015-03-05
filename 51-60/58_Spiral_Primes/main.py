from isPrime import isPrime

primeCount = 0
diagonalCount = 0
average = 100.0
diagonalNumber = 1
addNum = 2
while not average <= 0.1:
	for x in range(4):
		diagonalNumber += addNum
		if isPrime(diagonalNumber):
			primeCount += 1
		diagonalCount += 1
		average = primeCount / diagonalCount
		if average <= 0.1:
			break
	addNum += 2
print(addNum - 2 + 1)