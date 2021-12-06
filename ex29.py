# 给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字

s = input('请输入:')
l = len(s)

def output(s,l):
    if l == 0:
        return
    s = str(s)
    print(s[l-1])
    output(s,l-1)

print('它是%d位数' % l)
output(s,l)