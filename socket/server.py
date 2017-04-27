#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:GX

import socketserver
import subprocess
import json
import os
class MyServer(socketserver.BaseRequestHandler,socketserver.BaseServer):
    def handle(self):
        self.request.send(bytes('welcome socketserver','utf8'))
        while True:
            recv_data = self.request.recv(1024)
            self.recv_cmd = json.loads(recv_data.decode())
            self.file_path = self.recv_cmd[-1]
            if hasattr(self,self.recv_cmd[0]):
                getattr(self,self.recv_cmd[0])()

    def put(self):
        filename = self.recv_cmd[-2].split('/')[-1]
        filesize = self.recv_cmd[-1]
        self.request.send(bytes(json.dumps({"status":"1"}),'utf8'))
        with open(filename,'wb') as f:
            while filesize > 0:
                data = self.request.recv(1024)
                f.write(data)
                filesize -= len(data)
        self.request.send(bytes('send successfully','utf8'))

    def get(self):
        if os.path.isfile(self.file_path):
            filesize = os.path.getsize(self.file_path)
            self.request.send(bytes(json.dumps(["1",filesize]),'utf8'))
            recv_msg = json.loads(self.request.recv(1024).decode())
            if recv_msg['status'] == '1':
                print('start sending')
                print(filesize)
                with open(self.file_path,'rb') as f:
                    for line in f:
                        self.request.send(line)
        else:
            self.request.send(bytes(json.dumps(["0","file is not exist','utf8"])))

if __name__ == '__main__':
    server = socketserver.ThreadingTCPServer(('0.0.0.0',8083),MyServer)
    server.serve_forever()

