# 八进制转换为十进制

def f8to10(num8):
    print('八进制数:',num8)
    num10 = int(num8, base=8)
    print('转十进制数为:',num10)

if __name__ == '__main__':
    n = input('input a octal number:\n')
    f8to10(n)




