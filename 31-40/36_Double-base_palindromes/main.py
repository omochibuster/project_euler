# -*- coding: utf-8 -*-
#answer is 872198 (0.03•b) 2015/1/29

def NextBinaryPalindromes(numbers):
	if IsMaxDigit(numbers):
		numbers.append(1)
		BothEndsOnlyOne(numbers)
	else:
		if len(numbers) % 2 == 0:
			right = len(numbers) // 2
			left = right - 1
		else:
			right = left = len(numbers) // 2
		while numbers[right] != 0:
			right += 1
			left -= 1
		numbers[right] = numbers[left] = 1
		right -= 1
		left += 1
		while left <= right:
			numbers[right] = numbers[left] = 0
			right -= 1
			left += 1

def IsMaxDigit(numbers):
	return numbers.count(1) == len(numbers)

#‰ü‘P‚Ì—]’n‚ ‚è?
def BothEndsOnlyOne(numbers):
	for x in list(range(len(numbers) - 2)):
		numbers[x + 1] = 0

def ChangeDecimal(numbers):
	number = 0
	for digit in list(range(len(numbers))):
		if numbers[digit] == 1:
			number += 2 ** digit
	return number

def isPalindrome(number):
	listNumber = []
	temp = number
	while temp != 0:
		listNumber.append(temp % 10)
		temp //= 10
	reverse = listNumber[:]
	reverse.reverse()
#	print(reverse , listNumber, number)
	for digit in list(range(len(listNumber))):
		if listNumber[digit] != reverse[digit]:
			return 0
	return number

import time
import sys

start = time.time()
numbers = []
number = 0
answer = 0
while number <= 1000000:
	NextBinaryPalindromes(numbers)
	number = ChangeDecimal(numbers)
	if number >= 1000000:
		break
	answer += isPalindrome(number)
print(answer)
end = time.time()
print(end - start)
a = sys.stdin.readline()