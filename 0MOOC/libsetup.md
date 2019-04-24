安装库

使用pip3安装了几个库：  


```
pip3 install lxml
pip3 install beautifulsoup4
pip3 install requests

```  

从昨天开始，每次使用了pip，都会提示我从8升级到19.但其实已经升级了。

现在试了一下用`pip3`代替`pip`升级它自己：  

```
pip3 install --upgrade pip
```

再用`pip3 list`检查，显示版本号是19了。

在ipython中运行py3，import这几个库，都找不到。看来肯定是没有安装到那个下面去了。终端直接进入python3，import是可以的。

所以用pip3安装，是没法关联到ipython中去的。conda可以安装吗？？？

```
conda install lxml
conda install beautifulsoup4
conda install requests
``` 
安装成功。

打开ipython notebook试，在py3下，一个都不能import，在py2下，除了beautifulsoup4之外的其他两个可以import。查看了`conda list`，三个包都显示在py2.7下。

如果在终端直接进入ipython，由于调用了py2的内核，效果和notebook中新建一个py2是一样的，即除了beautifulsoup4外的其他两个可以import。

重新使用激活py3的命令：`source activate python35`，然后`conda install requests`，py3下成功import了。`conda install lxml`也成功了。但是`conda install beautifulsoup4`照旧，安装成功了，不能import。

发现问题出在如何引用库上：`from bs4 import BeautifulSoup`  
人家B和S是大写的。python是大小写敏感的！！！以及要从bs4中去import。回到py2下，也成功了。

所以意思是以后想要在ipython中同时使用py2和py3，每个库都要在两种状态下各安装一遍？

## 安装pyperclip

使用上面的方法，安装`pyperclip`库。先激活python35,再用conda命令。超时失败，anaconda中没有。回到python2也是没有。  

按照[python - 怎样安装第三方包到Anaconda环境？ - SegmentFault 思否](https://segmentfault.com/q/1010000012539647)的提示，目录切换到/bin/（由于操作失误，是在/caimeijuan下直接cd /bin的），再使用`pip`和`pip3`各安装一遍。回到ipython中，py2文件可以导入，py3文件不能。

用`source activate python35`激活python3,照上操作，目录进入bin，用pip3安装，ipython中py3文件可以导入了。

## 在ipython中使用终端命令

加个!就可以了。
例如，Mac中清除剪切板的命令是`pbcopy < /dev/null`，在ipython notebook中输入`!pbcopy < /dev/null`就可以清空剪切板了。

## 安装numpy和matplotlib

用	`source activate python35`进入py3，numpy是成功的。
`conda install matplotlib`未成功。还让我手动删掉一个/anaconda/envs/python35/lib/python3.7/site-packages/tornado下的__init__.py文件，删了以后也还是不行。  
于是改用`pip install matplotlib`，貌似成了。

想多了，import matplotlib的结果是：

```
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-7-0484cd13f94d> in <module>
----> 1 import matplotlib

~/anaconda/envs/python35/lib/python3.7/site-packages/matplotlib/__init__.py in <module>
    208 
    209 
--> 210 if not compare_versions(numpy.__version__, __version__numpy__):
    211     raise ImportError(
    212         "Matplotlib requires numpy>=%s; you have %s" % (

AttributeError: module 'numpy' has no attribute '__version__'

```

感觉意思是numpy要升级。上次怎么装上的也忘了。使用`pip install --upgrade numpy`升级，但是提示为已经是新版本了：`Requirement already up-to-date: numpy in ./anaconda/envs/python35/lib/python3.7/site-packages (1.16.2)`

那就update刚刚装的matplotlib吧。  
`pip install --upgrade matplotlib`  
结果似乎倒苦水了：  
```
Requirement already up-to-date: matplotlib in ./anaconda/envs/python35/lib/python3.7/site-packages (3.0.3)
Requirement already satisfied, skipping upgrade: numpy>=1.10.0 in ./anaconda/envs/python35/lib/python3.7/site-packages (from matplotlib) (1.16.2)
Requirement already satisfied, skipping upgrade: kiwisolver>=1.0.1 in ./anaconda/envs/python35/lib/python3.7/site-packages (from matplotlib) (1.0.1)
Requirement already satisfied, skipping upgrade: python-dateutil>=2.1 in ./anaconda/envs/python35/lib/python3.7/site-packages (from matplotlib) (2.8.0)
Requirement already satisfied, skipping upgrade: cycler>=0.10 in ./anaconda/envs/python35/lib/python3.7/site-packages (from matplotlib) (0.10.0)
Requirement already satisfied, skipping upgrade: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in ./anaconda/envs/python35/lib/python3.7/site-packages (from matplotlib) (2.3.1)
Requirement already satisfied, skipping upgrade: setuptools in ./anaconda/envs/python35/lib/python3.7/site-packages (from kiwisolver>=1.0.1->matplotlib) (40.8.0)
Requirement already satisfied, skipping upgrade: six>=1.5 in ./anaconda/envs/python35/lib/python3.7/site-packages (from python-dateutil>=2.1->matplotlib) (1.12.0)
```

看有个人是卸载再重装numpy的，于是：
`pip uninstall numpy`
然后：
`pip install -U numpy`
没有反应。
重启电脑，成了！！！！

## 安装builtwith、python-whois、selenium

用`source activate python35`进入python3，`pip3 install builtwith`，`pip3 install python-whois`，`pip3 install selenium`几秒钟就装好了。 

selenium有点麻烦。虽然装好了，但是不能使用chrome。需要下载Chromedriver，放到环境变量中去。

查看selenium版本号： `pip3 list selenium`

## 安装openpyxl、pillow  

用`source activate python35`进入python3，`conda install openpyxl`，`conda install pillow`，很快就装好了，可以用了。

## 安装PyPDF2

用`source activate python35`进入python3，不能用conda，必须用pip3安装。  

` pip3 install PyPDF2`


## 安装mounty  

[mac OSError: [Errno 30] Read-only file system: 'complete_data.txt' - 你的朋友不及格，你很难过；你的朋友考了第一，你更难过。 - CSDN博客](https://blog.csdn.net/w5688414/article/details/79248777)

```
---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)
<ipython-input-11-7743c951bce7> in <module>
     40 for file in dupFiles:
     41     if os.path.exists(file):
---> 42         os.remove(file)
     43     else:
     44         print('No such file. %s' %file)

OSError: [Errno 30] Read-only file system: '古典丨李海峰：凡事必有4种解决方案.mp3'

```
安装命令为：

`brew cask install mounty`

安装失败，原因是：  
`Error: Unknown command: cask`  

参照：  
[Bug report: "Error: Unknown command: cask" after #23852 · Issue #23934 · Homebrew/homebrew-cask](https://github.com/Homebrew/homebrew-cask/issues/23934)

```
caimeijuandeAir:local caimeijuan$ git fetch
remote: Enumerating objects: 121631, done.
remote: Counting objects: 100% (121631/121631), done.
remote: Compressing objects: 100% (29561/29561), done.
error: RPC failed; curl 18 transfer closed with outstanding read data remaining
fatal: the remote end hung up unexpectedly
fatal: early EOF
fatal: index-pack failed
caimeijuandeAir:local caimeijuan$ git fetch
remote: Enumerating objects: 121641, done.
remote: Counting objects: 100% (121641/121641), done.
remote: Compressing objects: 100% (29567/29567), done.
error: RPC failed; curl 18 transfer closed with outstanding read data remaining
fatal: the remote end hung up unexpectedly
fatal: early EOF
fatal: index-pack failed
caimeijuandeAir:local caimeijuan$ ```




