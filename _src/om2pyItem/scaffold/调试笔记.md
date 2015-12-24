# 调试笔记  

## 1. submit和button的区别  
[input type="submit" 和"button"有什么区别？ - 知乎](https://www.zhihu.com/question/20839977)  
> 在一个页面上画一个按钮，有四种办法：  
> 
>  `<input type="button" />` 这就是一个按钮。如果你不写javascript 的话，按下去什么也不会发生。  
> 
> `<input type="submit" />` 这样的按钮用户点击之后会自动提交 form，除非你写了javascript 阻止它。   
> 
> `<button>` 这个按钮放在 form 中也会点击自动提交，比前两个的优点是按钮的内容不光可以有文字，还可以有图片等多媒体内容。（当然，前两个用图片背景也可以做到）。它的缺点是不同的浏览器得到的 value 值不同；可能还有其他的浏览器兼容问题（葛亮）。  
> 
> 其他标签，例如 a, img, span, div，然后用图片把它伪装成一个按钮。  

用法：  
> 表单数据这个特性，是无法混淆的。`<button>`无法把自己当成Form的数据。  
> 所以，如果只是个单纯的按钮，触发一些画面动作，请使用`<button>`；  
> 反之，会把画面的数据提交给Server的，一般用`<input type="submit" />`，当然`<button>`+JS也完全可以取代。   

[html中submit和button的区别(总结)_劤步_新浪博客](http://blog.sina.com.cn/s/blog_693d183d0100uolj.html)  
写区别时和其他说法差不多：  
> INPUT   type=submit 即发送表单,按回车提交表单   
> INPUT   type=button 就是单纯的按钮功能,提交的是innerTEXT  

> submit:特殊的button，会自动将表单的数据提交，onClick方法不加return 会自动提交，并不会起到约束的作用。 
> 所以，使用submit时需要验证请加 return true或false.    
例：`<input type="submit" name="Submit" value="注 册" onClick=" return check();">`，在JS中判断的时候 写return true; 或者 return false;  

但提到了form的写法：  

    type="submit"  
	<form id="frm1" action="<%=request.ServerVariables("Script_Name")%>"  
	 method="post" onSubmit="return check_submit(this)">
	<input id="btnconfirm" type="submit" value="确定" name="btnconfirm"></form>

> `<input type="submit" name="b1" value="提交" onClick="bt_submit_onclick()">`
执行完onClick，转到action。可以自动提交不需要onClick,所以说onclick这里可以不要。 

## 2. action和onSubmit的区别  
[form表单中action和onsubmit的表单检查区别 - Lai18.com IT技术文章收藏夹](http://www.lai18.com/content/928916.html)  
> onsubmit和action两个都是提交时触发的不过：onsubmit是在表单中的确认按钮被点击时触发的，一般是js函数，而action是在按钮被点击之后触发的，一般是触发前台提交到后台的请求，而引起后台的回应。  

## 3. get和post的区别   
[Tutorial — Bottle 0.13-dev documentation](http://bottlepy.org/docs/dev/tutorial.html#request-data)   

> The action attribute specifies the URL that will receive the form data. method defines the HTTP method to use (GET or POST).   
> With method="get" the form values are **appended to the URL** and available through BaseRequest.query as described above. This is considered insecure and has other limitations, so we use method="post" here. If in doubt, use POST forms.

## 4.数字形式的时间转为时间格式  
[Python time strptime() Method](http://www.tutorialspoint.com/python/time_strptime.htm)  

    #!/usr/bin/python
	import time
	
	struct_time = time.strptime("30 Nov 00", "%d %b %y")
	print "returned tuple: %s " % struct_time

格式符意义：  
> %a - abbreviated weekday name  
%A - full weekday name  
%b - abbreviated month name  
%B - full month name  
%d - day of the month (01 to 31)  
%H - hour, using a 24-hour clock (00 to 23)  
%I - hour, using a 12-hour clock (01 to 12)  
%M - minute  
%y - year without a century (range 00 to 99)  

## 5. baby页面  

html文件中，  

    <form action="/baby.html" method="GET">  
方法定为GET。  

main.py中，  

    @app.route('/baby.html', method='GET')  
方法定为GET。  

运行500错误：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-16/29745709.jpg)  

原因是加号不能用在这里。  

之前只看到405或500，没发现问题代码。  

加上str（）转换，代码改为：  

    birthtime = time.strptime(str(request.forms.get('date'))+'/'+str(request.forms.get('month'))+'/'+str(request.forms.get('year')), "%d/%m/%Y")  

500错误为：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-17/29359471.jpg)  

查看striptime的文档：  
> time.striptime(string[, format])  

参数要求是string。现在str()转换出来的被系统认为是none。  

绕过这个问题，代码改为：  

     birthtime = time.strftime("%d/%m/%Y %H:%M:%S")  

现在问题代码是：  

    data = name.decode('utf-8'), gender.decode('utf-8'), birthtime.decode('utf-8')  

500提示是：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-17/35234971.jpg)  

再绕过去，代码改为：  

    data = name, gender, birthtime  

界面不再500.  
打开baby页面，填入信息，打印信息刚出现即消失。可以看到打印出来的信息是：  

> none,none,(当前时间)  

打印信息还可以看到的问题是：这里的打印方法用了和打印记录相同的方法，但是现在只录入一个宝宝，不应该有多行记录。应该是录入一次信息后，后来都变成修改模式保存最新。

这说明不但birthtime的写法被认为是none，连界面读取出来的text也被认为是none。  

另外，由于baby页面是get方法，所以可以看到不再500之后的baby页面网址：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-17/22143236.jpg)    
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-17/78667476.jpg)  
所填参数悉数体现在url中。  

