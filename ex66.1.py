# 输入3个数a,b,c，按大小顺序输出

L = []

for i in range(3):
    num = float(input('请输入一个数字:'))
    L.append(num)

for i in range(3):
    for j in range(i+1,3):
        if L[i] < L[j]:
            L[i],L[j] = L[j],L[i]

print(L)