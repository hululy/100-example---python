# 从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存

if __name__ == '__main__':
    filename = 'test.txt'
    with open(filename,'w') as f_obj:
        ch = input('请输入内容:')
        ch = ch.upper()
        f_obj.write(ch)

