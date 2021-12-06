# 请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母

s1 = input('请输入第一个字母:')
while True:
    if s1.upper() == 'M':
        print('星期一')
        break
    elif s1.upper() == 'W':
        print('星期三')
        break
    elif s1.upper() == 'T':
        s2 = input('请输入第二个字母:')
        if s2.lower() == 'u':
            print('星期二')
        elif s2.lower() == 'h':
            print('星期四')
        else:
            print('输入错误！')
        break
    elif s1.upper() == 'S':
        s2 = input('请输入第二个字母:')
        if s2.lower() == 'a':
            print('星期六')
        elif s2.lower() == 'u':
            print('星期日')
        else:
            print('输入错误！')
        break
    else:
        print('输入错误！')
    break