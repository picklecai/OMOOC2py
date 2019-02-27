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

