# _*_ coding:utf-8 _*_
#qpy:webapp:babyrecord
#qpy:fullscreen
#qpy://localhost:8800

"""
Babyrecordapp
@Author Picklecai
"""

import os
from os.path import exists
from bottle import Bottle, ServerAdapter, request, template
import sqlite3
import time
import datetime
from email.header import Header

ROOT = os.path.dirname(os.path.abspath(__file__))
# 定义html文件变量
global indexhtml, historyhtml, babyhtml, baby2html, emailhtml, camerahtml
indexhtml = '''
<html>
    <head>
        <META http-equiv=Content-Type content=text/html; charset=utf-8>
        <title>babyrecord</title>
        <meta name="description" content="">
        <meta name="keywords" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
        <meta name="renderer" content="webkit">
        <meta http-equiv="Cache-Control" content="no-siteapp" />
        <style>
             .get-title {
              font-size: 200%;
              border: 2px solid #fff;
              padding: 5px;
              display: inline-block;
            }
             .get {
              background: #85c80f;
              color: #fff;
              text-align: center;
              padding: 15px 0;
            }

            .labeltitle{
              background:#c6d7d2;
              color:#000000;
              font-size: 150%;
              text-align: left;
              padding: 5px 0 5px 0;
              font-weight:bold;
            }

            .labelrecord{
              background-color: #c6d7d2;
              text-align: left;
              padding: 2px 0 2px 0;
              font-size: 16px;  
            }

            .nav{             
                background:#85c80f;
                text-align: center;
                list-style-type:none;
                margin:0;
                padding:0;
            }

            .nav_li{
                margin:auto; 
                padding:inherit; 
                line-height:45px;
            }

            .nav_li li{ 
                width:10%;
                display: inline-block;
            }

            .nav_li a{ 
                font-size:14px;
                font-weight:bold;
                display:block; /* 将链接设为块级元素 */
                padding:1px 1px; /* 设置内边距 */
                background:#85c80f; /* 设置背景色 */
                color:#fff; /* 设置文字颜色 */
                text-decoration:none; /* 去掉下划线 */
                border-right:1px solid #fff; /* 在左侧加上分隔线 */
            }

            .nav_li ul li:hover{ 
                background:rgb(83,83,83);
            }

            .nav_li ul li ul li{
                background:rgb(164,0,0);
                color: #FFF; 
                width: 50px;
                padding: 0px;
                height: 20px; 
                line-height: 20px;
            }

        </style>
    </head>

    <body topmargin=2 leftmargin=2 bgcolor=#ffffff>

    <div class="get">
      <div >
        <div >
          <h1 class="get-title">我在长大</h1>
        </div>
      </div>
    </div>

    <div class="nav" align="center"  >
        <div class="nav_li" align="center" >
          <ul>
            <li><a href="/">开始记录</a></li>
            <li><a href="historyhtml">查看历史</a></li>
            <li><a href="babyhtml">宝宝信息</a></li>
            <li><a href="emailhtml">发送邮箱</a></li>
            <li><a href="camerahtml">宝宝拍照</a></li>
            </li>
          </ul>
        </div>
      </div>
    <div >友情提醒：如果第一次使用，请先点击菜单“宝宝信息”上传您宝宝的基本信息，否则系统会出错。</div>
    </br>

    <form action="/indexhtml" method="POST">
        <div class="labeltitle">
        请记录宝宝今天的表现吧:
        </div>
        </br>    
        <div align="center" style="width:100%;padding:30px;padding-bottom:80px;">
            <input name="newline" type="text" style="width:40%;float:left;"/>
        </div>
        <div align="center">
            <input value="save" type="submit" />
        </div>
    </form>     

    </body>
</html>
'''
historyhtml = '''
<html>
    <head>
        <META http-equiv=Content-Type content=text/html; charset=utf-8>
        <title>babyrecord</title>
        <meta name="description" content="">
        <meta name="keywords" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
        <meta name="renderer" content="webkit">
        <meta http-equiv="Cache-Control" content="no-siteapp" />
        <style>
             .get-title {
              font-size: 200%;
              border: 2px solid #fff;
              padding: 5px;
              display: inline-block;
            }
             .get {
              background: #85c80f;
              color: #fff;
              text-align: center;
              padding: 15px 0;
            }

            .labeltitle{
              background:#c6d7d2;
              color:#000000;
              font-size: 150%;
              text-align: left;
              padding: 5px 0 5px 0;
              font-weight:bold;
            }

            .labelrecord{
              background-color: #c6d7d2;
              text-align: left;
              padding: 2px 0 2px 0;
              font-size: 16px;  
            }

            .nav{             
                background:#85c80f;
                text-align: center;
                list-style-type:none;
                margin:0;
                padding:0;
            }

            .nav_li{
                margin:auto; 
                padding:inherit; 
                line-height:45px;
            }

            .nav_li li{ 
                width:10%;
                display: inline-block;
            }

            .nav_li a{ 
                font-size:14px;
                font-weight:bold;
                display:block; /* 将链接设为块级元素 */
                padding:1px 1px; /* 设置内边距 */
                background:#85c80f; /* 设置背景色 */
                color:#fff; /* 设置文字颜色 */
                text-decoration:none; /* 去掉下划线 */
                border-right:1px solid #fff; /* 在左侧加上分隔线 */
            }

            .nav_li ul li:hover{ 
                background:rgb(83,83,83);
            }

            .nav_li ul li ul li{
                background:rgb(164,0,0);
                color: #FFF; 
                width: 50px;
                padding: 0px;
                height: 20px; 
                line-height: 20px;
            }

        </style>
    </head>

    <body topmargin=2 leftmargin=2 bgcolor=#ffffff>

    <div class="get">
      <div >
        <div >
          <h1 class="get-title">我在长大</h1>
        </div>
      </div>
    </div>

    <div class="nav" align="center"  >
        <div class="nav_li" align="center" >
          <ul>
            <li><a href="/">开始记录</a></li>
            <li><a href="historyhtml">查看历史</a></li>
            <li><a href="babyhtml">宝宝信息</a></li>
            <li><a href="emailhtml">发送邮箱</a></li>
            <li><a href="camerahtml">宝宝拍照</a></li>
            </li>
          </ul>
        </div>
      </div>
    <div >友情提醒：如果第一次使用，请先点击菜单“宝宝信息”上传您宝宝的基本信息，否则系统会出错。</div>
    </br>

	<div class="labeltitle">历史记录：</div>
	%for i in historylabel:
		<div class="labelrecord"> 现在时间是：{{i[0]}}</div>
		<div class="labelrecord"> 宝宝今天{{i[1]}}天</div>
		<div class="labelrecord"> 宝宝今天的表现是：{{i[2]}}</div> 
    %end		
   	</div>
    </body>
</html>
'''
babyhtml = '''
<html>
    <head>
        <META http-equiv=Content-Type content=text/html; charset=utf-8>
        <title>babyrecord</title>
        <meta name="description" content="">
        <meta name="keywords" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
        <meta name="renderer" content="webkit">
        <meta http-equiv="Cache-Control" content="no-siteapp" />
        <style>
             .get-title {
              font-size: 200%;
              border: 2px solid #fff;
              padding: 5px;
              display: inline-block;
            }
             .get {
              background: #85c80f;
              color: #fff;
              text-align: center;
              padding: 15px 0;
            }

            .labeltitle{
              background:#c6d7d2;
              color:#000000;
              font-size: 150%;
              text-align: left;
              padding: 5px 0 5px 0;
              font-weight:bold;
            }

            .labelrecord{
              background-color: #c6d7d2;
              text-align: left;
              padding: 2px 0 2px 0;
              font-size: 16px;  
            }

            .nav{             
                background:#85c80f;
                text-align: center;
                list-style-type:none;
                margin:0;
                padding:0;
            }

            .nav_li{
                margin:auto; 
                padding:inherit; 
                line-height:45px;
            }

            .nav_li li{ 
                width:10%;
                display: inline-block;
            }

            .nav_li a{ 
                font-size:14px;
                font-weight:bold;
                display:block; /* 将链接设为块级元素 */
                padding:1px 1px; /* 设置内边距 */
                background:#85c80f; /* 设置背景色 */
                color:#fff; /* 设置文字颜色 */
                text-decoration:none; /* 去掉下划线 */
                border-right:1px solid #fff; /* 在左侧加上分隔线 */
            }

            .nav_li ul li:hover{ 
                background:rgb(83,83,83);
            }

            .nav_li ul li ul li{
                background:rgb(164,0,0);
                color: #FFF; 
                width: 50px;
                padding: 0px;
                height: 20px; 
                line-height: 20px;
            }

        </style>
    </head>

    <body topmargin=2 leftmargin=2 bgcolor=#ffffff>

    <div class="get">
      <div >
        <div >
          <h1 class="get-title">我在长大</h1>
        </div>
      </div>
    </div>

    <div class="nav" align="center"  >
        <div class="nav_li" align="center" >
          <ul>
            <li><a href="/">开始记录</a></li>
            <li><a href="historyhtml">查看历史</a></li>
            <li><a href="babyhtml">宝宝信息</a></li>
            <li><a href="emailhtml">发送邮箱</a></li>
            <li><a href="camerahtml">宝宝拍照</a></li>
            </li>
          </ul>
        </div>
      </div>
    <div >友情提醒：如果第一次使用，请先点击菜单“宝宝信息”上传您宝宝的基本信息，否则系统会出错。</div>
    </br>
      
      <input type="button" onclick="showAndHidden1();" align="left" value="更新宝宝信息："/> 
      <form action="/baby2html" method="post">
        <div id="div1" align="left" style="width:100%;padding:30px;padding-bottom:80px;display:none;">
        <span class="labelrecord">宝宝姓名：</span>
            <input name="name" type="text" /><br /><br />
        <span class="labelrecord">宝宝性别：</span>
            <input name="gender" type="text" /><br /><br />
        <span class="labelrecord">宝宝出生日期：</span>
            <input type="number" name="year" min="2005" max="2020" step="1" value="2015">年
            <input type="number" name="month" min="1" max="12" step="1" value="1">月
            <input type="number" name="date" min="1" max="31" step="1" value="15">日<br /><br />
        <span class="labelrecord">妈妈邮箱：</span>
            <input name="email" type="text" />  <br /><br />            
        <input type="submit" align="left" value="保存" name="savebaby" />
        </div>
      </form>   

    <div id="div2" style="width:100%;padding:30px;padding-bottom:80px;display:block">
    <p class="labeltitle">宝宝信息：</p>
        <span class="labelrecord">宝宝姓名：</span>
        {{name}}        
        </br></br>
        <span class="labelrecord">宝宝性别：</span>
        {{gender}}
        </br></br>
        <span class="labelrecord">宝宝出生日期：</span>
        {{birthtime}}
        </br></br>
        <span class="labelrecord">妈妈邮箱：</span>
        {{momemail}}
        <br /><br />
    </div>
        <br />  

        <script type="text/javascript"> 
            function showAndHidden1(){ 
                var div1=document.getElementById("div1"); 
                if(div1.style.display=='none') div1.style.display='block';
                if(div2.style.display=='block') div2.style.display='none';  
                } 
        </script> 

    </body>
</html>
'''
baby2html = '''
<html>
    <head>
        <META http-equiv=Content-Type content=text/html; charset=utf-8>
        <title>babyrecord</title>
        <meta name="description" content="">
        <meta name="keywords" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
        <meta name="renderer" content="webkit">
        <meta http-equiv="Cache-Control" content="no-siteapp" />
        <style>
             .get-title {
              font-size: 200%;
              border: 2px solid #fff;
              padding: 5px;
              display: inline-block;
            }
             .get {
              background: #85c80f;
              color: #fff;
              text-align: center;
              padding: 15px 0;
            }

            .labeltitle{
              background:#c6d7d2;
              color:#000000;
              font-size: 150%;
              text-align: left;
              padding: 5px 0 5px 0;
              font-weight:bold;
            }

            .labelrecord{
              background-color: #c6d7d2;
              text-align: left;
              padding: 2px 0 2px 0;
              font-size: 16px;  
            }

            .nav{             
                background:#85c80f;
                text-align: center;
                list-style-type:none;
                margin:0;
                padding:0;
            }

            .nav_li{
                margin:auto; 
                padding:inherit; 
                line-height:45px;
            }

            .nav_li li{ 
                width:10%;
                display: inline-block;
            }

            .nav_li a{ 
                font-size:14px;
                font-weight:bold;
                display:block; /* 将链接设为块级元素 */
                padding:1px 1px; /* 设置内边距 */
                background:#85c80f; /* 设置背景色 */
                color:#fff; /* 设置文字颜色 */
                text-decoration:none; /* 去掉下划线 */
                border-right:1px solid #fff; /* 在左侧加上分隔线 */
            }

            .nav_li ul li:hover{ 
                background:rgb(83,83,83);
            }

            .nav_li ul li ul li{
                background:rgb(164,0,0);
                color: #FFF; 
                width: 50px;
                padding: 0px;
                height: 20px; 
                line-height: 20px;
            }

        </style>
    </head>

    <body topmargin=2 leftmargin=2 bgcolor=#ffffff>

    <div class="get">
      <div >
        <div >
          <h1 class="get-title">我在长大</h1>
        </div>
      </div>
    </div>

    <div class="nav" align="center"  >
        <div class="nav_li" align="center" >
          <ul>
            <li><a href="/">开始记录</a></li>
            <li><a href="historyhtml">查看历史</a></li>
            <li><a href="babyhtml">宝宝信息</a></li>
            <li><a href="emailhtml">发送邮箱</a></li>
            <li><a href="camerahtml">宝宝拍照</a></li>
            </li>
          </ul>
        </div>
      </div>

    <div class="labeltitle">宝宝信息：</div>

    <div style="width:100%;padding:30px;padding-bottom:80px;">
        <span class="labelrecord">宝宝姓名：</span>
        {{name}}        
        </br></br>
        <span class="labelrecord">宝宝性别：</span>
        {{gender}}
        </br></br>
        <span class="labelrecord">宝宝出生日期：</span>
        {{birthtime}}
        </br></br>
        <span class="labelrecord">妈妈邮箱：</span>
        {{momemail}}
        <br /><br />
    </div>
        <br />   
    </body>
</html>
'''
emailhtml = '''
<html>
    <head>
        <META http-equiv=Content-Type content=text/html; charset=utf-8>
        <title>babyrecord</title>
        <meta name="description" content="">
        <meta name="keywords" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
        <meta name="renderer" content="webkit">
        <meta http-equiv="Cache-Control" content="no-siteapp" />
        <style>
             .get-title {
              font-size: 200%;
              border: 2px solid #fff;
              padding: 5px;
              display: inline-block;
            }
             .get {
              background: #85c80f;
              color: #fff;
              text-align: center;
              padding: 15px 0;
            }

            .labeltitle{
              background:#c6d7d2;
              color:#000000;
              font-size: 150%;
              text-align: left;
              padding: 5px 0 5px 0;
              font-weight:bold;
            }

            .labelrecord{
              background-color: #c6d7d2;
              text-align: left;
              padding: 2px 0 2px 0;
              font-size: 16px;  
            }

            .nav{             
                background:#85c80f;
                text-align: center;
                list-style-type:none;
                margin:0;
                padding:0;
            }

            .nav_li{
                margin:auto; 
                padding:inherit; 
                line-height:45px;
            }

            .nav_li li{ 
                width:10%;
                display: inline-block;
            }

            .nav_li a{ 
                font-size:14px;
                font-weight:bold;
                display:block; /* 将链接设为块级元素 */
                padding:1px 1px; /* 设置内边距 */
                background:#85c80f; /* 设置背景色 */
                color:#fff; /* 设置文字颜色 */
                text-decoration:none; /* 去掉下划线 */
                border-right:1px solid #fff; /* 在左侧加上分隔线 */
            }

            .nav_li ul li:hover{ 
                background:rgb(83,83,83);
            }

            .nav_li ul li ul li{
                background:rgb(164,0,0);
                color: #FFF; 
                width: 50px;
                padding: 0px;
                height: 20px; 
                line-height: 20px;
            }

        </style>
    </head>

    <body topmargin=2 leftmargin=2 bgcolor=#ffffff>

    <div class="get">
      <div >
        <div >
          <h1 class="get-title">我在长大</h1>
        </div>
      </div>
    </div>

    <div class="nav" align="center"  >
        <div class="nav_li" align="center" >
          <ul>
            <li><a href="/">开始记录</a></li>
            <li><a href="historyhtml">查看历史</a></li>
            <li><a href="babyhtml">宝宝信息</a></li>
            <li><a href="emailhtml">发送邮箱</a></li>
            <li><a href="camerahtml">宝宝拍照</a></li>
            </li>
          </ul>
        </div>
      </div>
    <div >友情提醒：如果第一次使用，请先点击菜单“宝宝信息”上传您宝宝的基本信息，否则系统会出错。</div>
    </br>
    
    <div class="labeltitle">系统提示：</div>
    </br>
    <div class="labelrecord">您宝宝的记录已经发送成功发送到邮箱{{momemail}}中。</div>
    </div>
    </body>
</html>
'''
camerahtml = '''
<html>
    <head>
        <META http-equiv=Content-Type content=text/html; charset=utf-8>
        <title>babyrecord</title>
        <meta name="description" content="">
        <meta name="keywords" content="">
        <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
        <meta name="renderer" content="webkit">
        <meta http-equiv="Cache-Control" content="no-siteapp" />
        <style>
             .get-title {
              font-size: 200%;
              border: 2px solid #fff;
              padding: 5px;
              display: inline-block;
            }
             .get {
              background: #85c80f;
              color: #fff;
              text-align: center;
              padding: 15px 0;
            }

            .labeltitle{
              background:#c6d7d2;
              color:#000000;
              font-size: 150%;
              text-align: left;
              padding: 5px 0 5px 0;
              font-weight:bold;
            }

            .labelrecord{
              background-color: #c6d7d2;
              text-align: left;
              padding: 2px 0 2px 0;
              font-size: 16px;  
            }

            .nav{             
                background:#85c80f;
                text-align: center;
                list-style-type:none;
                margin:0;
                padding:0;
            }

            .nav_li{
                margin:auto; 
                padding:inherit; 
                line-height:45px;
            }

            .nav_li li{ 
                width:10%;
                display: inline-block;
            }

            .nav_li a{ 
                font-size:14px;
                font-weight:bold;
                display:block; /* 将链接设为块级元素 */
                padding:1px 1px; /* 设置内边距 */
                background:#85c80f; /* 设置背景色 */
                color:#fff; /* 设置文字颜色 */
                text-decoration:none; /* 去掉下划线 */
                border-right:1px solid #fff; /* 在左侧加上分隔线 */
            }

            .nav_li ul li:hover{ 
                background:rgb(83,83,83);
            }

            .nav_li ul li ul li{
                background:rgb(164,0,0);
                color: #FFF; 
                width: 50px;
                padding: 0px;
                height: 20px; 
                line-height: 20px;
            }

        </style>
    </head>

    <body topmargin=2 leftmargin=2 bgcolor=#ffffff>

    <div class="get">
      <div >
        <div >
          <h1 class="get-title">我在长大</h1>
        </div>
      </div>
    </div>

    <div class="nav" align="center"  >
        <div class="nav_li" align="center" >
          <ul>
            <li><a href="/">开始记录</a></li>
            <li><a href="historyhtml">查看历史</a></li>
            <li><a href="babyhtml">宝宝信息</a></li>
            <li><a href="emailhtml">发送邮箱</a></li>
            <li><a href="camerahtml">宝宝拍照</a></li>
            </li>
          </ul>
        </div>
      </div>
    <div >友情提醒：如果第一次使用，请先点击菜单“宝宝信息”上传您宝宝的基本信息，否则系统会出错。</div>
    </br>
    
    <div class="labeltitle">照片目录：</div>
    </br>
    <div class="labelrecord">
         /photo文件夹中已经存了{{photoid}}张照片。</br>
    %for i in photoname:
        <div class="labelrecord"> 拍照时间：{{i[0]}} 照片名：{{i[1]}}</div>
    %end
    </div>
    </div>
    </body>
</html>
'''

