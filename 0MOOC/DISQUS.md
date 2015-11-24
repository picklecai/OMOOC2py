# DISQUS 私人教程

## 背景

大妈：
> 并配置好 DISQUS 插件令大家可评注

## 安装
1. 到https://disqus.com 中注册一个帐号“picklecai” (设定与github、gitbook用户名相同，可能不同也没有关系)。  
2. 在github根目录下上传book.json文件。  
文件内容为：  
<pre><code>
  {
    "plugins": ["disqus"],
    "pluginsConfig": {
      "shortName": "picklecai"
      }
  }    
</pre></code>

## 配置

在gitbook中omooc2py这本书的settings里，点开book configuration：  

<pre><code>"shortName": "openmind2py"</pre></code>

其中的用户名"openmind2py"改成**picklecai** (即与github的book.json文件中的disqus用户名一致)

## 使用

## 体验

在用户名设置上犯了两个错误：  
1. github的book.json文件中，用户名写作"<picklecai>"  
2. gitbook的book  configuration中，用户名是"openmind2py" (大妈所设定的他的用户名)，未改成自己的。  

错误结果是：未登录状态下看这本书，结果是404，页面提示是未发布（not published）。  

## 11.24补充  
错误提示：  
> Your book’s latest update failed to build.  

查看细节：  
> ![](http://i12.tietuku.com/9b684c337a282321.png)
> ![](http://i12.tietuku.com/97505e458536ab4d.png)

插件安装一直是正确的，直到最后一步提示：  
> > Error: Configuration Error: pluginsConfig.disqus.shortName is required  

book.json内容：  
<pre><code>
    {"title": "开智学院 编程课程 Python 入门班 私人教程模板",
    "version": "15.9.18,2020",
    "description": "OMOOC.py tutorial for teching",
    "author": "OMOOC-support <omooc-support@googlegroups.com>",

    "plugins": ["disqus"],
    "pluginsConfig": {
            "shortName": "picklecai"

     }
    }
</pre></code>  

shortName并未缺少。

1. 到disqus.com上检查帐号picklecai，提示邮箱未验证。试着在联合早报某新闻下发评论，未验证邮箱无法发评论。发验证邮件，发了好几次，最后统一在垃圾箱找到（垃圾箱无未读提示），邮箱为163邮箱。  
2. 验证成功后，可以发评论了。 红色警告的错误提示并未消失。点击“restart this build”继续错误。   
3. 研究book.json里的shortName写法，重新粘贴大妈的原始内容（替换为picklecai）。错误不变。  
4. 查看`https://github.com/GitbookIO/plugin-disqus` 和`https://plugins.gitbook.com/plugin/disqus`的内容，最后发现其中代码在`"pluginsConfig":`后还嵌入一层disqus。修改book.json如下：  
<pre><code>
    {"title": "开智学院 编程课程 Python 入门班 私人教程模板",
    "version": "15.9.18,2020",
    "description": "OMOOC.py tutorial for teching",
    "author": "OMOOC-support <omooc-support@googlegroups.com>",

    "plugins": ["disqus"],
    "pluginsConfig": {
        "disqus": {
            "shortName": "picklecai"
        }
     }
    }
</pre></code>
到gitbook刷新，这个update未出现红色。其他仍然红色。  
restart其他，错误如故。  
想着可能这一层`"disqus"`并不重要，所以没有解决问题。  
