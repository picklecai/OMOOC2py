# _*_coding:utf-8_*_

from bottle import Bottle, request, route, run,template
import sae
import time
from os.path import exists
import xml.etree.ElementTree as ET
import sae.kvdb

kv = sae.kvdb.Client()
count = 0

# 将数据存进数据库
def inputnewline(newline):
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
    notelist = []
    for item in kv.get_by_prefix('id'):
        notelist.append(item[1])
    return notelist

app = Bottle()

@app.route('/')
def home():
    return  '''
    <form action="/index" method="POST">
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

@app.route('/index', method='POST')
def save():
    newline = request.forms.get('newline')
    inputnewline(newline)
    historylabel = printhistory()
    return  "{historylabel}"