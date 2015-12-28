# _*_ coding:utf-8 _*_
#qpy:webapp:babyrecord
#qpy:fullscreen
#qpy://localhost:8800

"""
Babyrecordapp
@Author Picklecai
"""

from bottle import *
import os
import sqlite3
import time
import types
import re
import datetime
from os.path import exists
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

ROOT = os.path.dirname(os.path.abspath(__file__))
global indexhtml
indexhtml = '''
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

		    .get-title {
		      font-size: 200%;
		      border: 2px solid #fff;
		      padding: 5px;
		      display: inline-block;
		    }

		    .get-btn {
		      background: #fff;
		    }

		    .detail {
		      background: #fff;
		    }

		    .detail-h2 {
		      text-align: center;
		      font-size: 150%;
		      margin: 40px 0;
		    }

		    .detail-h3 {
		      color: #1f8dd6;
		    }

		    .detail-p {
		      color: #7f8c8d;
		    }

		    .detail-mb {
		      margin-bottom: 30px;
		    }

		    .hope {
		      background: #fff37;
		      padding: 50px 0;
		    }

		    .hope-img {
		      text-align: center;
		    }

		    .hope-hr {
		      border-color: #149C88;
		    }

		    .hope-title {
		      font-size: 140%;
		    }

		    .about {
		      background: #fff;
		      padding: 40px 0;
		      color: #7f8c8d;
		    }

		    .about-color {
		      color: #34495e;
		    }

		    .about-title {
		      font-size: 180%;
		      padding: 30px 0 50px 0;
		      text-align: center;
		    }

		    .footer p {
		      color: #7f8c8d;
		      margin: 0;
		      padding: 15px 0;
		      text-align: center;
		      background: #2d3e50;
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

			.no1{			  
				margin:50px;
				border:0;			  
				padding:0;
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
				width:20%;
				display: inline-block;
			}

			.nav_li a{ 
				font-size:16px;
				font-weight:bold;
				display:block; /* 将链接设为块级元素 */
				padding:5px 8px; /* 设置内边距 */
				background:#85c80f; /* 设置背景色 */
				color:#fff; /* 设置文字颜色 */
				text-decoration:none; /* 去掉下划线 */
				border-right:1px solid #fff; /* 在左侧加上分隔线 */
			}

			.active{ 
				background:rgb(212,2,3)
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
	  <div class="am-header-left am-header-nav">
	    <a href="#left-link" class="">
	      <i class="am-header-icon am-icon-home"></i>
	    </a>
	  </div>
	  <h1 class="am-header-title">
	    <a align="center" class=".hope">欢迎使用！</a>
	  </h1>
	  <div class="am-header-right am-header-nav">
	    <a href="#right-link" class="">
	      <i class="am-header-icon am-icon-bars"></i>
	    </a>
	  </div>
	</header>

	<div class="get">
	  <div class="am-g">
	    <div class="am-u-lg-12">
	      <h1 class="get-title">我在长大</h1>
	    </div>
	  </div>
	</div>

	<div class="nav" align="center"  >
	    <div class="nav_li" align="center" >
	      <ul>
	        <li ><a href=/>开始记录</a></li>
	        <li><a href=historyhtml>查看历史</a></li>
	        <li><a href=babyhtml>宝宝信息</a></li>
	        <li><a href=emailhtml>发送邮箱</a></li>
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
'''

