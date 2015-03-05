#-*-coding:utf-8-*-
#answer is 9110846700 (0.03秒) 2015/2/1

from time import time

start = time()
sum = 0

for i in range(1,1001):
	sum = sum + i ** i
print(sum)

end = time()
print(end - start,"秒")