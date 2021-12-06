# 输出前n项斐波那契数列

fib_list = []
def fib(n):
    for i in range(n):
        if i == 0:
            fib_list.append(0)
        elif i == 1:
            fib_list.append(1)
        elif i == 2:
            fib_list.append(1)
        else:
            f = fib_list[i-1] + fib_list[i-2]
            fib_list.append(f)
    print(fib_list)

n = int(input('请输入要查询的斐波那契数列项数：'))
fib(n)
