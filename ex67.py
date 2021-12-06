# 输入数列，最大的与第一个元素交换，最小的与最后一个元素交换，输出数列

L = []

for i in range(5):
    num = int(input('请输入数字:'))
    L.append(num)

print(L)

max_index = L.index(max(L))
min_index = L.index(min(L))

L[0],L[max_index] = L[max_index],L[0]
L[-1],L[min_index] = L[min_index],L[-1]

print(L)
