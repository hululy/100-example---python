# 一个5位数，判断它是不是回文数。如12321是回文数，个位与万位相同，十位与千位相同

a = input('请输入一个5位数:')
b = a[::-1]

if a == b:
    print('%s是回文数' % a)
else:
    print('%s不是回文数' % b)

