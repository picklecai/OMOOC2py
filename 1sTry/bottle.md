# bottle 私人教程

## 背景

win8

## 安装

下载bottle.py，放在工作目录下。  
[下载地址](https://pypi.python.org/pypi/bottle/0.12.9)  

## 配置

## 使用

在代码中加入import bottle即可使用。

## 体验

### @route()  
route函数在class Bottle下面，函数：  

    def route(self, path=None, method='GET', callback=None, name=None,
              apply=None, skip=None, **config):  

使用中：  

    from bottle import route, run, template

	@route('/hello/<name>')
	def index(name):
	    return template('<b>Hello {{name}}</b>!', name=name)
	
	run(host='localhost', port=8080)

这里route后面的参数，可能是函数定义中的path。  
函数里关于route的说明：  

            """ A decorator to bind a function to a request URL. Example::

                @app.route('/hello/:name')
                def hello(name):
                    return 'Hello %s' % name

            The ``:name`` part is a wildcard. See :class:`Router` for syntax
            details.

            :param path: Request path or a list of paths to listen to. If no
              path is specified, it is automatically generated from the
              signature of the function.
            :param method: HTTP method (`GET`, `POST`, `PUT`, ...) or a list of
              methods to listen to. (default: `GET`)
            :param callback: An optional shortcut to avoid the decorator
              syntax. ``route(..., callback=func)`` equals ``route(...)(func)``
            :param name: The name for this route. (default: None)
            :param apply: A decorator or plugin or a list of plugins. These are
              applied to the route callback in addition to installed plugins.
            :param skip: A list of plugins, plugin classes or names. Matching
              plugins are not installed to this route. ``True`` skips all.

            Any additional keyword arguments are stored as route-specific
            configuration and passed to plugins (see :meth:`Plugin.apply`).
        """

主要作用是：将特定的功能绑定到请求的url上。  
提到：  
> HTTP method (`GET`, `POST`, `PUT`, ...)   

这些是http方法。搜“http方法 get”，在[HTTP 方法：GET 对比 POST](http://www.w3school.com.cn/tags/html_ref_httpmethods.asp)：  
> 两种 HTTP 请求方法：GET 和 POST  
> 在客户机和服务器之间进行请求-响应时，两种最常被用到的方法是：GET 和 POST。  
 - GET - 从指定的资源请求数据。  
 - POST - 向指定的资源提交要被处理的数据

在bottle里的函数定义：  

        def get(self, path=None, method='GET', **options):
	        """ Equals :meth:`route`. """
	        return self.route(path, method, **options)

	    def post(self, path=None, method='POST', **options):
	        """ Equals :meth:`route` with a ``POST`` method parameter. """
	        return self.route(path, method, **options)
	
	    def put(self, path=None, method='PUT', **options):
	        """ Equals :meth:`route` with a ``PUT`` method parameter. """
	        return self.route(path, method, **options)
	
	    def delete(self, path=None, method='DELETE', **options):
	        """ Equals :meth:`route` with a ``DELETE`` method parameter. """
	        return self.route(path, method, **options)
get是函数，GET是http方法。

教练培炎关于bottle安装与否的解释：  

> python import一个库，必须到一些地方去找这个库，这些地方就是它的搜索路径，之所以可以放在同一个目录，是因为当前目录总是默认的搜索路径之一，默认路径还包括系统的标准库路径，如果有特殊需求，可以对搜索路径进行设置。  
> 目录什么的，就是个表象，根本的是这个东西能不能被找到，与主程序目录相同只能说是自然且合理的选择。“所以它的搜索过程是先当前工作目录然后才是py程序所在目录？”据我观察，是的，但不排除版本和系统可能有差异。    
