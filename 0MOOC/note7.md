# Note for 20151126 19:42  
## 表扬 
  
bambooom：竹子对google的使用心得。  
jeremiazhang：不纠结。  

## fabric  
关键词：DSL，本地，远程，批量，分组  
具体用处：自动运行，可用于自动测试，批量测试等。  

## QPy  
关键词：SL4A，QPyPi，.apk  
具体用处：在移动端开发的python。

## Task  
关键词：root，BusyBox，SSHDroid，abd

## team  
组团输出一个作品，团是团队，不是团伙。  
AKA：All know all.  
关键词：公示，定档，顺序，能技  

## Q&A  


##印象最深  

### 1. 不纠结：  
普通人在古稀之后不纠结，因为没条件纠结了。  （好逗）  
打草才能惊蛇，得打草！  

### 2. Qpy电脑端开发  

思考大妈说的能不能在电脑上开发。  

### 思路1：  
在pc上写好程序，放到手机上Q文件夹中运行。  

查看样例程序地址，手机连接电脑寻找这个地址，没有。 
地址是：

    /com.hipipal.qpyplus/scripts/helloworld.py

在手机中可以看到`com.hipipal.qpyplus`文件夹下有五个子文件夹： projects,snippets,lib,scripts,cache。  

到电脑上看只有projects一个。  

### 思路2：  
寻找电脑上的模拟环境。  
找到了一个电脑版的安装程序：[QPython电脑版下载v1.0.4_红软基地](http://www.rsdown.cn/down/37910.html)   
文件形式是exe的，冒险下载安装，果然是QPython（不是病毒）。  

安装中要求装framework3.5（其实本机早已安装过framew4.0），安装。最后成功。界面和手机一样。  


### 思路3：  
手机上所装qpy有qedit4web.py程序，开发者说这是为了让用户在pc上开发。运行后会出现网址，将这个网址在pc浏览器端打开即可。  

试验：每次运行，pc端都无法打开这个url。  
将手机用数据线连到pc端，仍然无法打开运行时所产生的url。  
手机端浏览器打开这个网址，可以打开。但这样不是失去意义？  

在电脑上装的qpy，并没有这个程序。  

开发者在视频中，使用了推送到手机的功能。但他又说自己用的虚拟机。根据前面描述，他可能用了qedit4web程序。  

发现river的一篇文章：[如何使用QPython开发Android应用 |QPython |Python for Android](http://codelab.qpython.org/qpythoncodelab/1st-qpython-app-for-android.html)

最后发现，直接在电脑端程序中写代码，点击运行，即可查看效果。  