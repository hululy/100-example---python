# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

import random

n = int(input('n = '))
m = int(input('m = '))
L1 = []
L2 = []

def move_num(n,m):
    for i in range(n):
        num = random.randint(1,100)
        L1.append(num)
    print('原列表:\n',L1)
    for i in range(m):
        l2 = L1.pop()
        L2.insert(0,l2)
    L = L2 + L1
    print('向后移%d个位置:\n' % m, L)

move_num(n,m)

