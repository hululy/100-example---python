# 输入3个数a,b,c，按大小顺序输出

a = float(input('请输入第一个数字:'))
b = float(input('请输入第二个数字:'))
c = float(input('请输入第三个数字:'))

if a > b:
    if a > c:
        if b > c:
            print(a,' ',b,' ',c)
        else:
            print(a,' ',c,' ',b)
    else:
        print(c,' ',a,' ',b)
elif a > c:
    print(b,' ',a,' ',c)
elif a < c:
    if b > c:
        print(b,' ',c,' ',a)
    else:
        print(c,' ',b,' ',a)