class MyWSGIRefServer(ServerAdapter):
    server = None

    def run(self, handler):
        from wsgiref.simple_server import make_server, WSGIRequestHandler
        if self.quiet:
            class QuietHandler(WSGIRequestHandler):
                def log_request(*args, **kw): pass
            self.options['handler_class'] = QuietHandler
        self.server = make_server(self.host, self.port, handler, **self.options)
        self.server.serve_forever()

    def stop(self):
        # sys.stderr.close()
        import threading
        threading.Thread(target=self.server.shutdown).start()
        # self.server.shutdown()
        self.server.server_close()
        print "# QWEBAPPEND"

def __exit():
    global server
    server.stop()

def __ping():
    return "OK"

def home():
    filename = ROOT+'/babyinfo.db'
    if exists(filename):
        return indexhtml
    else:
        name = "未设置"
        gender = "未设置"
        birthtime = "未设置"
        momemail = "未设置"
        return template(babyhtml, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml, name=name, gender=gender, birthtime=birthtime, momemail=momemail)

def inputnewline(data):
    newline = request.forms.get('newline')
    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
    babyage = calbabyage()
    data = nowtime.decode('utf-8'), babyage, newline.decode('utf-8')
    conn = sqlite3.connect(ROOT+'/noterecord.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists record (time text, age text, record text)')
    cursor.execute('insert into record (time, age, record) values (?,?,?)', data)
    cursor.close()
    conn.commit()
    conn.close()

