# _*_ coding:utf-8 _*_
#qpy:webapp:simple notebook
#qpy:fullscreen
#qpy://localhost:8800

"""
简易笔记本app
@Author Picklecai
"""

from bottle import *
import os
import sqlite3
import time

ASSETS = "/assets/"
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

def inputnewline(data):
    conn = sqlite3.connect(ROOT+'/noterecord.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists record (time text, record varchar)')
    cursor.execute('insert into record (time, record) values (?,?)', data)
    cursor.close()
    conn.commit()
    conn.close()

def printhistory():
    conn = sqlite3.connect(ROOT+'/noterecord.db')
    cursor = conn.cursor()
    cursor.execute('select * from record')
    return cursor.fetchall()

def home():
    return template(ROOT+'/index.html')

app = Bottle()
app.route('/', method='GET')(home)
app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)

@app.route('/index.html', method='POST')
def save():
    newline = request.forms.get('newline')
    nowtime = time.time()
    data = nowtime, newline
    inputnewline(data)
    records = printhistory() 
    return template(ROOT+'/index.html', historylabel=records)

try:
    server = MyWSGIRefServer(host="localhost", port="8800")
    app.run(server=server, reloader=False)
except Exception, ex:
    print "Exception: %s" % repr(ex)