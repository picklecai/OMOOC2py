# _*_ coding:utf-8 _*_

from bottle import *

@route('/hello')
def hello():
	return "hello\n\n"

@route('/about/<name>')
def aboutme(name):
	return "The page is about: %s" % name

if __name__ == '__main__':
	debug(True)
    run(host="localhost", port=8800, reloader=True) 
