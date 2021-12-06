# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

from functools import reduce

def ball(n):
    tour = []
    height = []
    h = 100
    for i in range(1,n+1):
        if i == 1:
            tour.append(h)
        else:
            tour.append(h*2)
        h = h * 0.5
        height.append(h)
        s = reduce(lambda x,y: x+y, tour)
    print('第{}次落地时，共经过{}米'.format(n,s),'\n第{}次反弹高度为{}米'.format(n,height[-1]))

if __name__ == '__main__':
    n = int(input('n = '))
    ball(n)
