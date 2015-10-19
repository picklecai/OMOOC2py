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

## 配置

## 使用

## 体验  
Package Control安装好之后，其他插件是按回车的时候就开始安装的。刚开始没注意状态栏的安装进展，以为只是最后返回一个插件解释。通过Remove命令才知道已经安装成功。