def save():
    newline = request.forms.get('newline')
    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
    babyage = calbabyage()
    data = nowtime.decode('utf-8'), babyage, newline.decode('utf-8')
    inputnewline(data)
    return indexhtml

def history():
    conn = sqlite3.connect(ROOT+'/noterecord.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists record (time text, age text, record text)')
    cursor.execute('select * from record')
    notelist = cursor.fetchall()
    return template(historyhtml, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml, camerahtml=camerahtml,  historylabel=notelist)

def createbaby(data):
    conn = sqlite3.connect(ROOT+'/babyinfo.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists babyinfo (name text, gender text, birthtime text, momemail text, settingtime text)')
    cursor.execute('insert into babyinfo (name, gender, birthtime, momemail, settingtime) values (?,?,?,?,?)', data)
    cursor.close()
    conn.commit()
    conn.close()

def readbaby():
    conn = sqlite3.connect(ROOT+'/babyinfo.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists babyinfo (name text, gender text, birthtime text, momemail text, settingtime text)')
    cursor.execute('select * from babyinfo')
    babyinfolist = cursor.fetchall()
    return babyinfolist

def calbabyage():
    today = datetime.date.today()
    filename = ROOT+'/babyinfo.db'
    if exists(filename):
        conn = sqlite3.connect(ROOT+'/babyinfo.db')
        cursor = conn.cursor()
        cursor.execute('select birthtime from babyinfo order by settingtime desc limit 0,1')
        bn = str(cursor.fetchall())
        babybirth = datetime.date(int(bn[4:8]), int(bn[9:11]), int(bn[12:14]))
    babyage = str((today - babybirth).days)
    return babyage

