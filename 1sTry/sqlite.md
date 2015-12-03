# sqlite 私人教程

## 背景

win8

## 安装

### 下载  

下载页面：[SQLite Download Page](http://www.sqlite.org/download.html)  

下载文件：  
[(64位dll文件)](http://www.sqlite.org/2015/sqlite-dll-win64-x64-3090200.zip)  
[(32位shell文件)](http://www.sqlite.org/2015/sqlite-shell-win32-x86-3090200.zip)  
因为没发现64位shell文件，就下载了32位。解压缩后发现就是命令行窗口，那可能64位和32位没有什么区别吧。  

### 安装

- 访问上述 SQLite 下载页面，从 Windows 区下载 sqlite-shell-win32-*.zip 和 sqlite-dll-win32-*.zip 压缩文件。  
- 创建文件夹 C:\sqlite，并在此文件夹下解压上面两个压缩文件，将得到 sqlite3.def、sqlite3.dll 和 sqlite3.exe 文件。  
- 添加 C:\sqlite 到 PATH 环境变量，最后在命令提示符下，使用 sqlite3 命令

## 配置

## 使用

打开shell，试用.help命令如下：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-3/14603097.jpg)

## 体验

装完发现在[使用SQLite - 廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001388320596292f925f46d56ef4c80a1c9d8e47e2d5711000)中写道：  
> Python就内置了SQLite3，所以，在Python中使用SQLite，不需要安装任何东西，直接使用。  

调用：  

> Python定义了一套操作数据库的API接口，任何数据库要连接到Python，只需要提供符合Python标准的数据库驱动即可。  
> 由于SQLite的驱动内置在Python标准库中，所以我们可以直接来操作SQLite数据库。  
> 我们在Python交互式命令行实践一下：  

     导入SQLite驱动:
	>>> import sqlite3
	# 连接到SQLite数据库
	# 数据库文件是test.db
	# 如果文件不存在，会自动在当前目录创建:
	>>> conn = sqlite3.connect('test.db')
	# 创建一个Cursor:
	>>> cursor = conn.cursor()
	# 执行一条SQL语句，创建user表:
	>>> cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
	<sqlite3.Cursor object at 0x10f8aa260>
	# 继续执行一条SQL语句，插入一条记录:
	>>> cursor.execute('insert into user (id, name) values (\'1\', \'Michael\')')
	<sqlite3.Cursor object at 0x10f8aa260>
	# 通过rowcount获得插入的行数:
	>>> cursor.rowcount
	1
	# 关闭Cursor:
	>>> cursor.close()
	# 提交事务:
	>>> conn.commit()
	# 关闭Connection:
	>>> conn.close()

查询：  

    >>> conn = sqlite3.connect('test.db')
	>>> cursor = conn.cursor()
	# 执行查询语句:
	>>> cursor.execute('select * from user where id=?', '1')
	<sqlite3.Cursor object at 0x10f8aa340>
	# 获得查询结果集:
	>>> values = cursor.fetchall()
	>>> values
	[(u'1', u'Michael')]
	>>> cursor.close()
	>>> conn.close()