# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个#为止

if __name__ == '__main__':
    filename = input('输入文件名:')
    with open(filename,'w') as f_obj:
        ch = input('请输入内容:')
        while ch != '#':
            f_obj.write(ch)
            ch = input()


