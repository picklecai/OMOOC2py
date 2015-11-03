# _*_coding:utf-8_*_
# 客户端程序

from socket import *
import time
import notebooknets

def main():
    BUF_SIZE = 65565
    ss_addr = ('127.0.0.1', 8800)
    cs = socket(AF_INET, SOCK_DGRAM)

    while True:
        global data
        data = raw_input('Please Input data>')
        cs.sendto(data, ss_addr)
        data, addr = cs.recvfrom(BUF_SIZE)
        print "Data: ", data        
    cs.close
    notebooknets.history(data)
if __name__ == '__main__':
    main()
