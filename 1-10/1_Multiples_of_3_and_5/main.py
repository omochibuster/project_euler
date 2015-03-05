# coding:utf-8

# 10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは 
# 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.
# 同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ

def SumDivisibleBy(n):
	p = END // n
	return n * (p * (p + 1)) // 2

END = 999 #999以下
N = 3 #3の倍数
M = 5 #5の倍数

sum =	SumDivisibleBy(N) + SumDivisibleBy(M) - SumDivisibleBy(N * M)
print(sum)