#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

def Find():
    Domain_name = input('请输入查找的域名：')
    flag = 0
    with open('conf1','r+',encoding='utf-8') as f1:
        for line in f1:
            if line.startswith('backend'):
                if Domain_name in line:
                    print(line)
                    flag = 1
                    continue
                else:
                    flag = 0
            if flag == 1:
                print(line)

def Add():
    import os
    Domain_name = input('Please input domain_name you want to find:')
    Server = input('Please input Server IP:')
    Weight = input('Please input weight:')
    Maxconn = input('Please input max connections:')

    Srv_info = '        ' + 'server' + ' ' + Server + ' ' + 'weight' + ' ' + Weight + ' ' + 'maxconn' + ' ' + Maxconn

    flag = 0

    with open('conf1', 'r', encoding='utf-8') as f1, open('conf2', 'w+') as f2:
        for line in f1:
            if line.startswith('backend'):
                if Domain_name in line:
                    flag = 1
                    f2.write(line)
                    continue
                else:
                    flag = 0
                    f2.write(line)
                    continue
            else:
                if flag == 1 and 'server' in line:
                    f2.write(line)
                    f2.write(Srv_info)
                    continue
                else:
                    f2.write(line)
    os.rename('conf1','conf1.backup')
    os.rename('conf2','conf1')


def Del():
    pass


opt = {0: '退出', 1: '查找', 2: '添加', 3: '删除',}
for item in opt:
    print(item, opt[item])

num = input('请输入操作选项：')
if num == '1':
    Find()
elif num == '2':
    Add()
elif num == '3':
    Del()
elif num == '0':
    exit()
else:
    print('您的输入有误，请重新输入')



