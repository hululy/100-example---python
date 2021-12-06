# 对10个数进行排序

list = []

for i in range(10):
    num = int(input('请输入数字：'))
    list.append(num)

list.sort()
print(list)