# 输出随机数、随机字符串

import random
import string

# 随机浮点数
print(random.random())
print(random.uniform(1,10))   # 指定范围

# 指定范围随机整数
print(random.randint(1,10))

# 指定范围、间隔随机整数
print(random.randrange(1,100,2))

# 指定范围随机字符
print(random.choice('snooker'))

# 指定范围、数量随机字符
print(random.sample('snooker,ronnie',3))

# 从a-zA-Z0-9生成指定数量的随机字符
ran_str = ''.join(random.sample(string.ascii_letters + string.digits,5))
print(ran_str)

# 打乱排序
list = ['snooker','skiing','shoot','bowling']
random.shuffle(list)
print(list)