# 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和

Fn = []
sum = 0
for i in range(21):
    if i == 0:
        Fn.append(1)
    elif i == 1:
        Fn.append(2)
    else:
        f = Fn[i-1] + Fn[i-2]
        Fn.append(f)

F1 = Fn[0:20]
F2 = Fn[1:21]

for j in range(20):
    f_div = F2[j] / F1[j]
    sum = sum + f_div

print('前20项和为:',sum)

