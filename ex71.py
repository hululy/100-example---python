# 编写input()和output()函数输入，输出5个学生的数据记录

student_info = []
N = int(input('学生人数:'))

for i in range(5):
    student_info.append(['','',[]])

def input_stu(stu):
    for i in range(N):
        stu[i][0] = input('输入学号:\n')
        stu[i][1] = input('输入姓名:\n')
        for j in range(3):
            stu[i][2].append(int(input('输入分数:\n')))

def output_stu(stu):
    for i in range(N):
        print('%s  %s' % (stu[i][0],stu[i][1]))
        for j in range(3):
            print('%d' % stu[i][2][j], end=' ')
        print('\n-----')

if __name__ == '__main__':
    input_stu(student_info)
    output_stu(student_info)