#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX


def Get_ID(username):
    flag = False
    with open('conf1.txt','r') as f:
        for line in f:
            new_line = line.strip().split('|')
            if username == new_line[0]:
                return  new_line[5]
                flag = True
                return
    if not flag:
        print('用户不存在')



def Root(func):
    def inner(user,num):
        new_user = input('请输入用户账户：')
        #print('hehe')
        ID1 = Get_ID(user.strip())
        ID2 = Get_ID(new_user.strip())
        #print(ID1,ID2)
        if num == '3' and ID1 == '0':
            func(new_user,num)
        elif num != '3' and (ID1 == ID2  or  ID1 == '0'):
            func(new_user,num)
        else:
            print('您没有权限')
    return  inner

@Root
def Find(user,num):
    li = ['账号', '密码', '邮箱', '电话', 'uid', 'gid']
    with open('conf1.txt','r') as f:
        for line in f:
            new_line = line.strip().split('|')
            if user == new_line[0]:
                for k in li:
                    print(k, '\t', new_line[li.index(k)])
    Operation(user)

@Root
def Get(user,num):
    import os
    import time
    with open('conf1.txt', 'r') as f1, open('conf2.txt', 'w') as f2:
        for line in f1:
            new_line = line.strip().split('|')
            if user == new_line[0]:
                if num == '2':   #password
                    new_pwd1 = input('请输入新密码:')
                    new_pwd2 = input('请再次输入新密码:')
                    if new_pwd1.strip() == new_pwd2.strip():
                        new_line[1] = new_pwd1.strip()
                        new = '|'.join(new_line) + '\n'
                        f2.write(new)
                        print('密码修改成功')
                    else:
                        print('密码不匹配')
                        f2.write(line)
                elif num == '3':  ##privilege
                    new_line[5] = '0'
                    new = '|'.join(new_line) + '\n'
                    f2.write(new)
                    print('权限修改成功')
            else:
                f2.write(line)
    os.rename('conf1.txt', 'conf1.txt_backup' + time.strftime("%m-%d_%H_%M_%S", time.localtime()))
    os.rename('conf2.txt', 'conf1.txt')


def Register():
    flag = True
    id_num = 0
    while True:
        username = input('请输入注册用户名,输入0退出注册:\n')
        if username.strip() == '0':
            exit()
        with open('conf1.txt','r+') as f:
            for line in f:
                if username.strip() in line.strip().split('|')[0]:
                    print('用户名已被注册，请重新注册')
                    flag = False
                    break
                else:
                    id_num +=  1
            if flag:
                pwd1 = input('Please input password:\n')
                pwd2 = input('Please input password again\n')
                if pwd1.strip() == pwd2.strip():
                    email = input('请输入email:')
                    phone = input('请输入phone:')
                    new_line = '\n' + username.strip() + '|' + pwd1.strip() +  '|' + email + '|' + phone + '|' +\
                               str(id_num) + '|' +  str(id_num)
                    print(new_line)
                    f.write(new_line)
                    print('注册成功')
                    break
                else:
                    print('password is not same')
    if flag:
        opt = input('是否登录  1:登录,其他键:退出\n')
        if opt.strip() == '1':
            Login()
        else:
            exit()

def Exit(user,num):
    import sys
    sys.exit()

def Operation(user):
    while True:
        option = ['查询信息','修改密码','修改权限','退出登录']
        print('请选择操作选项：')
        for k,v in enumerate(option,1):
            print(k,v)
        func_dic = {1:Find,2:Get,3:Get,4:Exit}
        num = input('请输入操作选项:')
        try:
            func_dic[int(num.strip())](user,num.strip())
        except KeyError:
            print('输入有错误')
        except ValueError:
            print('输入有错误')

def Login():
    flag = 1
    while flag < 4:
        username = input('请输入用户名:')
        pwd = input('请输入密码:')
        with open('conf1.txt','r') as f:
            for line in f:
                new_line = line.strip().split('|')
                if username == new_line[0] and pwd == new_line[1]:
                    #print('登录成功')
                    flag = 0
                    break
        if flag == 0:
            break
        else:
            flag += 1
    if flag != 0:
        print('登录失败')
    else:
        print('登录成功')
        Operation(username)

def main():
    import sys
    li = ['登录','注册','退出']
    print('welcome'.center(55,'-'))
    while True:
        for k,v in enumerate(li,1):
            print(k,v)
        opt = input('请输入:')
        if opt.strip() == '1':
            Login()
        elif opt.strip() == '2':
            Register()
        elif opt.strip() == '3':
            sys.exit()
        else:
            print('输入有误请重新输入')

main()