# _*_ coding:utf-8 _*_
#qpy:webapp:simple notebook
#qpy:fullscreen
#qpy://localhost:8800

from bottle import *

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
        #sys.stderr.close()
        import threading 
        threading.Thread(target=self.server.shutdown).start() 
        #self.server.shutdown()
        self.server.server_close() 
        print "# QWEBAPPEND"



def __exit():
	global server
	server.stop()

def __ping():
	return "OK"

def home():
	return template(ROOT+'/index.html')

def main():
    BUF_SIZE = 65565
    ss = socket(AF_INET, SOCK_DGRAM)
    ss_addr = ('127.0.0.1', 8800)
    ss.bind(ss_addr)
    while True:
        print "waiting for data"
        data, cs = ss.recvfrom(BUF_SIZE)
        print 'Connected by', cs, 'Receive Data: ', data, 'at: ', time.strftime("%d/%m/%Y %H:%M:%S"+"\n")
        ss.sendto(data, cs)
    history(data)
    ss.close   


@get('/index')
def newline():
    return '''
    <form action="/index" method="POST">
    history
    <br/>    
    Please input a new line: 
    <br/>
    <input name="newline" type="text"/>
    <br/>
    <input value="save" type="submit" />
    </form>
    '''

@post('/index')
def inputnewline():
    newline = request.forms.get('newline')
    if newline:
        save(newline)
        printhistory()
        return newline

app = Bottle()
app.route('/', method='GET')(home)
app.route('/__exit', method=['GET','HEAD'])(__exit)
app.route('/__ping', method=['GET','HEAD'])(__ping)

try:
    server = MyWSGIRefServer(host="localhost", port="8800")
    app.run(server=server,reloader=False)
except Exception,ex:
    print "Exception: %s" % repr(ex)