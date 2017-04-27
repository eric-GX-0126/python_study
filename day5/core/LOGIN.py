#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

def login():
    import sys
    import pickle
    acc_dict = pickle.load(open('../db/user_db', 'rb'))
    while True:
        user = input("请输入用户账户 或 输入'0'退出:")
        user = user.strip()
        if user == '0':
            sys.exit()
        password = input('请输入密码:')
        password = password.strip()
        if acc_dict.get(user,False):
            if acc_dict[user]['lock_num'] < 3:
                if acc_dict[user]['pwd'] == password:
                    print('success')
                    return user
                else:
                    print('密码错误')
                    acc_dict[user]['lock_num'] += 1
            else:
                print('账户已被锁定，请联系管理人员解锁')
                pickle.dump(acc_dict,open('../db/user_db','wb'))
                return
        else:
            print('账户不存在')