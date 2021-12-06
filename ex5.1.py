# 输入任意个整数，请从小到大输出这些数

'''
for i in list:

'''
list = []
while True:
    i = input('请输入：')
    if i != 'q':
        list.append(int(i))
    else:
        break
list.sort()
print(list)

