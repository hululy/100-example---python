# 字符串日期转换为易读的日期格式

from dateutil import parser

dt1 = parser.parse('Aug 28 2015 12:00AM')
dt2 = parser.parse('8 28 2015 12:00AM')
dt3 = parser.parse('28 8 2015 12:00am')
dt4 = parser.parse('8.28.2015')
dt5 = parser.parse('8/28/2015')
dt6 = parser.parse('2015.8.28')
print(dt1)
print(dt2)
print(dt3)
print(dt4)
print(dt5)
print(dt6)