#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX



def pay(product_sum):
    from LOGIN import login
    from LOGGER import userlog
    import pickle
    user = login()
    if not user:
        print('信用卡账户登录失败 byebye了 您呢')
        return
    else:
        acc_dict = pickle.load(open('../db/user_db','rb'))
        opt = input('是否确认支付\t Y:是，2:否\t')
        if opt.strip() == 'Y':
            if acc_dict[user]['balance'] >= product_sum:
                acc_dict[user]['balance'] -= product_sum
                pickle.dump(acc_dict,open('../db/user_db','wb'))
                userlog(user,' cost -- %.2f'%-product_sum)
                #print('支付成功')
                return True
            else:
                print('余额不足请使用其他支付方式')
                return False
        else:
            return False

