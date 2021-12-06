# 读取7个数（1—50）的整数值，每读取一个值，程序打印出该值个数的＊

import random

def random_print(n):
    for i in range(n):
        num = random.randint(1,50)
        print(num * '*')

if __name__ == '__main__':
    n = int(input('n = '))
    random_print(n)
