#-*- coding:utf-8 -*-
#answer is 28684 (PyPy 1.1秒) 2015/2/6

from polygonalNumber import (triangleNumber, squareNumber, pentagonalNumber, 
									 hexagonalNumber, heptagonalNumber, octagonalNumber)
from math import log10
from itertools import permutations
from time import time

def digitpolygonalNumber():
	for x in range(1,1000):
		return int(log10(triangleNumber(x))) + 1

def isCyclicNumber(function, number):
	for i in range(1, 1000):
		if int(log10(function(i))) + 1 == DIGIT:
			if function(i) // 100 == number % 100:
				yield function(i)

start = time()
DIGIT = (4)
dic = {0:triangleNumber, 1:squareNumber, 2:pentagonalNumber,
			3:hexagonalNumber, 4:heptagonalNumber, 5:octagonalNumber}

for permutation in permutations(range(6), 6):
	list = [dic[permutation[0]](x) for x in range(1, 1000) if int(log10(dic[permutation[0]](x))) + 1 == DIGIT]
	for j in range(len(permutation)):
		answer = [list[j]]
		for k in range(1, 6):
			for m in isCyclicNumber(dic[permutation[k]], answer[-1]):
				answer.append(m)
				if answer[0] // 100 == answer[-1] % 100:
					if len(answer) == 6:
						print(sum(answer))
				break

end = time()
print(end - start,"秒")