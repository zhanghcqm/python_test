import random
def red_packet(total,num):
    for i in range(num-1):
        per=random.uniform(0.01,total/2)
        total=total- per
        print('%.2f'%per)
    else:
        print('%.2f'%total)

red_packet(10,5)
