#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:GX

import  socket
import json
import os
import hashlib
import sys
import time

class transfer_cmd:
    def __init__(self,ip,port):
        self.srv_ip = ip
        self.srv_port = port
        self.s = socket.socket()
        self.s.connect((self.srv_ip,self.srv_port))
        print(self.s.recv(1024).decode())
        self.login()
        while True:
            self.send_cmd = input('>>>:').strip().split()
            if not self.send_cmd:continue
            if not hasattr(self,self.send_cmd[0]):
                self.cmd()
            else:
                getattr(self,self.send_cmd[0])()
        self.s.close()


    def login(self):
        while True:
            username = input('username:')
            passwd = input('password:')
            passwd_obj = hashlib.md5(bytes('gx', encoding='utf-8'))  # md5中增加一个key
            passwd_obj.update(bytes(passwd, encoding='utf-8'))
            passwd_res = passwd_obj.hexdigest()
            acc_user = json.dumps([username,passwd_res])
            self.s.send(bytes(acc_user,'utf8'))
            self.recv_res = self.s.recv(1024).decode()
            if  self.recv_res == '1':
                return
            else:
                print(self.recv_res)
                continue


    def cmd(self):
        self.s.send(bytes(json.dumps(self.send_cmd), 'utf8'))
        recv_data = json.loads(self.s.recv(4096).decode())
        # print('recv_data', recv_data)
        if recv_data[0] == '1':
            self.s.send(bytes(json.dumps(['1','status']),'utf8'))
            recv_size = recv_data[-1]
            # print(type(recv_size),recv_size)
            recv_res = b''
            while recv_size > 0:
                data = self.s.recv(1024)
                recv_size -= len(data)
                recv_res += data
            print(recv_res.decode())
        else:
            print(recv_data[-1])


    def progress_bar(self,num,total):
        rate = float(num) / total * 100
        r = '\r%s>%.2f%%' % ('-' * int(rate), rate)
        sys.stdout.write(r)
        sys.stdout.flush()


    def put(self):
        while True:
            if os.path.isfile(self.send_cmd[-1]): #file exist?
                filesize = os.path.getsize(self.send_cmd[-1])
                filename = self.send_cmd[-1].split('/')[-1]
                filepath = self.send_cmd[-1]
                self.send_cmd[-1] = filename
                print(self.send_cmd)
                self.send_cmd.append(filesize)
                print(self.send_cmd)
            else:
                print('file is not exist')
                return
            self.s.send(bytes(json.dumps(self.send_cmd),'utf8'))
            srv_status = json.loads(self.s.recv(1024).decode())
            line_size = 0
            if srv_status['status'] == "1":
                with open(filepath,'rb') as f:
                    for line in f:
                        self.s.send(line)
                        line_size += len(line)
                        self.progress_bar(line_size,filesize)
                print()
                recv_msg = self.s.recv(1024)
                print(recv_msg.decode())
                return
            else:
                print('server is not ready')
                return

    def get(self):
        if len(self.send_cmd) != 2:
            print('cmd err')
            return
        self.s.send(bytes(json.dumps(self.send_cmd),'utf8'))
        # print(self.send_cmd)
        recv_msg = json.loads(self.s.recv(1024).decode())
        if recv_msg[0] == '1':
            self.s.send(bytes(json.dumps({"status":'1'}), 'utf8'))
            filesize = recv_msg[-1]
            total_size = filesize
            # print('sum filesize',filesize)
            filename = self.send_cmd[-1].split('/')[-1]
            with open(filename,'wb') as f:
                while filesize > 0:
                    data = self.s.recv(1024)
                    f.write(data)
                    # print(data)
                    filesize -= len(data)
                    self.progress_bar(total_size-filesize,total_size)
                print()
        else:
            print(recv_msg)

if __name__ == '__main__':
    srv_ip = input('FTP Server IP:')
    obj = transfer_cmd(srv_ip,8888)
