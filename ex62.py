# 查找字符串

str1 = 'snooker'

print(str1.find('o'))
print(str1.find('t'))   # 不存在则返回-1

print(str1.index('o'))
print(str1.index('t'))   # 不存在则抛出异常
