# 有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

import random
from collections import deque

n = int(input('n = '))
m = int(input('m = '))
L = []

def move_num(n,m):
    for i in range(n):
        num = random.randint(1,100)
        L.append(num)
    print('原列表:\n',L)
    L_deque = deque(L)
    L_deque.rotate(m)
    print('向后移%d个位置:\n' % m,L_deque)

move_num(n,m)