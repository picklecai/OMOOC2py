# sae 私人教程

## 背景
win8。   
已安装git命令行。
## 安装
新浪云已用微博帐号注册过。

从github下载源码安装 

    $ git clone https://github.com/sinacloud/sae-python-dev-guide.git
    $ cd sae-python-dev-guide/dev_server
    $ python setup.py install
## 配置
进入新浪云应用（sae），代码管理，创建版本1。选择操作“编辑代码”，则进入chrome版的SAE Editor。可以直接开始编辑两个文件： 
 
config.yaml  
<pre><code>
    name: picklecai
    version: 1
</pre></code>

index.wsgi  
<pre><code>
import sae
def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/plain')])
    return ['Hello, my notebook!']
application =sae.create_wsgi_app(application)
</pre></code>

## 使用
浏览器进入地址：http://picklecai.sinaapp.com/：

已显示内容“Hello, my notebook!”

## 体验

纠结于代码管理到底是svn还是git。svn以前用过，这次并没有装。git本地有。但是不知道怎么显示了svn，并提示说除非新建一个项目，否则不能改git。  
没想到直接开始创建版本，编辑代码后，直接进入了两个文件的编辑状态，绕过去svn或git的问题了。  