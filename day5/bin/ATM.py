#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

import sys
sys.path.append('../core/')
#from LOGIN import login
from CHECK import check
from BORROW import borrow
from REPAYMENT import repayment
from REMITTANCE import remittance
from BILL import bill
import sys
li = ['查询','还款','借款','转账','账单','退出',]
while True:
    for k,v in enumerate(li,1):
        print(k,v)
    opt = input('请输入操作选项:')
    if opt.strip() == '1':
        check()
    elif opt.strip() == '2':
        repayment()
    elif opt.strip() == '3':
        borrow()
    elif opt.strip() == '4':
        remittance()
    elif opt.strip() == '5':
        bill()
    elif opt.strip() == '6':
        sys.exit()