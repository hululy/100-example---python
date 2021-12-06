# 求0—7所能组成的n位数以内的奇数个数

def f(n):
    if n == 0:
        return 1
    elif n == 1:
        return 7
    else:
        return f(n-1)*8

def odd_count(n):
    l = []
    for i in range(1, n+1):
        l.append(f(i - 1) * 4)
    print(l)
    print(sum(l))

if __name__ == '__main__':
    num = int(input('输入位数:'))
    odd_count(num)