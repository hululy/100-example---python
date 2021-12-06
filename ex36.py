# 求100之内的素数

from math import sqrt

def prime_number(n):
    s = []
    leap = 1
    for i in range(2, n + 1):
        k = int(sqrt(i + 1))
        for j in range(2, k + 1):
            if i % j == 0:
                leap = 0
                break
        if leap == 1:
            s.append(i)
        leap = 1
    print('{}以内的素数:{}'.format(n,s))

if __name__ == '__main__':
    n = int(input('n = '))
    prime_number(n)