def baby():
    filename = ROOT+'/babyinfo.db'
    if exists(filename):
        conn = sqlite3.connect(ROOT+'/babyinfo.db')
        cursor = conn.cursor()
        cursor.execute('select name from babyinfo order by settingtime desc limit 0,1')
        n = str(cursor.fetchall())
        name = n[4:-4].decode('unicode_escape')
        cursor.execute('select gender from babyinfo order by settingtime desc limit 0,1')
        g = str(cursor.fetchall())
        gender = g[4:-4].decode('unicode_escape')
        cursor.execute('select birthtime from babyinfo order by settingtime desc limit 0,1')
        bn = str(cursor.fetchall())
        birthtime = datetime.date(int(bn[4:8]), int(bn[9:11]), int(bn[12:14]))
        cursor.execute('select momemail from babyinfo order by settingtime desc limit 0,1')
        em = str(cursor.fetchall())
        momemail = em[4:-4].decode('utf-8')
    else:
        name = "未设置"
        gender = "未设置"
        birthtime = "未设置"
        momemail = "未设置"
    return template(babyhtml, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml, camerahtml=camerahtml, name=name, gender=gender, birthtime=birthtime, momemail=momemail)

def savebaby():
    name = request.forms.get('name')
    gender = request.forms.get('gender')
    birthtime = datetime.date(int(request.forms.get('year')), int(request.forms.get('month')), int(request.forms.get('date')))
    momemail = request.forms.get('email')
    settingtime = time.strftime("%d/%m/%Y %H:%M:%S")
    if name==None or gender==None or birthtime==None or validateEmail(momemail)== 0:
        name = "重新设置"
        gender = "重新设置"
        birthtime = "重新设置"
        momemail = "重新设置"
        return template(babyhtml, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml, camerahtml=camerahtml, name=name, gender=gender, birthtime=birthtime, momemail=momemail)
    else:
        data = name.decode('utf-8'), gender.decode('utf-8'), birthtime, momemail, settingtime
        createbaby(data)
        readbaby()
        return template(baby2html, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml, camerahtml=camerahtml,  name=name, gender=gender, birthtime=birthtime, momemail=momemail)

