# 八进制转换为十进制

def f8to10(num):
    print('八进制数:',num)
    l = str(num)
    length = len(l)
    sum = 0
    for i in range(length):
        sum += int(l[length-1-i]) * pow(8,i)
    print('转十进制数为:',sum)

if __name__ == '__main__':
    n = input('input a octal number:\n')
    f8to10(n)
