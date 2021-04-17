# coding=utf-8
# !/usr/bin/python

from socket import *
import threading
import inspect
import sys
import faceSay

reload(sys)
sys.setdefaultencoding('utf-8')

HOST = '192.168.72.161'
PORT = 12221
ADDR = (HOST, PORT)

s = socket(AF_INET, SOCK_STREAM)
s.bind(ADDR)
s.listen(5)

# def logFileRead(logFile):
#     '''
#     Read logFile by line
#     return List
#     '''
#     logFileDealList = []
#     with open(logFile, 'r') as logFileContent:
#         for line in logFileContent.readlines():
#             logFileDealList.append(line)
#     return logFileDealList


def def_socket_thread():
    try:
        while True:
            c, addr = s.accept()
            resu = "客户端:" + addr[0] + ",连接成功！"
            print resu
            t1 = threading.Thread(target=write_from_client, args=(c, addr))
            t2 = threading.Thread(target=read_from_client, args=(c, addr))
            t1.start()
            t2.start()
    except IOError as e:
        print("出现错误:", e.strerror)
    s.close()
    print '连接断开!'


def read_from_client(c, addr):
    resu = ""
    while True:
        content = c.recv(1024).decode('gbk')
        if content == "":
            resu = "客户端:" + addr[0] + ",断开连接！"
            print resu
            break
        elif content == "10":
            print "开始人脸识别:" + resu
        else:
            resu = addr[0] + ":" + content
            print resu
        # else:
        #     msg = "接收到了:" + content
        #     c.send(msg.encode('gbk'))


def write_from_client(c, addr):
    while True:
        start = raw_input()
        if start == "start":
            data = faceSay.facesearch()
            print data
            if data != "":
                msg = data.encode('gbk')
                c.send(msg)


if __name__ == '__main__':
    def_socket_thread()




