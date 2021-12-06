# 求1+2!+3!+...+20!的和

from functools import reduce

n = 20
Sn = []

def factorial(n):
    if  n == 1:
        fn = 1
    else:
        fn = factorial(n-1) * n
    return fn

for i in range(1,n+1):
    Sn.append(factorial(i))

sum = reduce(lambda x,y: x+y, Sn)
print('1! + 2! + 3! + ... + 20! = %d' % sum)

