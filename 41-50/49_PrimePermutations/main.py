#-*-coding:utf-8-*-
#answer is 296962999629 2015/2/1

from itertools import permutations
from isPrime import isPrime

def toNumber(list):
	number = 0
	for i in range(len(list)):
		number = number * 10 + int(list[i])
	if number >= 1000 and number <= 9999:
		return number
	return 1

Tolerance = 3330
for strnum in range(2000,10000):
	count = 0
	answer = []
	a = list(permutations(str(strnum),4))
	for x in range(len(a)):
		if isPrime(toNumber(a[x])):
			if not(toNumber(a[x]) in answer):
				if answer != []:
					if answer[-1] + Tolerance == toNumber(a[x]):
						answer.append(toNumber(a[x]))
						count += 1
				else:
					answer.append(toNumber(a[x]))
					count += 1
	if count == 3:
		break
print(answer)