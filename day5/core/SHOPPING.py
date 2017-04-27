#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

def shop():
    import sys
    sys.path.append('../conf')
    #from logger_conf import userlog
    from PAY import pay
    li = []
    flag = False
    product_sum = 0
    prod_dict = {'IPHONE':6000,'IPAD':3500,'IMAC':12000,'APPLE':50,'PEN':100}
    print('欢迎光临 随便吃 随便拿'.center(50,'_'))
    for item in prod_dict:
        print(item,'\t',prod_dict[item])
    while True:
        product = input("请将需要购买的商品加入购物车 输入‘0’退出:")
        if product.strip() == '0':
            sys.exit()
        if prod_dict.get(product.strip(),False):
            li.append(product.strip())
            print('您选择了:',product)
            product_sum += prod_dict[product.strip()]
            continue
        else:
            print('输入有误，请重新输入')
            opt = input('1:重新选择,2:结算,3:继续添加商品:')
            if opt.strip() == '1':
                li = []
                product_sum = 0
                continue
            elif opt.strip() == '2':
                print('、'.join(li),'sum is: ',product_sum)
                flag = True
                #break
        if flag:
            if pay(product_sum):
                print('购买成功')
            else:
                opt = input('1:继续购物 或者任意键退出:')
                if opt.strip() != 1:
                    sys.exit()

shop()