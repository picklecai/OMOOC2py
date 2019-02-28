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


