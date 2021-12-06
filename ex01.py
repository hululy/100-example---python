# 有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？
list = list(range(1,5))
for i in list:
    for j in list:
        for k in list:
            if i != j and i != k and j != k:
                print(int(str(i)+str(j)+str(k)))