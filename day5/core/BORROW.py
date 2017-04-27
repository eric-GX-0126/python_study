#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

def borrow():
    import pickle
    from LOGIN import login
    from LOGGER import userlog
    user = login()
    if not user:
        print('信用卡账户登录失败 byebye了 您呢')
        return
    acc_dict = pickle.load(open('../db/user_db','rb'))
    amount = float(input('请输入你要借款的金额:'))
    if acc_dict[user]['balance'] > 7875.00 and amount <= 7500.00:
        amount_sum = float('%.2f'%(amount * ( 1 + 0.05 )))
        print(amount_sum)
        print('借款总金额为:%.2f'%(amount_sum))
        opt = input('是否确认借款\t1:是，2:否:')
        if opt.strip() == '1':
            acc_dict[user]['balance'] -= amount_sum
            pickle.dump(acc_dict, open('../db/user_db', 'wb'))
            userlog(user,' borrow -- %.2f'%-amount_sum)
            print('您的余额为:%.2f'%(acc_dict[user]['balance']))
            return

    else:
        print('余额不足，就不借给你')
        return

