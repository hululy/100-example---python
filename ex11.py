# 古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问第n个月兔子总数为多少？

def f(n):
    if n <= 2:
        return 1
    else:
        return f(n-1)+f(n-2)

num = int(input('请输入月数:'))
print('第%d个月兔子总数为%d对' % (num,f(num)))


