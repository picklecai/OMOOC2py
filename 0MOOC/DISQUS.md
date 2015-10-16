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
