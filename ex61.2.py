# 打印出杨辉三角形

import string

a = []

for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)

for i in range(10):
    a[i][0] = 1
    a[i][i] = 1

for i in range(2,10):
    for j in range(1,i):
        a[i][j] = a[i-1][j-1] + a[i-1][j]

for i in range(9):
    for j in range(9-i):
        if 0 in a[i]:
            a[i].pop()

for a_i in a:
    str_a = ' '.join(str(x) for x in a_i)
    tritangle_a = str_a.center(26)
    print(tritangle_a)




