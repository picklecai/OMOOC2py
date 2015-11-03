# OMOOC.py 周任务代码试作


## 1w

- 私人笔记
    + 文本数据库

把使用Tkinter过程中的测试代码放在这里。

## 使用Tk过程中的坑  
### 1. name 'Tk' is not defined   
产生了pyc的编译文件，删除就没有这个问题了。  

为什么会产生这个文件？  
在powershell中运行py文件，不生成Tk的GUI窗口。在powshell中直接运行代码（使用python命令进入Python之后），会生成GUI窗口。  
试着在ide中运行。仍然没有生成GUI，但是产生了pyc文件。  

### 2. Tk窗口不出现  
末尾加了xx.mainloop()就可以在powershell中出现窗口了。  

### 3. unexpected indent  
如果空格为三个，则出现。问题是：提示并没有出现在出现问题的那一行。试了好几次才发现。
<pre><code>
def main():
  ''' win = Tk()
    win.title = ('Picklecai notebook' )
    win.geography =('400x600') '''
    print '''
请输入你的选择：
1 打印之前的历史记录
2 输入新的内容
3 退出程序 '''
	
   ''' l = Label(win, text = chooselabel)
    l.pack()'''

</pre></code>

对于以上代码，提示说是在print'''这一行，其实问题出在'''win。可能是因为那一行是注释？所以不提示然而不予通过？修改了win这一行后，马上提示到了'''l这一行。
