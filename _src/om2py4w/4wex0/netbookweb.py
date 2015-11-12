# _*_ coding:utf-8 _*_

from bottle import *
from jinja2 import Template
from socket import *
import time
from os.path import exists

def main():
    BUF_SIZE = 65565
    ss = socket(AF_INET, SOCK_DGRAM)
    ss_addr = ('127.0.0.1', 8800)
    ss.bind(ss_addr)
    while True:
        print "waiting for data"
        data, cs = ss.recvfrom(BUF_SIZE)
        print 'Connected by', cs, 'Receive Data: ', data, 'at: ', time.strftime("%d/%m/%Y %H:%M:%S"+"\n")
        ss.sendto(data, cs)
    history(data)
    ss.close   

def save(newline):
    global txt
    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n")) #在保存当前输入的同时，也保存当前时间。
    txt.write(newline)
    txt.write("\n"+"\n")
    txt.close()

def printhistory():
    if exists("tempfile.txt"): 
        txt = open("tempfile.txt")
        notelist = txt.readlines()
        print "历史记录：" + "\n"
        for i in notelist:
            print(i)

@route('/history')
def printh():
    if exists("tempfile.txt"): 
        txt = open("tempfile.txt")
        notelist = txt.readlines()
        return '''
    <form action="/index" method="POST">
    The history records
    <br/>''' + "".join(notelist)

@get('/index')
def newline():
    return '''
    <form action="/index" method="POST">
    history
    <br/>    
    Please input a new line: 
    <br/>
    <input name="newline" type="text"/>
    <br/>
    <input value="save" type="submit" />
    </form>
    '''
@post('/index')
def inputnewline():
    newline = request.forms.get('newline')
    if newline:
        save(newline)
        printhistory()
        return newline

if __name__ == '__main__':
    debug(True)
    run(host="localhost", port=8800, reloader=True)
    main()