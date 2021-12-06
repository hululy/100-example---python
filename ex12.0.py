# 判断101-200之间有多少个素数，并输出所有素数

zs = []

for i in range(101,201):
    if i%2 != 0 and  i%3 != 0 and  i%5 != 0 and  i%7 != 0 and  i%11 != 0 and  i%13 != 0:
        zs.append(i)
        
print(zs,'\n共%d个' % len(zs))
