# 数字比较

def compare(num1,num2):
    if a > b:
        print('%d大于%d' % (a,b))
    elif a < b:
        print('%d小于%d' % (a,b))
    elif a == b:
        print('%d等于%d' % (a, b))
        
if __name__ == '__main__':
    a = int(input('输入第一个数字:'))
    b = int(input('输入第二个数字:'))
    compare(a,b)