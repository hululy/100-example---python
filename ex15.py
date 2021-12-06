# 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示

def grade():
    n = int(input('请输入分数:'))
    if n < 60:
        print('{}分的等级为C'.format(n))
    elif 60 <= n <= 89:
        print('{}分的等级为B'.format(n))
    elif n >= 90:
        print('{}分的等级为A'.format(n))

grade()