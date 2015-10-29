# _*_coding:utf-8_*_

from os.path import exists
from sys import exit
import time
import Tkinter

def main():
    global win
    win = Tkinter.Tk()
    # 为窗体设置标题和大小
    win.title = ('Picklecai notebook')
    win.geography = ('640x480')
    # 放置三个按钮供选择
    b1 = Tkinter.Button(win, text="打印历史记录", command=printhistory)
    b2 = Tkinter.Button(win, text="输入新的内容", command=writenew)
    b3 = Tkinter.Button(win, text="退出程序", command=exit1)
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=2)
    b3.grid(row=0, column=4)
    win.mainloop()

def printhistory():
    # 打印之前所有的内容
    historyfirst = '''
    历史记录：
    -------------------------------------------''' + "\n"
    historynone = "对不起，程序第一次运行，尚无历史记录可打印。你可以开始输入新内容。"
    l1 = Tkinter.Label(win)
    if exists("tempfile.txt"):   # 如果tempfile不存在，说明程序是第一次运行，没有历史内容可打印。
        txt = open("tempfile.txt")
        notelist = txt.readlines()
        txt.close()
        for i in notelist:
            historyfirst += (i + "\n")
        historyfirst += ("\n" + "-------------------------------------------")
        l1.configure(text=historyfirst)
    else:
        l1.configure(text=historynone)
    l1.grid(row=1, column=0)

def writenew():
    # 输入新的内容
    prompt = "今日记录，请输入： "
    l3 = Tkinter.Label(win, text=prompt)
    l3.grid(row=1, column=2)
    newline = Tkinter.Entry(win)
    newline.grid(row=2, column=2)

    def savenew():
        # 保存
        fn = Tkinter.Entry(win)
        fn.grid(row=4, column=2)
        fn.bind('<Key-Return>', fuzhi)
        filename = fuzhi(fn)
        output = open(filename + ".txt", 'w')  # 规定好扩展名，以免出现用户保存的文件打不开的情况。
        output.write(filename + ".txt"+"\n")  # 在文件中写入文件名。
        output.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n"))  # 写入当前时间。
        output.write(newline.get().encode("utf-8"))  # 可以输入汉字
        output = open(filename + ".txt")
        output.close
        # 暂存
        txt = open("tempfile.txt", 'a')
        txt.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n"))  # 在保存当前输入时，也保存当前时间。
        txt.write(newline.get().encode("utf-8"))  # 可以输入汉字
        txt.write("\n"+"\n")
        txt.close()

    b4 = Tkinter.Button(win, text="保存新内容", command=savenew)
    b4.grid(row=3, column=2)

def fuzhi(e):
    e = Tkinter.Entry(win)
    f = e.get().encode("utf-8")
    return f

def exit1():
    exit()

if __name__ == '__main__':
    main()
