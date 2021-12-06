# 求0—7所能组成的n位数奇数个数

def odd_count(n):
    if n == 1:
        count = 0
        for i in range(0,8):
            if i % 2 != 0:
                if '8' not in str(i) and '9' not in str(i):
                    count += 1
        print('%d位数奇数个数为:%d' % (n,count))
    elif n == 2:
        count = 0
        for i in range(10,78):
            if i % 2 != 0:
                if '8' not in str(i) and '9' not in str(i):
                    count += 1
        print('%d位数奇数个数为:%d' % (n,count))
    elif n == 3:
        count = 0
        for i in range(100,778):
            if i % 2 != 0:
                if '8' not in str(i) and '9' not in str(i):
                    count += 1
        print('%d位数奇数个数为:%d' % (n,count))
    elif n == 4:
        count = 0
        for i in range(1000,7778):
            if i % 2 != 0:
                if '8' not in str(i) and '9' not in str(i):
                    count += 1
        print('%d位数奇数个数为:%d' % (n,count))
    elif n == 5:
        count = 0
        for i in range(10000,77778):
            if i % 2 != 0:
                if '8' not in str(i) and '9' not in str(i):
                    count += 1
        print('%d位数奇数个数为:%d' % (n,count))
    elif n == 6:
        count = 0
        for i in range(100000,777778):
            if i % 2 != 0:
                if '8' not in str(i) and '9' not in str(i):
                    count += 1
        print('%d位数奇数个数为:%d' % (n,count))
    elif n == 7:
        count = 0
        for i in range(1000000,7777778):
            if i % 2 != 0:
                if '8' not in str(i) and '9' not in str(i):
                    count += 1
        print('%d位数奇数个数为:%d' % (n,count))
    elif n == 8:
        count = 0
        for i in range(10000000,77777778):
            if i % 2 != 0:
                if '8' not in str(i) and '9' not in str(i):
                    count += 1
        print('%d位数奇数个数为:%d' % (n,count))

if __name__ == '__main__':
    num = int(input('输入位数:'))
    odd_count(num)


