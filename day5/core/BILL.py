#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

def bill():
    import pickle
    import time
    from LOGIN import login
    from LOGGER import userlog
    cost_sum = 0.0
    limit_sum = 0.0
    user = login()
    if not user:
        print('信用卡账户登录失败 byebye了 您呢')
        return

    acc_dict = pickle.load(open('../db/user_db','rb'))
    date1 = time.strftime('%Y-%m').split('-')
    date2 = []
    if date1[1] != '1':
        date2.append(date1[0])
        date2.append('0' + str(int(date1[1]) -1))
    else:
        date2.append(date1[0])
        date2.append(12)

    file_name = '../log/' + user + '.log'
    new_file = '../log/' + user + '_' + '-'.join(date1) + '.log'

    with open(file_name,'r') as f1,open(new_file,'w') as new_file:
        for line in f1:
            if '-'.join(date1) in line:
                new_line1 = line.split(' ')[0].split('-')
                if int(new_line1[2]) < 23:
                    new_file.write(line)
            elif '-'.join(date2) in line:
                new_line2 = line.split('-')
                if int(new_line2[2]) >22:
                    new_file.write(line)


    user_file = '../log/' + user + '_' + '-'.join(date1) + '.log'
    print('%s的账单:\n'%'-'.join(date1))
    with open(user_file,'r') as f:
        for line in f:
            print(line)
            cost = float(line.split('--')[1].strip())
            if cost < 0:
                cost_sum += cost
            limit_sum += cost
    print('总共消费:\t%.2f'%cost_sum)
    print('额度为:%.2f'%limit_sum)

