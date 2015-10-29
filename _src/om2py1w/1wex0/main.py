# _*_coding:utf-8_*_
import Tkinter
import notebook

def main():
    # 创建窗体
    win = Tkinter.Tk()

    # 为窗体设置标题和大小
    win.title = ('Picklecai notebook' )
    win.geography =('400x600')
    # win.attributes("-alpha", 0.5)

    # 放置标签
    w = Tkinter.Label(win, text = 'Please input a number:')
    w.grid(row = 0, column = 0)

    # 输入
    txt = Tkinter.Entry(win)
    txt.grid(row = 1, column = 0)

    def a():
        print txt.get()

    def b(event):
        print("You enter the key: " + event.char)

    # 放置按钮
    b1 = Tkinter.Button(win, text = "click")
    # b1.pack(fill= Tkinter.X, side=Tkinter.BOTTOM, pady=2)
    b2 = Tkinter.Button(win, text = "print_entry", command = a)
    b2.grid(row = 2, column = 0)
    '''txt.bind('<Key>', b)'''
    txt.bind('<Key-Return>')
    print "This is Key Enter."
    # txt.bind('<Key-Return>', b)

    m= Tkinter.Message(win, text="this is a message.", width=50)
    m.grid(row=3, column=0)

    win.mainloop()

if __name__ == '__main__':
	main()
