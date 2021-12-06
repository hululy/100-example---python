# deque列表使用实例

from collections import deque

list1 = ['snooker','bowling']
list2 = deque(list1)

# 添加元素
list2.append('skiing')
print(list2)
list2.appendleft('o')
print(list2,'\n')


# 添加可迭代对象
list2.extend(['t','e','x'])
print(list2)
list2.extendleft([(0,1),2,3])
print(list2,'\n')

# 移除元素
list2.pop()
print(list2)
list2.popleft()
print(list2,'\n')

# 移除第一次出现的指定元素
list2.remove(2)
print(list2,'\n')

# 统计指定元素个数
count = list2.count('o')
print(count,'\n')

# 在指定位置插入元素
list2.insert(0,'ly')
print(list2,'\n')

# 反转
list2.rotate(2)   # 正数，从后转到前
print(list2)
list2.rotate(-3)   # 负数，从前转到后
print(list2)

# 清空列表元素
list2.clear()
print(list2,'\n')

# 只读属性，返回限制的最大长度;添加元素超过最大限制长度时，删除另一边的元素
list = deque(maxlen=2)
list.append(1)
list.append(2)
print(list)
list.append(3)
print(list)
print(list.maxlen)

