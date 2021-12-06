# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数

str = input('请输入:')
letters = 0
space = 0
digit = 0
others = 0
for s in str:
    if s.isalpha():
        letters += 1
    elif s.isspace():
        space += 1
    elif s.isdigit():
        digit += 1
    else:
        others += 1
print('char=%d , space=%d , digit=%d , others=%d' % (letters,space,digit,others))
