# 从键盘输入一些字符，逐个把它们写到磁盘文件上，直到输入一个#为止

from sys import stdout

if __name__ == '__main__':
    filename = input('输入文件名:')
    f_obj = open(filename,'w')
    ch = input('请输入内容:')
    while ch != '#':
        f_obj.write(ch)
        stdout.write(ch)
        ch = input()
    f_obj.close()