def _format_addr(s):
    from email.utils import parseaddr, formataddr
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def validateEmail(email):
    import re
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0

def sendmail():
    # 导入email模块
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import smtplib
    # 设置邮件变量
    from_addr = "pickle.ahcai@163.com"
    password = "ahcai318"
    smtp_server = "smtp.163.com"
    filename = ROOT+'/babyinfo.db'
    if exists(filename):
        conn = sqlite3.connect(ROOT+'/babyinfo.db')
        cursor = conn.cursor()
        cursor.execute('select momemail from babyinfo order by settingtime desc limit 0,1')
        em = str(cursor.fetchall())
        momemail = em[4:-4].decode('utf-8')
    else:
        momemail = "caimeijuan@gmail.com"
    to_addr = momemail
    historyrecord = ROOT+'/noterecord.db'
    # 发邮件
    if exists(historyrecord):
        msg = MIMEMultipart()
        msg['From'] = _format_addr(u'我在长大 <%s>' % from_addr)
        msg['To'] = _format_addr(u'亲爱的妈妈 <%s>' % to_addr)
        msg['Subject'] = Header(u'您的宝宝记录……', 'utf-8').encode()
        msg.attach(MIMEText('附件是您宝宝的日常记录，请查收。祝您生活愉快！宝宝健康快乐！', 'plain', 'utf-8'))
        with open(historyrecord, 'rb') as f:
            mime = MIMEBase('database', 'xls', filename='noterecord.xls')
            mime.add_header('Content-Disposition', 'attachment', filename='noterecord.db')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
    else:
        msg = MIMEText('您尚未开始记录宝宝的日常记录，记录后可收到带宝宝记录附件的邮件！', 'plain', 'utf-8')
        msg['From'] = _format_addr(u'我在长大 <%s>' % from_addr)
        msg['To'] = _format_addr(u'亲爱的妈妈 <%s>' % to_addr)
        msg['Subject'] = Header(u'您的宝宝记录……', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    return template(emailhtml, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml, camerahtml=camerahtml, momemail=momemail)

def savephotoname(data):
    # 保存照片名列表
    conn = sqlite3.connect(ROOT+'/photoname.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists photoname (time text, name text)')
    cursor.execute('insert into photoname (time, name) values (?,?)', data)
    cursor.close()
    conn.commit()
    conn.close()

def readphotoname():
    conn = sqlite3.connect(ROOT+'/photoname.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists photoname (time text, name text)')
    cursor.execute('select * from photoname')
    namelist = cursor.fetchall()
    return namelist

def camerababy():
    import androidhelper
    droid = androidhelper.Android()
    if not exists(ROOT+'/photo'):
        photoid = 1
        os.makedirs(ROOT+'/photo')
    else:
        photoid = sum([len(files) for root,dirs,files in os.walk(ROOT+'/photo')]) + 1
    # 设置照片名
    photoname = str('babyrecordphoto%d.jpg' % photoid)
    # 拍照
    droid.cameraInteractiveCapturePicture(ROOT+'/photo/%s' % photoname)
    # 保存照片名
    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
    data = nowtime, photoname
    savephotoname(data)
    # 读取照片名
    namelist = readphotoname()
    return template(camerahtml, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml, camerahtml=camerahtml, photoid=photoid, photoname=namelist)

app = Bottle()
app.route('/', method='GET')(home)
app.route('/indexhtml', method='POST')(save)
app.route('/historyhtml', method='GET')(history)
app.route('/babyhtml', method='GET')(baby)
app.route('/baby2html', method='POST')(savebaby)
app.route('/emailhtml', method='GET')(sendmail)
app.route('/camerahtml', method='GET')(camerababy)
app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)

try:
    server = MyWSGIRefServer(host="localhost", port="8800")
    app.run(server=server, reloader=False)
except Exception, ex:
    print "Exception: %s" % repr(ex)