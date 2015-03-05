# coding:utf-8
# フィボナッチ数列の項は前の2つの項の和である.
# 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 数列の項の値が400万以下の, 偶数値の項の総和を求めよ.

max_num = 4000000
fibo_list = [1,2]

while(True):
    fibo_list.append(fibo_list[-2] + fibo_list[-1])
    if fibo_list[-1] > max_num:
        del fibo_list[-1]
        break;
even_fibo_list = [x for x in fibo_list if x % 2 == 0]

print('フィボナッチ数列:', fibo_list)
print('偶数だけ:', even_fibo_list)
print('総和:', sum(even_fibo_list))