[执行python脚本时，返回：AttributeError: 'NoneType' object has no attribute 'open_session'，原因？_百度知道](http://zhidao.baidu.com/question/499301263.html)  
这里说：  
> NoneType的本意是 （变量的值是）空的值.所以，值都是空的了，当然没有相关的各种属性  

所以name和gender可能没有收到传值，所以是none。但是为什么又已经被get到了url中了呢？  

重新考虑一下，在刚刚打开baby页面时，确实这些值都是none。而现在程序走的顺序是：先确认这些值不是none，才允许打开页面，再输入。应该做到让baby页面打开时，不去碰这一段代码，直接打开。  

在首页，首先用get方法打开的是“/”页面，然后采用post方法打开并返回“/index”,运行和输入数据相关的save函数。所以打开“/”时，不会产生任何none类错误。  

---
12.23问教练：  
输入无法传递到数据库（none,none,none）里去，归根结底还是method。  
观察已经成功接受数据并显示数据的/页面和/history.html，/的method是get，/index的method是post，/history的method是get。/页面管数据输入，接受键盘敲入数据，/history管数据输出，从数据库里读出来显示在页面上。这里的/index.html如果独立在url中打出来，就显示405方法错误。如果把/index的方法改为get，数据输入回车后，马上就返回这个错误的405index页面，这时history就无法接受到数据了，因为中间错误导致数据没有进入数据库。  
在7w作业里，没有history页面，/输入后，在index页面输出结果。方法是：负责输入的/是get，负责输出的/index是post。  
这两个成功案例，/和/index居然是两个页面，可以用两个方法，让我觉得根目录/是个逆天的神奇存在。
现在在baby项目里，baby页面需要负责输入，所以方法是get，同时它还要负责输出。结果就是从baby页面的输入框输入的内容，不能被正确存储到数据库里，从而导致页面也不能输出正确的内容。因为方法是get，所以输入内容可以在url中看到。  
为什么url都能接受的内容，就没有正确进入数据库呢？感觉这个和用了submit还是用了button的关系不大。submit在这里的作用就是提交form。用不用submit，url都已经获得了这个输入内容，它只是没有进入数据库，或者说它总是把空数据传入数据库。  
之所以会插入js，是因为我觉得这个页面需要这样一个交互效果：addnew按钮要把填写宝宝信息数据的表单显示出来，填完表单数据后提交，又需要返回刚刚填入的宝宝信息数据。并且为了可修改，还需要返回一个修改按钮（setting）。这三个按钮：addnewbaby，savebaby，setting，唯一涉及到提交表单的就是savebaby，所以它是submit。但是设它为submit后，返回的内容一闪而过。改为button则不会。除了一闪而过外，submit可以直接enter提交，而button不会，这也是它们的主要区别。在这里，都没有解决为什么会传空数据给数据库的问题。  
我能想到的可能因素就是页面的方法和按钮的type，但是对其中的道道和所以然很模糊。  

猜测如果有一个地方，能让baby.html在接受了数据后方法变成post的话，这事儿就成了。  

刚才说的所有method，都是在main.py中。  
现在把baby.html里form的方法，从get改为post。main.py里，在原来的点击baby方法get之下，又写了一个路由，方法post，函数就是savebaby搬下来。运行结果是：提交后500错误，命令行端没有提示。但是查看baby数据库，发现输入内容读进数据库里了。不再none了。  

手机端有500提示（电脑版qpython没有）：  
> Bottle v0.13-dev server starting up (using MyWSGIRefServer())...
Listening on http://localhost:8800/
Hit Ctrl-C to quit.

> localhost - - [23/Dec/2015 15:44:38] "HEAD / HTTP/1.1" 200 0   
> localhost - - [23/Dec/2015 15:44:38] "GET / HTTP/1.1" 200 4408  
> localhost - - [23/Dec/2015 15:44:42] "GET /baby.html HTTP/1.1" 200 5884  
> Traceback (most recent call last):  
> File "/storage/emulated/0/com.hipipal.qpyplus/lib/python2.7/site-packages/bottle.py", line 850, in _handle  
    return route.call(**args)  

> File "/storage/emulated/0/com.hipipal.qpyplus/lib/python2.7/site-packages/  bottle.py", line 1721, in wrapper  
    rv = callback(*a, **ka)  

> File "/storage/emulated/0/com.hipipal.qpyplus/projects/babyrecord/main.py", line 107, in savebaby  
    createbaby(data)  

> File "/storage/emulated/0/com.hipipal.qpyplus/projects/babyrecord/main.py", line 72, in createbaby  
    cursor.execute('insert into babyinfo (name, gender, birthtime) values (?,?,?)', data)  

> ProgrammingError: You must not use 8-bit bytestrings unless you use a text_factory that can interpret 8-bit bytestrings (like text_factory = str). It is highly recommended that you instead just switch your application to Unicode strings.  

> localhost - - [23/Dec/2015 15:45:07] "POST /baby.html HTTP/1.1" 500 750  

把baby.db删除，重新运行程序，然后查看新生成的baby.db，发现其中有两行数据：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-23/99086390.jpg)    

