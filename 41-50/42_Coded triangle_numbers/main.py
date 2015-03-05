# -*- coding:utf-8 -*-
#answer is 162 (0.0秒) 2015/1/31

def getWord(listWord):
	for index in range(len(listWord)):
		yield listWord[index][1:-1]

def ToValue(word):
	value = 0
	for index in range(len(word)):
		value += ord(word[index]) - ord('@')
	return value

def getTriangleNumbers():
	return [number * (number + 1) // 2 for number in range(1, 30)]

from time import time

start = time()
count = 0
TriangleNumbers = getTriangleNumbers()
for words in open("words.txt", "r"):
	a = words.split(",")
	for word in getWord(a):
		if ToValue(word) in TriangleNumbers:
			count += 1
print(count)
end = time()
print(end - start,"秒")