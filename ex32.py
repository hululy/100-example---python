# 按相反的顺序输出列表的值

list = ['snooker','ronnie','python','R']

# 方法一
for s in list[::-1]:
    print(s)

print('-----')

# 方法二
for i in range(3,-1,-1):
    print(list[i])