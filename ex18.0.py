# 求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制

n = int(input('请输入n的值:'))
a = input('请输入a的值:')
sum = 0
for i in range(1,n+1):
    sum = sum + int(a * i)
print('和为:',sum)
