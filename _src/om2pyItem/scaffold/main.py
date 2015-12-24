# _*_ coding:utf-8 _*_
#qpy:webapp:simple notebook
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

ROOT = os.path.dirname(os.path.abspath(__file__))

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
    return template(ROOT+'/index.html')

def calbabyage():
    today = datetime.date.today()
    filename = ROOT+'/babyinfo.db' 
    if exists(filename):
        conn = sqlite3.connect(ROOT+'/babyinfo.db')
        cursor = conn.cursor()
        cursor.execute('select birthtime from babyinfo order by settingtime desc limit 0,1')
        bn = str(cursor.fetchall())
        babybirth = datetime.date(int(bn[4:8]), int(bn[9:11]), int(bn[12:14]))
    babyage = str(today - babybirth)
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
    cursor.execute('create table if not exists babyinfo (name text, gender text, birthtime text, settingtime text)')
    cursor.execute('insert into babyinfo (name, gender, birthtime, settingtime) values (?,?,?,?)', data)
    cursor.close()
    conn.commit()
    conn.close()

def readbaby():
    conn = sqlite3.connect(ROOT+'/babyinfo.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists babyinfo (name text, gender text, birthtime text, settingtime text)')
    cursor.execute('select * from babyinfo')
    babyinfolist = cursor.fetchall()
    return babyinfolist

app = Bottle()
app.route('/', method='GET')(home)

@app.route('/index.html', method='POST')
def save():
    newline = request.forms.get('newline')
    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
    babyage = calbabyage()
    data = nowtime.decode('utf-8'), babyage, newline.decode('utf-8')
    inputnewline(data)
    return template(ROOT+'/index.html')
    
@app.route('/baby.html', method='GET')
def baby():
    return template(ROOT+'/baby.html')

@app.route('/baby2.html', method='POST')
def savebaby():
    name = request.forms.get('name')
    gender = request.forms.get('gender')
    birthtime = datetime.datetime(int(request.forms.get('year')), int(request.forms.get('month')), int(request.forms.get('date')))
    settingtime = time.strftime("%d/%m/%Y %H:%M:%S")
    if name==None or gender==None or birthtime==None:
        return None
    else:
        data = name.decode('utf-8'), gender.decode('utf-8'), birthtime, settingtime
        createbaby(data)
        readbaby()
        return template(ROOT+'/baby2.html', name=name, gender=gender, birthtime=birthtime)

@app.route('/history.html', method='GET')
def history():
    conn = sqlite3.connect(ROOT+'/noterecord.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists record (time text, age text, record text)')
    cursor.execute('select * from record')
    notelist = cursor.fetchall()
    return template(ROOT+'/history.html', historylabel=notelist)

@app.route('/history.html', method='POST')
def sendEmail():
    email = request.forms.get('email')
    validateEmail(email)

app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)

try:
    server = MyWSGIRefServer(host="localhost", port="8800")
    app.run(server=server, reloader=False)
except Exception, ex:
    print "Exception: %s" % repr(ex)