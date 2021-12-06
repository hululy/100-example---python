'''
企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；
40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%；
高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数(P)？
'''
def bonus_count():
    I = int(input('请输入利润（单位：万元）：'))
    if I <= 10:
        P = I * 0.1
        print('利润{}万元，发放奖金{}万元'.format(I,P))
    elif 10 < I <= 20:
        P  = 1 + 0.075*(I-10)
        print('利润{}万元，发放奖金{}万元'.format(I,P))
    elif 20 < I <= 40:
        P = 1 + 0.75 + 0.05* (I - 20)
        print('利润{}万元，发放奖金{}万元'.format(I, P))
    elif 40 < I <= 60:
        P = 1 + 0.75 + 1 + 0.03 * (I - 40)
        print('利润{}万元，发放奖金{}万元'.format(I, P))
    elif 60 < I <= 100:
        P = 1 + 0.75 + 1 + 0.6 + 0.015 * (I - 60)
        print('利润{}万元，发放奖金{}万元'.format(I, P))
    else:
        P = 1 + 0.75 + 1 + 0.6 + 0.6 + 0.01 * (I - 100)
        print('利润{}万元，发放奖金{}万元'.format(I, P))

bonus_count()





