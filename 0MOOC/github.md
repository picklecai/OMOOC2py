# github 私人教程

## 1. Github绑定邮箱设成公开

## 背景

win7或win8

使用芝麻星系统，提示：
> 请在将github绑定邮箱设成公开后，用github账户登录

## 安装

在github的settings中，Email选项设置无果，后来发现是profile没仔细看，其中有Public Email。

## 配置

## 使用

## 体验


## 2. fork仓库建立issue  


## 背景

win7或win8  

大妈：  
> 最好是链接到自个儿仓库的专用 Issue 中  

## 问题  
发现自己的仓库里，fork来的都没有issue，只有自己建立的才有。  

## 解决  
初始搜索结果都是在说如何fork，查看github的help文件，也只有简单的步骤，对是否fork未提及。  

后来在知乎上看到了一个回答：  [在github上从别人那里fork一个new branch，为什么就没有Issue功能了？ - 匿名用户的回答 - 知乎](http://www.zhihu.com/question/26871860/answer/34576333)，原来是要在settings里设置的：  

![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-3/25322908.jpg)

另外，今天才发现，到[OpenMindClub/OMOOC2py](https://github.com/OpenMindClub/OMOOC2py)下去查看issues，可以避免[Dashboard](https://github.com/orgs/OpenMindClub/dashboard)里issue太多，找不到的情况。  

## 3. 将本地文件与远程仓库同步 

本地修改文件提交到远程，就在客户端点击sync就可以了。  

反之呢？昨天在家里更新了文件，今天到公司来，要读取这些更新，已经不能用clone再操作一遍了。  

尝试1：  `git fetch`  
结果：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/47493354.jpg)  

尝试2：  `git branch`与`git status`  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/27667853.jpg)  
 `git branch`没有什么用，但`git status`给出了提示，应该用`git pull`：   

尝试3： 

    git pull

![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/11797356.jpg)  

到本地查看，确实是最新的了：   
 
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/91678068.jpg)  

注意：尽管已经进了子目录，但是`git pull`是把整个repository下的更新都下载了的，这效果和在OMOOC2py根目录下是一样的。  

参考资料：  
[GitHub超详细图文攻略 - 韩曙亮 の 技术博客 - CSDN.NET](http://blog.csdn.net/shulianghan/article/details/18812279)