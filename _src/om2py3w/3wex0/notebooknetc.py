# _*_coding:utf-8_*_
# 客户端程序

from socket import *
import time
from sys import exit
import notebooknets

def main():
    BUF_SIZE = 65565
    ss_addr = ('127.0.0.1', 8800)
    cs = socket(AF_INET, SOCK_DGRAM)
    notebooknets.printhistory()
    while True:
        global data
        data = raw_input('今日记录，请输入（输入quit退出程序）：')
        if data == 'quit':
            exit(0)
        else:
            cs.sendto(data, ss_addr)
            data, addr = cs.recvfrom(BUF_SIZE)
            print "Data: ", data  
            notebooknets.save(data)      
    cs.close

if __name__ == '__main__':
    main()
