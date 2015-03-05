#-*- coding:utf-8 -*-
#(510510) 2015/3/4

import prime

if __name__ == "__main__":
	N = 1000000
	answer = 1
	for i in range(1, N):
		if prime.isPrime(i):
			answer *= i
			if answer >= N:
				answer //= i
				break
	print(answer)