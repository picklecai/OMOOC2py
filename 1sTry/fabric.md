# Fabirc 私人教程

## 背景

win8

## 安装

搜索，表示要先安装pip。正好到现在也没有安装pip。  

### 1.安装pip  

在[极简 Python 上手导念 | Zoom.Quiet Personal Static Wiki](http://wiki.zoomquiet.io/pythonic/MinimalistPyStart)中有pip安装教程[pip安装教程](https://pip.pypa.io/en/latest/installing/)。当时（2015年4月份）看了没办法，现在就很简单了：  

步骤一：下载[get-pip.py](https://bootstrap.pypa.io/get-pip.py)。这次采用的方式是链接另存为文件。    
步骤二：在命令行下运行这个文件。它开始自动下载[pip-7.1.2-py2.py3-none-any.whl](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip)，自动安装成功。  

### 2.安装fabric  
[windows下安装fabric](http://www.bubuko.com/infodetail-309375.html)这个教程说：安装pip之后要安装Pycrypto、setuptools，才能再安装fabric。  

我在命令行先运行python，进去之后再运行 pip install fabric，错误。绕回去试图安装它说的两个工具，也搞不清自己的机子上setuptools到底装了没有（有的说python装好了就自然有了），两个都没成功。  

在命令行下不进入python，直接运行`pip install fabric`，装好了。  

注：在未翻墙的64位win7上上述操作未成功。安装pip及fabric均出现了许多错误提示。最后结果大概是配置不完全，反正fab命令不能用。  

## 配置

## 使用

fabric安装好了之后，要使用fab命令，需要把代码放入当前文件夹的根目录，并起名为fabfile.py。  

例如：   

1. 进入当前文件夹`I:py`，在命令行运行python。 
2. 建立fabfile.py文件。代码见后文。  
3. 在命令行运行`fab 函数名`。  

代码如下：  

    def hello():
		print("Hello world!")

运行情况：  

![](http://i5.tietuku.com/a084dfc5f83854d1.png)  


一开始的错误使用方式：  

![](http://i5.tietuku.com/16ea5212ad5412c7.png)


## 体验

用它来检验db文件有没有正确写入，很好。  
代码：  

    # _*_ coding:utf-8 _*_


	def dataexam():
	    import sqlite3
	    conn = sqlite3.connect('noterecord.db')
	    cursor = conn.cursor()
	    cursor.execute('select * from record')
	    print cursor.fetchall()
	    cursor.close()
	    conn.commit()
	    conn.close()

由于fabric安装的失败，以上代码每运行一次，就要在命令行里输入一次。反观fabric是多么好用，尤其用在测试上。