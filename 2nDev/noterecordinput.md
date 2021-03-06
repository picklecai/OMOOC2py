# App版简易笔记本调试笔记  

为了“诚意”起见，这期作业无论如何也得完成。至少完成到纯APP状态（无命令行，无微信）。  

## 参考代码：  

[picklecai的4w作业](https://github.com/picklecai/OMOOC2py/tree/master/_src/om2py4w/4wex0)  
[River的BusHelper](https://github.com/qpython-apps/BusHelper)  
[xpgeng的8w作业](https://github.com/xpgeng/OMOOC2py/tree/master/_src/om2py7w/7wex0/mydaily)   
[bambooom的8w作业](https://github.com/bambooom/OMOOC2py/tree/master/_src/om2py7w/7wex0)  

## 环境及工具配置  
略。见：  
[QPython笔记](0MOOC/QPython.md)  
[Fabric笔记](1sTry/fabric.md)  

## 改代码  

先抄了一遍bushelper，反复研究，点击项目运行，html页面能呈现，但是不能处理任何动作，点击没有反应。  

参考[OMOOC2py/main.py at master · xpgeng/OMOOC2py](https://github.com/xpgeng/OMOOC2py/blob/master/_src/om2py7w/7wex0/mydaily/src/main.py)代码，做了一个关于sqlite的修改：  
建好db文件，而不是用时再建。 （起初仿照读取文件时的做法，用了if exist，但是运行没有反应） 

又看了[OMOOC2py/main.py at master · bambooom/OMOOC2py](https://github.com/bambooom/OMOOC2py/blob/master/_src/om2py7w/7wex0/main.py)，发现也可以不新建，代码是：  

 `CREATE TABLE if not exists diary`  

发现两位都没有用到asset文件夹，于是重新整理index.html，把其中引用了script的部分都去掉。样式表css图它好看，没删。  

同学提到日志，但我觉得我这里并没有看到错误提示。后来发现是qpy下有个位置，无论运行成功与否，都有的提示。上述html文件重新整理，即根据日志文件返回的代码，直到返回都是200为止。

### 1.  
修改过程中重新在index.html中用了form，于是再改main.py的request。改错了，forms写成了form：  

    def save():
	    newline = request.forms.get('newline')
	    nowtime = time.time()
	    data = nowtime, newline
	    inputnewline(data)
	    historylabel = printhistory()
	    return template(ROOT+'index.html', historylabel)

这个错误就是根据日志文件找到的。按照以前的思路，只告诉了`500 internal server err`，那就发现不了了。  


### 2.
再运行，新的错误是：  

![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/75354965.jpg)  

说创建的数据库里并没有record这个表。  不过数据库已经在命令行端测试过了，有test记录，怎么会没有表呢？  

换回bambooom的做法，在main.py里创建。  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/31682093.jpg)  
新添加这一句，以代替原先已经创建好的：   

    cursor.execute('create table if not exists record (time text, record varchar)')

### 3.  
500错误变成了这样：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/24126289.jpg)  

指向notebookappindex.html文件，没有更细节的东西了。  

路径下确实没有这个文件，但现在找不到是哪里用它。main.py里没看到。  

考虑可能是哪里少了个点，没想到在project下面看到了新建立的db文件：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/10999767.jpg)  
一看命名这架势，懂了。原来的index不起作用了，它要求这样的名字。那一定是路径问题。  

尝试去掉所有`ROOT+`，直接挂了：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/6023766.jpg)  

恢复`ROOT+`，把它后面所加目录缺少`/`的补起来。  

### 4.  
再运行，新的错误是：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/94998320.jpg)  
这是啥呢？  

    database disk image is malformed  

Google的结果：[SQLite出现database disk image is malformed(11)的处理 : sunnyu](http://www.sunnyu.com/?p=201)  

> SQLite有一个很严重的缺点就是不提供Repair命令。  
导致死亡提示database disk image is malformed  
它的产生有很多种可能，比如，磁盘空间不足，还有就是写入数据过程中突然掉电等。  
官方对产生原因的一些[说明](http://www.sqlite.org/lockingv3.html#how_to_corrupt)  

这一页还说可以先导出再导入，一般可以用。  

于是我把原先辛辛苦苦传上去的文件删了，解决了。    

### 5.   
再运行，不出错了。但是：label并没有打印记录。  

日志文件全200：   
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/63709297.jpg)  

考虑到printhistory是打印之前历史记录，再运行一次。    

无论再输入点击save，还是再运行，都同样表现，不打印，不出错。  

#### 5.1 查看db文件  
  
把db文件搞下来看看吧。    
改py复制法不起作用了。    

把新的main.py和index.html通过qq发送到手机上，转存到qpy的project目录里，在notebookapp文件夹中，替代上次传入的文件。  

奇怪的事情发生了：   
  
由于运行没有变化，而且界面和电脑上看到的不一样，所以打开main.py看了一下，发现是上次的代码。但是打开文件目录，又显示文件是12-7。在文件目录里可以通过手机浏览器打开index.html，也是和电脑上一样的。  

为什么项目文件夹中的文件并未被替代呢？如果是目录搞错的话，那12-4也不能正确传入啊？  

用qq又重新传了一次文件，打开看没变化，不知道怎么搞的，运行了第二次时，成了。产生了db文件，打开main.py一看，新的代码。  

把db发回电脑，用fab查看，确实是新生成的数据。   

注意：数据表里的时间是**unix时间戳**。 这也可能是导致无法打印的原因。    

####  5.2 查看label代码  
db文件不错，说明存储成功。现在问题肯定是在label代码上了。   

print函数：  

    def printhistory():
	    conn = sqlite3.connect(ROOT+'/noterecord.db')
	    cursor = conn.cursor()
	    cursor.execute('select * from record')
	    return cursor.fetchall()

save函数：  

    @app.route('/index.html', method='POST')
	def save():
	    newline = request.forms.get('newline')
	    nowtime = time.time()
	    data = nowtime, newline
	    inputnewline(data)
	    historylabel = printhistory()
	    return template(ROOT+'/index.html', historylabel)  

问题应该出现在最后两句：  

    historylabel = printhistory()
    return template(ROOT+'/index.html', historylabel)

将数据库查询结果直接硬性复制给标签名（在index.html中，将label的name赋值为historylabel），肯定不对。  

Google“html label赋值”：  
[javascript 怎么给页面里的label赋值?-CSDN论坛](http://bbs.csdn.net/topics/90426983)  
> 在html中，label是没有value属性的，他与div以及其他大部分html元素一样，有innerText和innerHTML属性。  

更改代码：  

    historylabel.innerText = printhistory()
    return template(ROOT+'/index.html', historylabel)  

## 6. 
运行，很高兴地又迎来了500错误，这次有详细日志：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/32521026.jpg)  

说：问题在于标签label的name"historylabel"未定义。  

代码改成：   

    request.forms.get('historylabel').innerText = printhistory() 
    records = request.forms.get('historylabel').innerText
    return template(ROOT+'/index.html', records)  

运行日志说：  

![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/50692524.jpg)  

代码改成：  

    request.forms.label('historylabel').innerText = printhistory() 

日志说：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/86432141.jpg)  

> 在Python中，出现'unicode' object is not callable的错误一般是把字符串当做函数使用了。
> ——[[Python] 'unicode' object is not callable - igody - 博客园](http://www.cnblogs.com/xiongjiaji/p/3615943.html)

仿照两位，改html代码为%for： 

    <div>
		</br>History records:</br>
		% for i in historylabel:
        	{{i[0]}}: {{i[1]}} </br>
    	% end
	</div>	

改main.py为：  

    records = printhistory() 
    return template(ROOT+'/index.html', historylabel=records)  

这回日志不但继续500，而且提示信息变长了，但归根结底就是说：historylabel未定义：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/85542932.jpg)  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-7/85257077.jpg)  

