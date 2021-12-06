# 求一个3*3矩阵主对角线元素之和

import numpy as np

arr_list = []

for i in range(9):
    num = float(input('请输入：'))
    arr_list.append(num)

arr = np.array(arr_list)
arr.resize([3,3])
sum = arr[0,0] + arr[1,1] + arr[2,2]
print('主对角线元素之和为:',sum)

