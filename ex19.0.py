# 一个数如果恰好等于它的因子之和，这个数就称为"完数",找出1000以内的完数

from functools import reduce

print('1000以内的完数:')

Sn = []
sum = 0
for i in range(1,1001):
    for j in range(1,i):
        Sn.append(j)
        sum = reduce(lambda x,y: x+y ,Sn)
    if sum == i:
        print(i)
