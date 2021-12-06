# 利用递归方法求5!

def factorial(n):
    if  n == 1:
        fn = 1
    else:
        fn = factorial(n-1) * n
    return fn

print('5! = %d' % factorial(5))