第一行none数据，应该就是还不能把decode放出来的原因。不能把decode放出来又造成了上面这个500错误中说的“You must not use 8-bit bytestrings”。  

[python - pysqlite insert unicode data 8-bit bytestring error - Stack Overflow](http://stackoverflow.com/questions/5839335/pysqlite-insert-unicode-data-8-bit-bytestring-error)  

> That is one of the most helpful error messages that I've ever seen. Just do what it says. Feed it unicode objects, not UTF-8-encoded str objects. In other words, lose the .encode('utf-8') or maybe follow that later by decode('utf-8')  


练习if-else：  
代码修改：  

    @app.route('/baby.html', method='GET')
	def baby():
	    babylabel=savebaby()
	    print babylabel
	    if babylabel ==None:
	        return  template(ROOT+'/baby.html')
	
	@app.route('/baby.html', method='POST')
	def savebaby():
	    name = request.forms.get('name')
	    gender = request.forms.get('gender')
	    birthtime = time.strftime("%d/%m/%Y  %H:%M:%S") #time.strptime(str(request.forms.get('date'))+'/'+str(request.forms.get('month'))+'/'+str(request.forms.get('year')), "%d/%m/%Y")
	    # data = name.decode('utf-8'), gender.decode('utf-8'), birthtime.decode('utf-8')
	    if name==None or gender==None or birthtime==None:
	        return None
	    else:
	        data = name, gender, birthtime.decode('utf-8')
	        createbaby(data)
	        return readbaby()

运行结果：  
页面500，终端提示信息为：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-23/66351817.jpg)  

在reture语句中加入`babylabel = ''`可以点开baby.html了。  

    @app.route('/baby.html', method='GET')
	def baby():
	    babylabel = savebaby()
	    print babylabel
	    if babylabel == None:
	        return  template(ROOT+'/baby.html', babylabel='')

继续运行，输入baby信息，500错误：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-24/6826547.jpg)  

none输出了两遍，到post时500了。  

补充完整的print变量语句：  

    def baby():
	    babylabel = savebaby()
	    print 'babylabel is: %s'%(babylabel)
    ……  
    def savebaby():
	    name = request.forms.get('name')
	    print  'name is: %s'%(name)
	    gender = request.forms.get('gender')
	    print  'gender is: %s'%(gender)

运行结果为：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-24/74796126.jpg)  

到post出错，想起来到了baby信息填完后，没有返回baby页面。  
代码改为：  

        else:
	        data = name, gender, birthtime.decode('utf-8')
	        createbaby(data)        
	        return template(ROOT+'/baby.html', babylabel=readbaby())
再运行，确实通过了：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-24/42651244.jpg)  

运行，baby2页面无内容。单独打开baby2，也没有内容。  
把babylabel和按钮setting从div2中放出来，有了。  