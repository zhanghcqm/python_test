"""
人机猜拳游戏
"""

import random
role_dict={'1':'曹操','2':'张飞','3':'刘备'}
fist_dict={1:'剪刀',2:'石头',3:'布'}
count_role=0
count_pc=0
count_draw=0
while True:
    print('------ 1、曹操  2、张飞  3、刘备 ------')
    role_num = input('请选择一个英雄：')
    if role_num not in ['1','2','3']:
        print('请选择正确的英雄序号！')
        continue
    else:
        print('您选择的英雄是:{}'.format(role_dict[role_num]))

        while True:
            print('------ 1、剪刀  2、石头  3、布 ------')
            fist_num = int(input('请您出拳：'))
            if fist_num not in [1,2,3]:
                print('请选择正确的猜拳序号!')
                continue
            else:
                print('{}出拳:{}'.format(role_dict[role_num], fist_dict[fist_num]))

            pc_num=random.randint(1,3)
            print('电脑出拳:{}'.format(fist_dict[pc_num]))

            result_num = fist_num - pc_num
            if result_num in [-2,1]:
                print('{}获胜!'.format(role_dict[role_num]))
                count_role+=1
            elif result_num in [-1,2]:
                print('电脑获胜！')
                count_pc+=1
            else:
                print('打成平局！')
                count_draw+=1
            break
    choice=input('本轮结束，是否继续游戏：')
    if choice == 'y':
        continue
    elif choice == 'n':
        break

print("对战结束，{}赢{}局！，电脑赢{}局！，平局{}局！".format(role_dict[role_num],count_role,count_pc,count_draw))
    


