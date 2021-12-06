# 写一个函数，求一个字符串的长度，在main函数中输入字符串，并输出其长度

def str_count(str):
    l = len(str)
    return l

if __name__ == '__main__':
    str = input('请输入字符串:')
    print('字符串长度为%d' % str_count(str))