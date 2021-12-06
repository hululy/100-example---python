# 打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身

print('水仙花数：')
for a in range(0,10):
    for b in range(0, 10):
        for c in range(0, 10):
            x = a ** 3 + b ** 3 + c ** 3
            y = 100 * a + 10 * b + c
            if x == y:
                if (100 <= x < 1000) and (100 <= y < 1000):
                    print(x)