global historyhtml
historyhtml = '''
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

		    .get-title {
		      font-size: 200%;
		      border: 2px solid #fff;
		      padding: 5px;
		      display: inline-block;
		    }

		    .get-btn {
		      background: #fff;
		    }

		    .detail {
		      background: #fff;
		    }

		    .detail-h2 {
		      text-align: center;
		      font-size: 150%;
		      margin: 40px 0;
		    }

		    .detail-h3 {
		      color: #1f8dd6;
		    }

		    .detail-p {
		      color: #7f8c8d;
		    }

		    .detail-mb {
		      margin-bottom: 30px;
		    }

		    .hope {
		      background: #fff37;
		      padding: 50px 0;
		    }

		    .hope-img {
		      text-align: center;
		    }

		    .hope-hr {
		      border-color: #149C88;
		    }

		    .hope-title {
		      font-size: 140%;
		    }

		    .about {
		      background: #fff;
		      padding: 40px 0;
		      color: #7f8c8d;
		    }

		    .about-color {
		      color: #34495e;
		    }

		    .about-title {
		      font-size: 180%;
		      padding: 30px 0 50px 0;
		      text-align: center;
		    }

		    .footer p {
		      color: #7f8c8d;
		      margin: 0;
		      padding: 15px 0;
		      text-align: center;
		      background: #2d3e50;
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

			.no1{			  
				margin:50px;
				border:0;			  
				padding:0;
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
				width:20%;
				display: inline-block;
			}

			.nav_li a{ 
				font-size:16px;
				font-weight:bold;
				display:block; /* 将链接设为块级元素 */
				padding:5px 8px; /* 设置内边距 */
				background:#85c80f; /* 设置背景色 */
				color:#fff; /* 设置文字颜色 */
				text-decoration:none; /* 去掉下划线 */
				border-right:1px solid #fff; /* 在左侧加上分隔线 */
			}

			.active{ 
				background:rgb(212,2,3)
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
	  <div class="am-header-left am-header-nav">
	    <a href="#left-link" class="">
	      <i class="am-header-icon am-icon-home"></i>
	    </a>
	  </div>
	  <h1 class="am-header-title">
	    <a align="center" class=".hope">欢迎使用！</a>
	  </h1>
	  <div class="am-header-right am-header-nav">
	    <a href="#right-link" class="">
	      <i class="am-header-icon am-icon-bars"></i>
	    </a>
	  </div>
	</header>

	<div class="get">
	  <div class="am-g">
	    <div class="am-u-lg-12">
	      <h1 class="get-title">我在长大</h1>
	    </div>
	  </div>
	</div>

	<div class="nav" align="center" >
	    <div class="nav_li" align="center" >
	      <ul>
	        <li ><a href=/>开始记录</a></li>
	        <li><a href=historyhtml>查看历史</a></li>
	        <li><a href=babyhtml>宝宝信息</a></li>
	        <li><a href=emailhtml>发送邮箱</a></li>
	        </li>
	      </ul>
	    </div>
	  </div>

    <div >友情提醒：如果第一次使用，请先点击菜单“宝宝信息”上传您宝宝的基本信息，否则系统会出错。</div>
    </br>

	</br></br>
	<div class="labeltitle">历史记录：</div>
	%for i in historylabel:
		<div class="labelrecord"> 现在时间是：{{i[0]}}</div>
		<div class="labelrecord"> 宝宝今天{{i[1]}}天</div>
		<div class="labelrecord"> 宝宝今天的表现是：{{i[2]}}</div> 
    %end		
   	</div>
'''

