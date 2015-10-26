# 使用Tk过程中的坑  
## 1. name 'Tk' is not defined   
产生了pyc的编译文件，删除就没有这个问题了。  

为什么会产生这个文件？  
在powershell中运行py文件，不生成Tk的GUI窗口。在powshell中直接运行代码（使用python命令进入Python之后），会生成GUI窗口。  
试着在ide中运行。仍然没有生成GUI，但是产生了pyc文件。  

##2. Tk窗口不出现  
末尾加了xx.mainloop()就可以在powershell中出现窗口了。  
