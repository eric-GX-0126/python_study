#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

def check():
    from LOGGER import  userlog
    from LOGIN import login
    import pickle
    user = login()
    if not user:
        print('信用卡账户登录失败 byebye了 您呢')
        return
    acc_dict = pickle.load(open('../db/user_db', 'rb'))
    user_file = '../log/' + user + '.log'
    with open(user_file,'r') as f:
        print(f.read())
    print('您的余额为:%.2f'%acc_dict[user]['balance'])


