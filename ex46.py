# 求输入数字的平方，如果平方运算后小于50则退出

while True:
    num = int(input('请输入一个数字:'))
    num_2 = num**2
    if num_2 >= 50:
        print('%d的平方等于%d' % (num,num_2))
    else:
        print('终止运行！')
        break
