# 使用lambda来创建匿名函数

h = lambda x,y: x//y
x,y = eval(input('请输入两个数，用逗号隔开:'))
print(h(x,y))