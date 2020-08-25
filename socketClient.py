# coding=utf-8
# !/usr/bin/python

from socket import *
import threading
import inspect
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

HOST = '192.168.32.109'
PORT = 50088
ADDR = (HOST, PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(ADDR)


def def_socket_thread():
    try:
        while True:
            c, addr = s.accept()
            print "服务端:", addr[0], ",连接成功！"
            t1 = threading.Thread(target=write_from_client, args=(c, addr))
            t1.start()
            t2 = threading.Thread(target=read_from_client, args=(c, addr))
            t2.start()
    except IOError as e:
        print("出现错误:", e.strerror)
    s.close()
    print('连接断开!')


def read_from_client(c, addr):
    while True:
        content = c.recv(1024).decode('gbk')
        if content == "":
            print "服务端:", addr[0], ",断开连接！"
            break
        else:
            print addr[0] + ":" + content


def write_from_client(c, addr):
    while True:
        data = raw_input()
        if data != "":
            msg = data.encode('gbk')
            c.send(msg)


if __name__ == '__main__':
    def_socket_thread()




