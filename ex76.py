# 写一个函数，输入n为偶数时，调用函数求1/2+1/4+...+1/n,当输入n为奇数时，调用函数1/1+1/3+...+1/n

from functools import reduce
from fractions import Fraction

def f_even():
    even = []
    for i in range(1,n+1):
        if i % 2 == 0:
            num = Fraction(1,i)
            even.append(num)
    sum = reduce(lambda x,y: x+y, even)
    print('1/2+1/4+...+1/n = {}'.format(sum))

def f_odd():
    odd = []
    for i in range(1,n+1):
        if i % 2 != 0:
            num = Fraction(1,i)
            odd.append(num)
    sum = reduce(lambda x,y:x+y, odd)
    print('1+1/3+...+1/n = {}'.format(sum))

def f(n):
    if n % 2 == 0:
        f_even()
    else:
        f_odd()

if __name__ == '__main__':
    n = int(input('n = '))
    f(n)