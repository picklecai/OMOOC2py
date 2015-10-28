# _*_ coding:utf-8 _*_

from os.path import exists
from sys import exit
import time
from Tkinter import *

def main():
    global win
    win = Tk()
    win.title = ('Picklecai notebook' )
    win.geography =('640x480')

    # 放置三个按钮供选择
    b1 = Button(win, text = "打印历史记录", command = printhistory)
    b2 = Button(win, text = "输入新的内容", command = writenew)
    b3 = Button(win, text = "退出程序", command = quit())

    b1.grid(row = 0, column = 0)
    b2.grid(row = 0, column = 1)
    b3.grid(row = 0, column = 3)

    win.mainloop()
 
def printhistory():
    # 打印之前所有的内容

    historyfirst = '''
历史记录：
-------------------------------------------'''
    historynone = "对不起，程序第一次运行，尚无历史记录可打印。你可以开始输入新内容。"
    l1 = Label(win, text = historyfirst)
    l2 = Label(win, text = historynone)

    if exists("tempfile.txt"):   #如果tempfile不存在，说明程序是第一次运行，没有历史内容可打印。
        txt = open("tempfile.txt")
        notelist = txt.readlines()
        txt.close()
        for i in notelist:
            historyfirst + i + "\n" 
        historyfirst + "\n" + "-------------------------------------------"
        l1.grid(row = 1, column = 0) 
    else:
        l2.grid(row = 1, column = 0)

def writenew():
    # 输入新的内容
    newlinefirst = "今日记录，请输入： "
    l3 = Label(win, text = newlinefirst)
    l3.grid(row =2, column = 0)
    newline = Entry(win)
    newline.grid(row = 2, column = 1)    

    txt = open("tempfile.txt", 'a')
    txt.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n")) #在保存当前输入的同时，也保存当前时间。
    txt.write(newline)
    txt.write("\n"+"\n")
    txt.close()

    b4 = Button(win, text = "保存新内容", command = savenew)
    def savenew():
            filename = Entry(win)
            output = open(filename + ".txt", 'w') #规定好扩展名，以免出现用户保存的文件打不开的情况。
            output.write(filename + ".txt"+"\n") #在文件中写入文件名。
            output.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n")) #在文件中写入当前时间。
            output.write(newline)
            output = open(filename + ".txt")
            output.close

if __name__ == '__main__':
    main()
