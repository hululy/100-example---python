# 输入一个奇数，然后判断最少几个9除于该数的结果为整数

def f(n):
    for i in range(1,9):
        if (9 * int(i*'1')) % n == 0:
            print('至少%d个9除于%d的结果为整数' % (i,n))
            break

if __name__ == '__main__':
    num = int(input('请输入一个奇数:'))
    f(num)