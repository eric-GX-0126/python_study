#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

import re
def calc(s):
    if re.search(r'[*/]', s):                         # 乘除运算
        # print('s is',s)
        s = s.replace('-', '+-')
        s = s.replace('*+','*')
        s = s.replace('/+','/')
        s = re.sub('^\+', '', s)
        # print('s.replace',s)
        r1 = re.split(r'(\+)',s)
        # print('r1 is',r1)
        for i in r1:
            if re.match(r'[+\-*/]',i) and len(i) == 1:
                pass
            else:
                r2 = re.split(r'([*/])', i)
                sum = float(r2[0])
                index = 0
                while True:
                    if index + 2 > len(r2):
                        break
                    if r2[index + 1] == '*':
                        sum *= float(r2[index + 2])
                    else:
                        sum /= float(r2[index + 2])
                    index += 2
                r1[r1.index(i)] = sum
        sum = float(r1[0])
        index = 0
        while True:
            if index + 2 > len(r1):
                return sum
            if r1[index + 1] == '+':
                sum += float(r1[index + 2])
            else:
                sum -= float(r1[index + 2])
            index += 2
    else:                                       #加 减 运算
        s = s.replace('-','+-')
        s = re.sub('^\+', '', s)
        r1 = re.split(r'(\+)', s)
        li = []
        for i in r1:
            if i:
                li.append(i)
        sum = float(li[0])
        index = 0
        while True:
            if index + 2 > len(li):
                return sum
            if li[index + 1] == '+':
                sum += float(li[index + 2])
            else:
                sum -= float(li[index + 2])
            index += 2
while True:
    expr = input('==========>')
    expr = expr.replace(' ','')
    if 'exit' in expr:
        break
    elif re.findall(r'[a-zA-Z]',expr):
        print('输入不合法')
        continue
    expr = expr.replace('++', '+')
    expr = expr.replace('--', '+')
    expr = expr.replace('+-', '-')
    #print(expr)
    while True:
        if '(' in expr:
            r = re.split(r"\(([^()]+)\)", expr, 1)
            # print(r)
            if len(r) == 3:
                r[1] = str(calc(r[1]))
                expr = ''.join(r)
                expr = expr.replace('++', '+')
                expr = expr.replace('--', '+')
                expr = expr.replace('+-', '-')
                #print(expr)
                # print('r1 is',r[1],'\n','expr is',expr)
        else:
            print('Result:\t',calc(expr))
            break