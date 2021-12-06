# 输出指定格式的日期

import datetime

if __name__ == '__main__':
    # 输出今日日期
    print(datetime.date.today().strftime('%Y-%m-%d'))
    # datetime.datetime.today().strftime('%Y-%m-%d %H:%M:%S')

    # 创建日期对象
    ronnie_birthday = datetime.date(1975,12,5)
    print(ronnie_birthday.strftime('%d/%m/%Y'))

    # 日期算术运算
    ronnie_birthday_nextday = ronnie_birthday + datetime.timedelta(days=1)
    print(ronnie_birthday_nextday.strftime('%d/%m/%Y'))

    # 日期替换
    ronnie_first_birthday = ronnie_birthday.replace(year=ronnie_birthday.year+1)
    print(ronnie_first_birthday.strftime('%d/%m/%Y'))

