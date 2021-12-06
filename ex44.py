# 两个3*3矩阵相加，并返回一个新矩阵

import numpy as np
import random

A = np.random.randint(0,10,(3,3))
B = np.random.rand(9).reshape(3,3)

print('A:\n',A)
print('\nB:\n',B)
print('\nA+B:\n',A+B)