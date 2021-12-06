# 时间函数举例4:一个猜数游戏，判断一个人反应快慢

import time
import random

if __name__ == '__main__':
    num = random.randint(0,100)
    while True:
        answer = int(input('Please input your answer:'))
        start = time.process_time()
        if answer == num:
            end = time.process_time()
            diff = end - start
            print('Right！time={}'.format(diff))
            break
        elif answer > num:
            print('Too high!')
        elif answer < num:
            print('Too low!')


