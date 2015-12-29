## 1. 知识学习

第一段代码：  
[怎么在Android下用python调用摄像头？_python吧_百度贴吧](http://tieba.baidu.com/p/2682413660)  

    #encoding:utf-8
	import androidhelper,sys

	droid = androidhelper.Android()
	p = "776779.jpg"
	try:
		droid.cameraCapturePicture("776779.jpg",True)
	except:
		print '拍照失败'
	sys.exit(1)
	print '拍照完成'

关于Androidhelper的文档：[androidhelper documentation](http://kylelk.github.io/html-examples/androidhelper.html)  

## 2. 试行

方法`cameraCapturePicture`：  
> self,targetPath,useAutoFocus=True  
> 
> cameraCapturePicture(targetPath,useAutoFocus=True)   

> Take a picture and save it to the specified path.   
> targetPath (String) useAutoFocus (Boolean) (default=true) returns: (Bundle)  
> A map of Booleans autoFocus and takePicture where True indicates success.  

第一个参数是路径，代码写成：  

    import androidhelper
    @app.route('/camera.html', method='GET')
	def camerababy():
		droid = androidhelper.Android()
		droid.cameraCapturePicture(ROOT+'/photo/776779.jpg',True)
		return template(ROOT+'/camera.html')
运行成功，可以在项目根目录下建立一个photo文件夹，并拍照。  
缺点是照片自动拍成，无法调整拍摄角度和控制拍摄内容。  

方法`cameraInteractiveCapturePicture`：  
>self,targetPath  
cameraInteractiveCapturePicture(targetPath) Starts the image capture application to take a picture and saves it to the specified path. targetPath (String)  

代码改成：  

    import androidhelper
    @app.route('/camera.html', method='GET')
	def camerababy():
		droid = androidhelper.Android()
		droid.cameraInteractiveCapturePicture(ROOT+'/photo/776779.jpg')
		return template(ROOT+'/camera.html')  
马上就可以自己控制镜头方向，拍摄自己想要的照片了。位置仍然在photo下。  

下一个问题是：由于照片名称固定，所以每次新拍摄的，都会将原先拍的替代掉。  

大概由于qpython不稳定，写动态的照片文件名，调试了很久，终于运行成功。  
代码：  

    @app.route('/camera.html', method='GET')
	def camerababy():
	    droid = androidhelper.Android()
	    if not exists(ROOT+'/photo'):
	        photoid = 1 
	    else:
	        photoid = sum([len(files) for root,dirs,files in os.walk(ROOT+'/photo')]) + 1
	    # 设置照片名
	    photoname = str('babyrecordphoto%d.jpg' % photoid)
	    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
	    # 拍照
	    droid.cameraInteractiveCapturePicture(ROOT+'/photo/%s' % photoname)
	    return template(ROOT+'/camera.html', photoid=photoid, nowtime=nowtime, photoname=photoname)

顺便解决了数文件的任务。  
文档见：[15.1. os — Miscellaneous operating system interfaces — Python 2.7.11 documentation](https://docs.python.org/2/library/os.html)  

理想状态是像历史记录一样，返回网页时，能列出照片名列表和时间。但不知何故，db文件无法打开。昨天也遇到这个问题，后来又消失了。  

增加db模块后：  

    @app.route('/camera.html', method='GET')
	def camerababy():
	    droid = androidhelper.Android()
	    if not exists(ROOT+'/photo'):
	        photoid = 1 
	    else:
	        photoid = sum([len(files) for root,dirs,files in os.walk(ROOT+'/photo')]) + 1
	    # 设置并保存照片名
	    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")    
	    photoname = str('babyrecordphoto%d.jpg' % photoid)
	    data = nowtime, photoname
	    savephotoname(data)
	    # 读取照片名
	    namelist = readphotoname()  
	    # 拍照
	    droid.cameraInteractiveCapturePicture(ROOT+'/photo/%s' % photoname)
	    return template(ROOT+'/camera.html', photoid=photoid, photoname=namelist)  

有photo文件夹的情况下，运行成功。  

删去已有的photo文件夹和photoname.db文件，再运行，非常慢，返回camera页面，内容正确。到根目录文件夹查看，photoname.db文件已经成功建立，而photo文件夹未建立。因此新拍的照片不存在。  

使用动态照片名之前，是会自动建立photo文件夹的。那就加上建立文件夹的步骤吧。  

        if not exists(ROOT+'/photo'):
	        photoid = 1 
	        os.mkdir(ROOT+'/photo')

结果报错：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-28/80212646.jpg)  

在[Python实现mkdir -p递归创建多级目录 | 书影博客](http://bookshadow.com/weblog/2014/10/02/python-mkdir-p/)中，提到建文件夹两种方式的区别：  

> Python的os模块也存在两个函数，分别为mkdir和makedirs，其中：

> mkdir( path [,mode] )：创建一个目录，可以是相对或者绝对路径，mode的默认模式是0777。如果目录有多级，则创建最后一级。如果最后一级目录的上级目录有不存在的，则会抛出一个OSError。  
> 
> makedirs( path [,mode] )：创建递归的目录树，可以是相对或者绝对路径，mode的默认模式是0777。如果子目录创建失败或者已经存在，会抛出一个OSError的异常，Windows上Error 183即为目录已经存在的异常错误。如果path只有一级，与mkdir相同。  

两种函数，无论哪种，都是error16错误。  

去掉root，就可以运行了：  

        if not exists(ROOT+'/photo'):
	        photoid = 1 
	        os.mkdir('/photo')  

误，还是要改成makedirs：  

    if not exists(ROOT+'/photo'):
	        photoid = 1 
	        os.makedirs(ROOT+'/photo') 