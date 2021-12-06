# 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位

from collections import deque

a = []
n = int(input('请输入人数:'))   # n大于1

for i in range(1,+n+1):
    a.append(i)

b = deque(a)

if n == 2:
    print('最后剩的人是%d号' % b[1])
    quit()

while True:
    b.remove(b[2])
    b.rotate(-2)
    if len(b) == 2 :
        print('最后剩的人是%d号' % b[1])
        break



