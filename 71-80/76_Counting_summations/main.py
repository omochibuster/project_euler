# coding:utf-8

# 5は数の和として6通りに書くことができる:
# 4 + 1
# 3 + 2
# 3 + 1 + 1
# 2 + 2 + 1
# 2 + 1 + 1 + 1
# 1 + 1 + 1 + 1 + 1
# 2つ以上の正整数の和としての100の表し方は何通りか.

memo = { }
def p(n, m1 = 0):
    m = n if m1 == 0 else min(n, m1)
    
    if n == 0:
        return 1
    elif (n, m) in memo:
        return memo[(n,m)]
    else:
        s = sum(p(n - d, d) for d in range(1, m + 1))
        memo[(n,m)] = s
        return s
        
print(p(100) - 1)