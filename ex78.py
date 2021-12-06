# 找到年龄最大的人，并输出

def find_max(dict):
    max_age = 0
    name_list = []
    for key,value in dict.items():
        if value > max_age:
            max_age = value
            name = key
    print('年龄最大的是{},{}岁'.format(name, max_age))



if __name__ == '__main__':
    person = {'Ronnie':46,'Trump':32,'Wilson':30}
    find_max(person)
