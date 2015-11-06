# _*_ coding:utf-8 _*_

from bottle import *

@route('/hello')
def hello():
	return "hello\n\n"

@route('/inputwin/<name>')
def inputwin(name):
	return "Please input: %s" % name

if __name__ == '__main__':
    run(host="localhost", port=8800)
