# 求1+2!+3!+...+20!的和

from functools import reduce

n = 20
t = 1
Tn = []

for i in range(1,n+1):
    t = t * i
    Tn.append(t)

sum = reduce(lambda x,y: x+y, Tn)

print('1! + 2! + 3! + ... + 20! = %d' % sum)