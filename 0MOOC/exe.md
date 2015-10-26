# 生成windows下exe可执行文件 私人教程

## 背景

## 安装
### 安装py2exe  
Get py2exe from http://www.py2exe.org/

## 配置
### 写setup.py  
<pre><code>
from distutils.core import setup
import py2exe

setup(console = ['notebook.py']) #以上周的notebook.py为例。

</pre></code>

### 运行setup.py
在powershell中输入命令：  
> python setup.py py2exe

## 使用

### 运行生成的exe文件  
setup.py运行后，生成了dist文件夹，其中有***.exe这个文件，双击可直接运行。

## 体验

