# 输入某年某月某日，判断这一天是这一年的哪一天
# 置闰法则：四年一闰；百年不闰，四百年再闰

year = int(input('year: '))
month = int(input('month: '))
day = int(input('day: '))

months = [0,31,59,90,120,151,181,212,243,273,304,334]
if 0 < month <= 12:
    sum = months[month-1]
else:
    print('date error!')

sum = sum + day
leap = 0
if ((year%4 == 0) and (year%100 != 0)) or (year%400 == 0):
    leap = 1
if leap==1 and month > 2:
    sum += 1
print('it is the %ith day.' % sum)