# 一个数如果恰好等于它的因子之和，这个数就称为"完数",找出1000以内的完数

print('1000以内的所有完数:')
for i in range(1,1001):
    sum = 0
    for j in range(1,i):
        if i % j == 0:
            sum += j
    if sum == i:
        print(i)