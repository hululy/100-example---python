# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身

print('水仙花数：')
for n in range(100,1000):
    n_str = list(str(n))
    i = int(n_str[0])
    j = int(n_str[1])
    k = int(n_str[2])
    if n == i**3 + j**3 + k**3:
        print(n)
