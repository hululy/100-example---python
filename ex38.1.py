# 求一个3*3矩阵主对角线元素之和

if __name__ == '__main__':
    a = []
    for i in range(3):
        a.append([])
        for j in range(3):
            a[i].append(float(input('请输入:')))
    for i in range(3):
        sum = 0
        sum += a[i][i]
    print('主对角线元素之和为:',sum)