from time import time

def nextTriangular():
	for n in range(287,1000000,2):
		yield n * (n + 1)

def nextPentagonal():
	for n in range(165,1000000):
		yield n * (3 * n - 1)

start = time()

triangular = 2
pentagonal = 3

while triangular != pentagonal:
	if triangular < pentagonal:
		for tri in nextTriangular():
			triangular = tri
			if triangular >= pentagonal:
				break
	else:
		for pen in nextPentagonal():
			pentagonal = pen
			if triangular <= pentagonal:
				break
	#print(triangular, pentagonal)
print(triangular // 2)

end = time()
print(end - start,"秒")