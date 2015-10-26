from os.path import exists
from sys import exit
import time
from Tkinter import *

def main():
    win = Tk()
    win.title = ('Picklecai notebook' )
    win.geography =('640x480') 
    chooselabel = '''
请输入你的选择：
1 打印之前的历史记录
2 输入新的内容
3 退出程序 '''	
    l = Label(win, text = chooselabel, justify="left")
    l.grid(row = 0, column = 0)
    win.mainloop()
