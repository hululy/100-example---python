# 打印出杨辉三角形

import string

def YangHui (num=10):
    LL = [[1]]
    for i in range(1,num):
        LL.append([(0 if j == 0 else LL[i-1][j-1]) + (0 if j == len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
    return LL

Y = YangHui(num=10)

for i in Y:
    str_i = ' '.join(str(x) for x in i)
    tritangle_Y = str_i.center(26)
    print(tritangle_Y)
