from math import sqrt

limit = 1000000
sieveLimit = (int(sqrt(limit)) - 1) // 2
maxIndex = (limit - 1) // 2
cache = [0 for i in range(maxIndex + 1)]
for n in range(1, sieveLimit):
	if cache[n] == 0: # 2*n + 1 is prime
		p = 2 * n + 1
		for k in range(2 * n * (n + 1), maxIndex + 1, p):
			if cache[k] == 0:cache[k] = p
			
multiplier = 1
while multiplier <= limit:
	multiplier *= 2
multiplier //= 2
fractionCount = multiplier - 1 # powers of 2
multiplier //= 2
stepIndex = ((limit // multiplier) + 1) // 2

for n in range(1, maxIndex + 1):
	if n == stepIndex:
		multiplier //= 2
		stepIndex = ((limit // multiplier) + 1) // 2
	if cache[n] == 0:
		cache[n] = 2 * n
		fractionCount = fractionCount + multiplier * cache[n]
	else:
		p = cache[n]
		cofactor = (2 * n + 1) // p
		if cofactor % p == 0:
			factor = p 
		else:
			factor = p - 1
		cache[n] = factor * cache[cofactor // 2]
		fractionCount = fractionCount + multiplier * cache[n]
print(fractionCount)