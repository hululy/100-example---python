# 利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来

def output(s,l):
    if l == 0:
        return
    else:
        print(s[l-1])
        output(s,l-1)

s = input('请输入5个字符:')
l = len(s)
output(s,l)
