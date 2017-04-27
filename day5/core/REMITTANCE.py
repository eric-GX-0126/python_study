#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

def remittance():
    import pickle
    from LOGIN import login
    from LOGGER import userlog

    user = login()
    if not user:
        print('信用卡账户登录失败 byebye了 您呢')
        return
    acc_dict = pickle.load(open('../db/user_db', 'rb'))
    while True:
        new_user = input('请输入汇款账户:')
        new_user = new_user.strip()
        if new_user == '0':
            return
        if acc_dict.get(new_user,False):
            break
        else:
            print('对方账款不存在请重新输入，输入0退出')
    amount = float(input('请输入汇款金额:'))
    if acc_dict[user]['balance'] > 7875.00 and amount <= 7500.00:
        amount_sum = float('%.2f' % (amount * (1 + 0.05)))
        print(amount_sum)
        print('汇款总金额为:%.2f' % (amount_sum))
        opt = input('是否确认转账\t1:是，2:否:')
        if opt.strip() == '1':
            acc_dict[user]['balance'] -= amount_sum
            acc_dict[new_user]['balance'] += amount
            pickle.dump(acc_dict, open('../db/user_db', 'wb'))
            userlog(user, ' remittance -- %.2f' % -amount_sum)
            print('您的余额为:%.2f' % (acc_dict[user]['balance']))
            return

    else:
        print('余额不足，就不借给你')
        return

