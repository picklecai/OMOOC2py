# _*_ coding:utf-8 _*_
#qpy:webapp:simple notebook
#qpy:fullscreen
#qpy://localhost:8800

"""
?????app
@Author Picklecai
"""

from bottle import *
import os
import sqlite3
import time

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
    newline = request.forms.get('newline')
    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
    data = nowtime.decode('utf-8'), newline.decode('utf-8')
    conn = sqlite3.connect(ROOT+'/noterecord.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists record (time text, record text)')
    cursor.execute('insert into record (time, record) values (?,?)', data)
    cursor.close()
    conn.commit()
    conn.close()
    return template(ROOT+'/index.html')

def history():
    conn = sqlite3.connect(ROOT+'/noterecord.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists record (time text, record text)')
    cursor.execute('select * from record')
    notelist = cursor.fetchall()
    return template(ROOT+'/history.html', historylabel=notelist)

app = Bottle()
app.route('/', method='GET')(home)
app.route('/history', method=['GET'])(history)
app.route('/baby', method=['GET'])
app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)

try:
    server = MyWSGIRefServer(host="localhost", port="8800")
    app.run(server=server, reloader=False)
except Exception, ex:
    print "Exception: %s" % repr(ex)