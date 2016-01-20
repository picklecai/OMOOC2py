# 笔记部署公网的开发笔记  

## sae内容见sae教程  

## 主程序index.wsgi  

### 1. 页面显示  

    from bottle import Bottle, run	
	import sae
	
	app = Bottle()
	
	@app.route('/')
	def hello():
	    return "Hello, world! - Bottle"
	
	application = sae.create_wsgi_app(app)  

这是最简页面，显示内容即："Hello, world! - Bottle"  

    @app.route("/ping")
	def application(environ, start_response):
	    start_response('200 ok', [('content-type', 'text/plain')])
	    return  "The connection is ok !"
	application = sae.create_wsgi_app(application) # 这里如果写app就500出错

这个页面显示"The connection is ok !"  
无论我在route后面填入什么地址，它总是默认打开页面。即：我打开/和打开/ping，效果等同，都是显示它的内容。即使我另外加上一个指向/的route。  

    @app.route('/')
	def home():
	    return  '''
	    <form action="/" method="POST">
	    <a href="/history.html">hitory</a>
	    <br/>    
	    Please input a new line: 
	    <br/>
	    <input name="newline" type="text"/>
	    <br/>
	    <input value="save" type="submit" />
	    </form>'''
	application = sae.create_wsgi_app(app)

把第二段代码注释掉了，第三段代码才起作用。  

### 2. txt文件存储改为kvdb存储  

这里主要是看的[公网版日记系统 | 小赖的Python学习笔记](https://wp-lai.gitbooks.io/learn-python/content/1sTry/sae.html)笔记来改写的：  

    import sae.kvdb
	kv = sae.kvdb.Client()
	count = 0
	
	# 将数据存进数据库
	def save(newline):
	    global count
	    count += 1
	    #在保存当前输入的同时，也保存当前时间。
	    time = time.strftime("%d/%m/%Y %H:%M:%S"+"\n")
	    # 设置id是为了方便后面提取，顺序或逆序也在其中
	    id = 'id' + str(count) 
	    record = {'time':time, 'record':newline}
	    kv.set(id, record)
	
	# 读取数据库中的信息
	def printhistory():
	    history = []
	    for item in kv.get_by_prefix('id'):
	        history.append(item[1])
	    return history

增加的序号这一列，应该对后面逆序排列非常有用。我在长大后吗的改版点有一个就是要逆序排列。