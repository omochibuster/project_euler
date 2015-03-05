from itertools import combinations
from time import time
#-*- coding:uft-8 -*-
#answer is 4075 (0.0秒)2015/2/3

def overOneHundredinList(list):
	count = 0
	for index in range(len(list)):
		if list[index] >= 1000000:
			count +=1
	return count

#パスカルの三角形を用いる
start = time()
count = 0
list = [1,1]

for n in range(2, 101):
	list = [list[index] + list[index + 1] for index in range(len(list) - 1)]
	list.append(1)
	list.insert(0,1)
	count += overOneHundredinList(list)
print(count)

end = time()
print(end - start,"秒")