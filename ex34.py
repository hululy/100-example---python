# 练习函数调用。使用函数，输出三次snooker字符串

def f():
    print('snooker')

def g():
    for i in range(3):
        f()

if __name__ == '__main__':
    g()