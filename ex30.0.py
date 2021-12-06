# 一个5位数，判断它是不是回文数。如12321是回文数，个位与万位相同，十位与千位相同

num = input('请输入一个5位数：')

if (num[0] == num[-1]) and (num[1] == num[-2]):
    print('%s是回文数' % num)
else:
    print('%s不是回文数' % num)