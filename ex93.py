# 时间函数举例3

import time

if __name__ == '__main__':
    start = time.process_time()
    for i in range(10000):
        print(i)
    end = time.process_time()
    print('different is %6.3f' % (end - start))
