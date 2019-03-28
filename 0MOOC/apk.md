2015年12月29日，在river的帮助下，用qpython打的包，已经没法在现在的安卓系统上运行了。所以想重新打个包。搜索了一下，kivy出现的频率比较高。

[mac系统中kivy打包为apk安装包步骤](http://www.360doc.com/content/16/0331/16/13647213_546844872.shtml)

基本按照这里的指导做的。

## 安装Bulldozer

'
git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python setup.py install
'

建了个文件夹zhangda，初始化为buildozer项目：

`
mkdir zhangda
cd zhangda
buildozer init
`
生成了配置文件buildozer.spec

抄了他的helloworld程序。 


## 安装kivy  

[kivy 在mac上安装笔记 - 简书](https://www.jianshu.com/p/27278af8a92e)

step1:

`brew install pkg-config sdl2 sdl2_image sdl2_ttf sdl2_mixer gstreamer`

成功

step2:

`pip install Cython==0.26.1 `  

提示说本机已有Cython，但是版本是0.23.4，那就改为升级吧。

`python -m pip install --upgrade Cython`

还是提示本机已有Cython 0.23.4

step3:

`pip install kivy`

没想到这一个成功了，其他的方法倒是没成。
`Successfully built Kivy-Garden
Installing collected packages: Kivy-Garden, kivy
Successfully installed Kivy-Garden-0.1.4 kivy-1.10.1`

## 安装Java

执行`buildozer -v android debug`，错误提示是：  

`No Java runtime present, requesting install.`  

对话框提示是“您需要安装JDK才能使用‘Java’命令行工具。” 提示了一个网址如下。
从[Download Java for Mac OS X](https://www.java.com/en/download/mac_download.jsp)下载了安装。

安装完毕，重新执行buil这句，照旧。  

页面有一句提示：  

> When your Java installation completes, you may need to reload (Command+R) or quit(Command+Q) your browser in order to enable Java in your browser.

重启并没有用。  

[[Java] Mac安装JDK - 简书](https://www.jianshu.com/p/0036a344509e)  
按照这里的，下载了jdk12,安装成功。
在命令行中输入echo $SHELL ，输出/bin/bash则为bash  

用`open ~/.bash_profile`打开文件改写：export JAVA_HOME=$(/usr/libexec/java_home)

`source .bash_profile`  

最后用`java -version`出现了版本信息：  
`java version "12" 2019-03-19
Java(TM) SE Runtime Environment (build 12+33)
Java HotSpot(TM) 64-Bit Server VM (build 12+33, mixed mode, sharing)`  

再执行`buildozer -v android debug`，错误提示是：

`No buildozer.spec found in the current directory. Abandon.` 

这是目录不对。回到zhangda目录中去。  
安装java的错误已经没有了。终于回到正途上。  

## 解决。。。  

正途上的问题是什么呢？  

`# Command failed: /Users/caimeijuan/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager tools platform-tools
# ENVIRONMENT:
#     LANG = 'zh_CN.UTF-8'
#     TERM = 'xterm-256color'
#     Apple_PubSub_Socket_Render = '/private/tmp/com.apple.launchd.nEAsgn7OwM/Render'
#     SHLVL = '1'
#     OLDPWD = '/Users/caimeijuan/buildozer'
#     SSH_AUTH_SOCK = '/private/tmp/com.apple.launchd.2Knxb5wLi2/Listeners'
#     SECURITYSESSIONID = '186a9'
#     TERM_SESSION_ID = 'C7F8B4C8-997E-422D-A429-C61810C90FC5'
#     TERM_PROGRAM_VERSION = '421.1'
#     PWD = '/Users/caimeijuan/buildozer/zhangda'
#     SHELL = '/bin/bash'
#     LOGNAME = 'caimeijuan'
#     USER = 'caimeijuan'
#     XPC_SERVICE_NAME = '0'
#     HOME = '/Users/caimeijuan'
#     PATH = '/Users/caimeijuan/.buildozer/android/platform/apache-ant-1.9.4/bin:/Users/caimeijuan/anaconda/bin:/Users/caimeijuan/anaconda/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin'
#     XPC_FLAGS = '0x0'
#     JAVA_HOME = ''
#     _ = '/Users/caimeijuan/anaconda/bin/buildozer'
#     TMPDIR = '/var/folders/ll/hf0rtrgx4qb0vffp086qfkx80000gn/T/'
#     TERM_PROGRAM = 'Apple_Terminal'
# 
# Buildozer failed to execute the last command
# The error might be hidden in the log above this error
# Please read the full log, and search for it before
# raising an issue with buildozer itself.
# In case of a bug report, please add a full log with log_level = 2`  










