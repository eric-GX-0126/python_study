#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

import pickle
acc_dict = {'gx': {'pwd': '123', 'lock_num': 0, 'balance': 15000.00},
            'zt': {'pwd': '456', 'lock_num': 0, 'balance': 15000.00},
            'tony': {'pwd': '789', 'lock_num': 0, 'balance': 15000.00},}
#pickle.dump(acc_dict,open('../db/user_db','wb'))

acc = pickle.load(open('../db/user_db','rb'))
print(acc)