global babyhtml
babyhtml = '''
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

		    .get-title {
		      font-size: 200%;
		      border: 2px solid #fff;
		      padding: 5px;
		      display: inline-block;
		    }

		    .get-btn {
		      background: #fff;
		    }

		    .detail {
		      background: #fff;
		    }

		    .detail-h2 {
		      text-align: center;
		      font-size: 150%;
		      margin: 40px 0;
		    }

		    .detail-h3 {
		      color: #1f8dd6;
		    }

		    .detail-p {
		      color: #7f8c8d;
		    }

		    .detail-mb {
		      margin-bottom: 30px;
		    }

		    .hope {
		      background: #fff37;
		      padding: 50px 0;
		    }

		    .hope-img {
		      text-align: center;
		    }

		    .hope-hr {
		      border-color: #149C88;
		    }

		    .hope-title {
		      font-size: 140%;
		    }

		    .about {
		      background: #fff;
		      padding: 40px 0;
		      color: #7f8c8d;
		    }

		    .about-color {
		      color: #34495e;
		    }

		    .about-title {
		      font-size: 180%;
		      padding: 30px 0 50px 0;
		      text-align: center;
		    }

		    .footer p {
		      color: #7f8c8d;
		      margin: 0;
		      padding: 15px 0;
		      text-align: center;
		      background: #2d3e50;
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

			.no1{			  
				margin:50px;
				border:0;			  
				padding:0;
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
				width:20%;
				display: inline-block;
			}

			.nav_li a{ 
				font-size:16px;
				font-weight:bold;
				display:block; /* 将链接设为块级元素 */
				padding:5px 8px; /* 设置内边距 */
				background:#85c80f; /* 设置背景色 */
				color:#fff; /* 设置文字颜色 */
				text-decoration:none; /* 去掉下划线 */
				border-right:1px solid #fff; /* 在左侧加上分隔线 */
			}

			.active{ 
				background:rgb(212,2,3)
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
	  <div class="am-header-left am-header-nav">
	    <a href="#left-link" class="">
	      <i class="am-header-icon am-icon-home"></i>
	    </a>
	  </div>
	  <h1 class="am-header-title">
	    <a align="center" class=".hope">欢迎使用！</a>
	  </h1>
	  <div class="am-header-right am-header-nav">
	    <a href="#right-link" class="">
	      <i class="am-header-icon am-icon-bars"></i>
	    </a>
	  </div>
	</header>

	<div class="get">
	  <div class="am-g">
	    <div class="am-u-lg-12">
	      <h1 class="get-title">我在长大</h1>
	    </div>
	  </div>
	</div>

	<div class="nav" align="center" >
	    <div class="nav_li" align="center" >
	      <ul>
	        <li ><a href=/>开始记录</a></li>
	        <li><a href=historyhtml>查看历史</a></li>
	        <li><a href=babyhtml>宝宝信息</a></li>
	        <li><a href=emailhtml>发送邮箱</a></li>
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
			<input name="email" type="text" />	<br /><br />			
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

'''

global baby2html
baby2html = '''
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

		    .get-title {
		      font-size: 200%;
		      border: 2px solid #fff;
		      padding: 5px;
		      display: inline-block;
		    }

		    .get-btn {
		      background: #fff;
		    }

		    .detail {
		      background: #fff;
		    }

		    .detail-h2 {
		      text-align: center;
		      font-size: 150%;
		      margin: 40px 0;
		    }

		    .detail-h3 {
		      color: #1f8dd6;
		    }

		    .detail-p {
		      color: #7f8c8d;
		    }

		    .detail-mb {
		      margin-bottom: 30px;
		    }

		    .hope {
		      background: #fff37;
		      padding: 50px 0;
		    }

		    .hope-img {
		      text-align: center;
		    }

		    .hope-hr {
		      border-color: #149C88;
		    }

		    .hope-title {
		      font-size: 140%;
		    }

		    .about {
		      background: #fff;
		      padding: 40px 0;
		      color: #7f8c8d;
		    }

		    .about-color {
		      color: #34495e;
		    }

		    .about-title {
		      font-size: 180%;
		      padding: 30px 0 50px 0;
		      text-align: center;
		    }

		    .footer p {
		      color: #7f8c8d;
		      margin: 0;
		      padding: 15px 0;
		      text-align: center;
		      background: #2d3e50;
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

			.no1{			  
				margin:50px;
				border:0;			  
				padding:0;
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
				width:20%;
				display: inline-block;
			}

			.nav_li a{ 
				font-size:16px;
				font-weight:bold;
				display:block; /* 将链接设为块级元素 */
				padding:5px 8px; /* 设置内边距 */
				background:#85c80f; /* 设置背景色 */
				color:#fff; /* 设置文字颜色 */
				text-decoration:none; /* 去掉下划线 */
				border-right:1px solid #fff; /* 在左侧加上分隔线 */
			}

			.active{ 
				background:rgb(212,2,3)
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
	  <div class="am-header-left am-header-nav">
	    <a href="#left-link" class="">
	      <i class="am-header-icon am-icon-home"></i>
	    </a>
	  </div>
	  <h1 class="am-header-title">
	    <a align="center" class=".hope">欢迎使用！</a>
	  </h1>
	  <div class="am-header-right am-header-nav">
	    <a href="#right-link" class="">
	      <i class="am-header-icon am-icon-bars"></i>
	    </a>
	  </div>
	</header>

	<div class="get">
	  <div class="am-g">
	    <div class="am-u-lg-12">
	      <h1 class="get-title">我在长大</h1>
	    </div>
	  </div>
	</div>

	<div class="nav" align="center" >
	    <div class="nav_li" align="center" >
	      <ul>
	        <li ><a href=/>开始记录</a></li>
	        <li><a href=historyhtml>查看历史</a></li>
	        <li><a href=babyhtml>宝宝信息</a></li>
	        <li><a href=emailhtml>发送邮箱</a></li>
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
'''

