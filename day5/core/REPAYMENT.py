#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX


def repayment():
    import pickle
    from LOGGER import  userlog
    from LOGIN import login
    user = login()
    if not user:
        print('信用卡账户登录失败 byebye了 您呢')
        return
    acc_dict = pickle.load(open('../db/user_db', 'rb'))
    money = float(input('请输入还款金额:'))
    opt = input('是否还款\t1:是,2:否\t')
    if opt.strip() != '1':
        return
    else:
        acc_dict[user]['balance'] += money
        userlog(user, ' repayment -- %.2f' %money)
        pickle.dump(acc_dict,open('../db/user_db', 'wb'))
        return

