#-*- coding:utf-8 -*-
#answer is  107359

from sys import stdout

b1 = 0
b2 = 0
b3 = 0
sum = 0
for words in open("cipher1.txt"):
	word = words.split(",")
	max1 = 0
	max2 = 0
	max3 = 0
	for a in range(26):
		count1 = 0
		count2 = 0
		count3 = 0
		for index in range(0,len(word)-3, 3):
			if (ord("a") + a) ^ int(word[index]) == ord(" "):
				count1 += 1
			if (ord("a") + a) ^ int(word[index + 1]) == ord(" "):
				count2 += 1
			if (ord("a") + a) ^ int(word[index + 2]) == ord(" "):
				count3 += 1
		if max1 <= count1:
			max1 = count1
			b1 = a
		if max2 <= count2:
			max2 = count2
			b2 = a
		if max3 <= count3:
			max3 = count3
			b3 = a
	for index in range(0,len(word) - 3,3):
		stdout.write(chr(ord("a") + b1 ^ int(word[index])))
		stdout.write(chr(ord("a") + b2 ^ int(word[index + 1])))
		stdout.write(chr(ord("a") + b3 ^ int(word[index + 2])))
		sum += (ord("a") + b1 ^ int(word[index]))
		sum += (ord("a") + b2 ^ int(word[index + 1]))
		sum += (ord("a") + b3 ^ int(word[index + 2]))
sum += (ord("a") + b1 ^ int(word[-1]))
print(sum)