# 输出第n项斐波那契数列

def fib(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1)+fib(n-2)

n = int(input('请输入要查询的项：'))
print('第%d项斐波那契数列的值为%d' % (n,fib(n)))