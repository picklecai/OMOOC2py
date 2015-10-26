# import自己的代码 
<pre><code>
from Tkinter import *
import notebook


win = Tk()
win.title = ('Picklecai notebook' )
win.geography =('400x600')
w = Label(win, text = 'Hello,world!')
w.pack()
win.mainloop()

notebook.printhistory()

<pre><code>

能正常运行。
