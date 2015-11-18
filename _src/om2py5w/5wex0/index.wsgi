import sae
from bottle import *
from jinja2 import Template
from socket import *
import time
from os.path import exists
import sae.kvdb

app = Bottle()

@app.route('/')
def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/plain')])
    return  "Hello, my notebook."
application =sae.create_wsgi_app(application)