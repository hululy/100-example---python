# 输入一个奇数，然后判断最少几个9除于该数的结果为整数

def f(n):
    a = 9
    k = 1
    while True:
        if a % n == 0:
            break
        else:
            a = a * 10 + 9
            k += 1
    print('至少%d个9除于%d的结果为整数' % (k,n))

if __name__ == '__main__':
    num = int(input('请输入一个奇数:'))
    f(num)