# _*_ coding:utf-8 _*_

from bottle import *

'''@route('/index')
def printhistory():
    return '''
'''    <form action="/index" method="history">
    Here are your history records:
    <br/>
    </form>
    '''
@route('/index')
def newline():
    return '''
    <form action="/index" method="POST">
    Please input a new line: 
    <br/>
    <input name="newline" type="text"/>
    <br/>
    <input value="save" type="submit" />
    </form>
    '''
@route('/index', method='POST')
def inputnewline():
    newline = request.forms.get('newline')
    if newline:
        return template("成功", newline=newline)


@route('/hello')
def hello():
    return "hello\n\n"

@route('/about/<name>')
def aboutme(name):
    return "The page is about: %s" % name

if __name__ == '__main__':
    debug(True)
    run(host="localhost", port=8800, reloader=True)
