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


def server_static(filepath):
    return static_file(filepath, root=ROOT+'/assets')


def home():
    inputnewline()
    return template(ROOT+'/index.html')


def save(newline):
    conn = sqlite3.connect('/storage/emulated/0/com.hipipal.qpyplus/project/notebookapp/noterecord.db')
    cursor = conn.cursor()
    cursor.execute('create table record (time text, record varchar)')
    newline = request.get['newline']
    cursor.execute('insert into record (time, record) values (time.strftime("%d/%m/%Y %H:%M:%S"), \'newline\')')
    cursor.close()
    conn.commit()
    conn.close()


@post('/index.html')
def printhistory():
    conn = sqlite3.connect('noterecord.db')
    cursor = conn.cursor()
    cursor.execute('select * from record')
    return cursor.fetchall()


@get('/index.html')
def inputnewline():
    newline = request.get('newline')
    return '''
    <button type="button" name="save" class="am-btn am-btn-primary am-round" onclick="save(newline)"><i class="am-icon-search"></i> save</button>
    <label cols="40" rows="8" name="historylabel" style="">printhistory()</label>
    '''


app = Bottle()
app.route('/', method='GET')(home)
app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)
app.route('/assets/<filepath:path>', method='GET')(server_static)

try:
    server = MyWSGIRefServer(host="localhost", port="8800")
    app.run(server=server, reloader=False)
except Exception, ex:
    print "Exception: %s" % repr(ex)
