# _*_coding:utf-8_*_

from bottle import Bottle, request, route, run,template
import sae

from jinja2 import Template
from socket import *
import time
from os.path import exists
import xml.etree.ElementTree as ET

app = Bottle()

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

'''
@app.route("/ping")
def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/plain')])
    return  "The connection is ok !"
application = sae.create_wsgi_app(application) # 这里如果写app就500出错 '''

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