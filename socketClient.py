# coding=utf-8
# !/usr/bin/python

from socket import *
import threading
import inspect
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

HOST = '192.168.0.136'
PORT = 50088
ADDR = (HOST, PORT)
s = socket(AF_INET, SOCK_STREAM)

# 立即释放端口
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

s.connect(ADDR)


def def_socket_thread():
    try:
        addr, c = ADDR
        print "服务端:", addr[0], ",连接成功！"
        t1 = threading.Thread(target=write_from_service, args=(c, addr))
        t1.setDaemon(True)
        t1.start()
        t2 = threading.Thread(target=read_from_service, args=(c, addr))
        t2.setDaemon(True)
        t2.start()
    except IOError as e:
        print "出现错误:" + e.strerror  # v.decode('utf-8')
        s.close()
    print('连接断开!')


def read_from_service(c, addr):
    while True:
        content = c.recv(1024).decode('gbk')
        if content == "":
            print "服务端:", addr[0], ",断开连接！"
            # break
        else:
            print addr[0] + ":" + content


def write_from_service(c, addr):
    while True:
        data = raw_input()
        if data != "":
            msg = data.encode('gbk')
            c.send(msg)


if __name__ == '__main__':
    def_socket_thread()




