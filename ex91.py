# 时间函数举例1

import time

if __name__ == '__main__':
    print(time.ctime(time.time()))
    print(time.asctime(time.localtime()))
    print(time.asctime(time.localtime(time.time())))
    print(time.asctime(time.gmtime(time.time())))