global emailhtml
emailhtml ='''
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

		    .get-title {
		      font-size: 200%;
		      border: 2px solid #fff;
		      padding: 5px;
		      display: inline-block;
		    }

		    .get-btn {
		      background: #fff;
		    }

		    .detail {
		      background: #fff;
		    }

		    .detail-h2 {
		      text-align: center;
		      font-size: 150%;
		      margin: 40px 0;
		    }

		    .detail-h3 {
		      color: #1f8dd6;
		    }

		    .detail-p {
		      color: #7f8c8d;
		    }

		    .detail-mb {
		      margin-bottom: 30px;
		    }

		    .hope {
		      background: #fff37;
		      padding: 50px 0;
		    }

		    .hope-img {
		      text-align: center;
		    }

		    .hope-hr {
		      border-color: #149C88;
		    }

		    .hope-title {
		      font-size: 140%;
		    }

		    .about {
		      background: #fff;
		      padding: 40px 0;
		      color: #7f8c8d;
		    }

		    .about-color {
		      color: #34495e;
		    }

		    .about-title {
		      font-size: 180%;
		      padding: 30px 0 50px 0;
		      text-align: center;
		    }

		    .footer p {
		      color: #7f8c8d;
		      margin: 0;
		      padding: 15px 0;
		      text-align: center;
		      background: #2d3e50;
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

			.no1{			  
				margin:50px;
				border:0;			  
				padding:0;
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
				width:20%;
				display: inline-block;
			}

			.nav_li a{ 
				font-size:16px;
				font-weight:bold;
				display:block; /* 将链接设为块级元素 */
				padding:5px 8px; /* 设置内边距 */
				background:#85c80f; /* 设置背景色 */
				color:#fff; /* 设置文字颜色 */
				text-decoration:none; /* 去掉下划线 */
				border-right:1px solid #fff; /* 在左侧加上分隔线 */
			}

			.active{ 
				background:rgb(212,2,3)
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
	  <div class="am-header-left am-header-nav">
	    <a href="#left-link" class="">
	      <i class="am-header-icon am-icon-home"></i>
	    </a>
	  </div>
	  <h1 class="am-header-title">
	    <a align="center" class=".hope">欢迎使用！</a>
	  </h1>
	  <div class="am-header-right am-header-nav">
	    <a href="#right-link" class="">
	      <i class="am-header-icon am-icon-bars"></i>
	    </a>
	  </div>
	</header>

	<div class="get">
	  <div class="am-g">
	    <div class="am-u-lg-12">
	      <h1 class="get-title">我在长大</h1>
	    </div>
	  </div>
	</div>

	<div class="nav" align="center" >
	    <div class="nav_li" align="center" >
	      <ul>
	        <li ><a href=/>开始记录</a></li>
	        <li><a href=historyhtml>查看历史</a></li>
	        <li><a href=babyhtml>宝宝信息</a></li>
	        <li><a href=emailhtml>发送邮箱</a></li>
	        </li>
	      </ul>
	    </div>
	  </div>

    <div >友情提醒：如果第一次使用，请先点击菜单“宝宝信息”上传您宝宝的基本信息，否则系统会出错。</div>
    </br>

	</br></br>
	<div class="labeltitle">系统提示：</div>
	</br>
	<div class="labelrecord">您宝宝的记录已经发送成功发送到邮箱{{momemail}}中。</div>
   	</div>
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

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

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

def validateEmail(email):
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0

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

app = Bottle()
app.route('/', method='GET')(home)

@app.route('/indexhtml', method='POST')
def save():
    newline = request.forms.get('newline')
    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
    babyage = calbabyage()
    data = nowtime.decode('utf-8'), babyage, newline.decode('utf-8')
    inputnewline(data)
    return indexhtml
    
@app.route('/babyhtml', method='GET')
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
    return template(babyhtml, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml,  name=name, gender=gender, birthtime=birthtime, momemail=momemail)

@app.route('/baby2html', method='POST')
def savebaby():
    name = request.forms.get('name')
    gender = request.forms.get('gender')
    birthtime = datetime.date(int(request.forms.get('year')), int(request.forms.get('month')), int(request.forms.get('date')))
    momemail = request.forms.get('email')
    settingtime = time.strftime("%d/%m/%Y %H:%M:%S")
    if name==None or gender==None or birthtime==None or validateEmail(momemail) == 0:
        name = "重新设置"
        gender = "重新设置"
        birthtime = "重新设置"
        momemail = "重新设置"
        return template(babyhtml, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml, name=name, gender=gender, birthtime=birthtime, momemail=momemail)
    else:
        data = name.decode('utf-8'), gender.decode('utf-8'), birthtime, momemail, settingtime
        createbaby(data)
        readbaby()
        return template(baby2html, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml,  name=name, gender=gender, birthtime=birthtime, momemail=momemail)

@app.route('/historyhtml', method='GET')
def history():
    conn = sqlite3.connect(ROOT+'/noterecord.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists record (time text, age text, record text)')
    cursor.execute('select * from record')
    notelist = cursor.fetchall()
    return template(historyhtml, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml,  historylabel=notelist)

@app.route('/emailhtml', method='GET')
def sendmail():
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
    historyrecord =  ROOT+'/noterecord.db' 
    if exists(historyrecord):
        msg = MIMEMultipart()
        msg['From'] = _format_addr(u'我在成长 <%s>' % from_addr)
        msg['To'] = _format_addr(u'亲爱的妈妈 <%s>' % to_addr)
        msg['Subject'] = Header(u'您的宝宝记录……', 'utf-8').encode()
        msg.attach(MIMEText('baby\'s record', 'plain', 'utf-8'))
        with open(historyrecord, 'rb') as f:
            mime = MIMEBase('database', 'db', filename='noterecord.db')
            mime.add_header('Content-Disposition', 'attachment', filename='noterecord.db')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
    else:
        msg = MIMEText('babyy\'s record', 'plain', 'utf-8')
        msg['From'] = _format_addr(u'我在成长 <%s>' % from_addr)
        msg['To'] = _format_addr(u'亲爱的妈妈 <%s>' % to_addr)
        msg['Subject'] = Header(u'您的宝宝记录……', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    return template(emailhtml, indexhtml=indexhtml, historyhtml=historyhtml, babyhtml=babyhtml, emailhtml=emailhtml,  momemail=momemail)

app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)

try:
    server = MyWSGIRefServer(host="localhost", port="8800")
    app.run(server=server, reloader=False)
except Exception, ex:
    print "Exception: %s" % repr(ex)