回到自己的思路：  
代码改成：  

main.py  

    historylabel.innerText = printhistory() 
    return template(ROOT+'/index.html', historylabel

index.html  

    <div>
		</br>History records:</br>
		<label name= "historylabel"> </label>
	</div>		    

界面运行起来了。点击save，继续出错。错误日志：  

![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-8/74395467.jpg)  
换了个地方说变量未定义,回到main.py里来说了，所以html运行起来了。

---
插入：  
name和id的区别  
[细说HTML元素的ID和Name属性的区别 -birdshome博客](http://www.cnblogs.com/birdshome/archive/2005/01/31/99562.html)  
> 用途1: 作为可与服务器交互数据的HTML元素的服务器端的标示，比如input、select、textarea、和button等。我们可以在服务器端根据其Name通过Request.Params取得元素提交的值。  

---

html代码不动，main.py代码改为：  

    request.forms.post('historylabel').innerText = prinsthistory()

运行错误日志为：  

![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-8/33572857.jpg)  

同代码 `request.forms.label('historylabel').innerText = printhistory() `结果。  

去掉“innerText”，界面不能运行了，错误日志为：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-8/46378526.jpg)  

[Python: Cannot Assign Function Call - Stack Overflow](http://stackoverflow.com/questions/5964927/python-cannot-assign-function-call)给出的解释：  
> You are attempting to assign a value to a function call, as the error says. 

值不能赋给功能模块，字符串也不能当函数用。 

---
搁置  
回头解决unix时间戳及uft8编码  

试修改几次，最终代码如下：  

    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
    data = nowtime.decode('utf-8'), newline.decode('utf-8')  

抛弃一开始的time.time()  

---

试了加history链接，到时候点击history链接去访问结果。但是显示405错误。后放弃。  

回到单页面来：  

代码：  

    @app.route('/index.html', method='POST')
    def save():
	    newline = request.forms.get('newline')
	    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
	    data = nowtime.decode('utf-8'), newline.decode('utf-8')
	    inputnewline(data)
	    historylabel = "".join(printhistory())
	    return template(ROOT+'/index.html',historylabel

错误日志： 
 
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-8/91419439.jpg)  

Google “sequence item 0: expected string, tuple found” ：  

[使用list和tuple - 廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386819318453af120e8751ea4d2696d8a1ffa5ffdfd7000)解释list和tuple区别，说tuple不能更改。  

[python - TypeError: sequence item 0: expected string, int found - Stack Overflow](http://stackoverflow.com/questions/10880813/typeerror-sequence-item-0-expected-string-int-found)  
说：  
> `string.join connects elements inside list of strings, not ints.`  
> Use this generator expression instead :  
>   `values = ','.join(str(v) for v in value_list)`

所以改为：  

    @app.route('/index.html', method='POST')
	def save():
	    newline = request.forms.get('newline')
	    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
	    data = nowtime.decode('utf-8'), newline.decode('utf-8')
	    inputnewline(data)
	    notelist1 = printhistory() 
	    historylabel = "".join(str(v) for v in notelist1)
	    return template(ROOT+'/index.html', historylabel）	

错误日志为：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-8/77862812.jpg)  

## 7. 
修改：  

    cursor.execute('create table if not exists record (time text, record varchar)')
变成：  

    cursor.execute('create table if not exists record (time text, record text)')

printhistory函数中增加：  

        cursor.execute('create table if not exists record (time text, record text)')
home函数改为：  

    @app.route('/')
	def home():
	    notelist1 = printhistory()
	    return template(ROOT+'/index.html', historylabel=notelist1)  
save函数：  
由：  

    notelist1 = printhistory() 
    historylabel = str(notelist1)
    return template(ROOT+'/index.html', historylabel) 

变为：  
    
    notelist1 = printhistory()
    return template(ROOT+'/index.html', historylabel=notelist1)

删去`server_static`相关。  

错误日志：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-9/49727787.jpg)  

教练提示说：  
> 试试直接电脑运行，因为代码本身并不依赖于qpy。如果直接跑没问题，可能是qpy有bug。  

在win8系统下运行，果然成功。  
代码挪到手机上，也可以运行。  

所以是电脑端的QPython有bug？！