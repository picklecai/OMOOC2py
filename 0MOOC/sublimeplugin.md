# Sublime插件安装 私人教程

## 背景  
> M$ 用户,请允许俺致以最大的同情, 然后,敬请自行先安装好:  
- activestate.com/activepython  
- Sublime Text 2  
  - 并配置好 Python 支持插件  

## 安装  
### 1.安装 Package Control
1.1. 打开菜单 View - Show Console 或者 ctrl + ~ 快捷键，调出 console  
1.2. 将以下 Python 代码(for sublime text 3)粘贴进去并 enter 执行  
<pre><code>
import urllib.request,os; 
pf = 'Package Control.sublime-package'; 
ipp = sublime.installed_packages_path(); 
urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); 
open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ','%20')).read())
</pre></code>
1.3. 重启Sublime Text  

### 2.安装插件
Package Control安装完毕后，可以使用快捷键 ctrl+shift+p (Win, Linux)打开。  
输入 Package Control: Install Package 回车, 输入 package 名再回车，会自动进行安装。 
本机环境安装了Pylinter，Anaconda，SublimeGit，Python Flake8 Lint。可以通过Remove看，也可以通过Preferences菜单的Package Settings查看。

### 3. 破解  
mac下使用了3103版本，找到[这里](http://9iphp.com/web/html/sublime-text-3-license-key.html)的代码粘贴进licence：  

	Michael Barnes
	Single User License
	EA7E-821385
	8A353C41 872A0D5C DF9B2950 AFF6F667
	C458EA6D 8EA3C286 98D1D650 131A97AB
	AA919AEC EF20E143 B361B1E7 4C8B7F04
	B085E65E 2F5F5360 8489D422 FB8FC1AA
	93F6323C FD7F7544 3F39C318 D95E6480
	FCCC7561 8A4A1741 68FA4223 ADCEDE07
	200C25BE DBBC4855 C4CFB774 C5EC138C
	0FEC1CEF D9DCECEC D3A5DAD1 01316C36

菜单变成了`remove licence`，应该是成功了。

## 配置

### 4. octave文件语法高亮
在[这里](http://blog.sina.com.cn/s/blog_71e26e290102v3ad.html)看到配置：  

	{
	    // Change path to matlab.exe per local settings
	    "cmd": ["D:/MATLAB/R2013a/bin/matlab.exe", "-nodesktop", "-nosplash",
	            "-r", "\"run('$file')\""],
	    "selector": "source.m",
	    "working_dir": "${project_path:${folder}}"
	}
	
需要程序位置：  
在[这里](http://www.2cto.com/os/201203/124833.html)查看octave程序位置。

保存为octave名字，usr路径下。

运行，无效，找不到这样的路径：  

	[Errno 2] No such file or directory: '/Applications/octave-cli'
	[cmd: ['/Applications/octave-cli', '-nodesktop', '-nosplash', '-r', '"run(\'/Users/caimeijuan/github/mlearn/assign/ex4/nnCostFunction.m\')"']]
	[dir: /Users/caimeijuan/github/mlearn/assign/ex4]
	[path: /usr/bin:/bin:/usr/sbin:/sbin]
	[Finished]

发现菜单：`view-syntax-matlab`  
点选，没反应。  

过了些时，sublime关掉了（嗯， 其实我好几个月都没有关sublime），重新打开程序时，又想起了去点击了上面这个菜单。界面瞬间变了：所有注释都是灰色。   

哦也～～～  上次没成功只是因为我没有重新启动程序。  

（copyright：3103）  

野教程害人不浅。

## 使用

## 体验  
Package Control安装好之后，其他插件是按回车的时候就开始安装的。刚开始没注意状态栏的安装进展，以为只是最后返回一个插件解释。通过Remove命令才知道已经安装成功。


