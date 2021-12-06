# 反向输出一个链表

if __name__ == '__main__':
    ptr = []
    ptr_reversed = []
    for i in range(5):
        num = int(input('please input a number:\n'))
        ptr.append(num)
    print(ptr)

    ptr_reverse = reversed(ptr)
    for i in ptr_reverse:
        ptr_reversed.append(i)
    print(ptr_reversed)
