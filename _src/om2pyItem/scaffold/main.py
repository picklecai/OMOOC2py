# _*_ coding:utf-8 _*_
#qpy:webapp:babyrecord
#qpy:fullscreen
#qpy://localhost:8800

"""
Babyrecordapp
@Author Picklecai
"""

import os
from os.path import exists
from bottle import Bottle, ServerAdapter, request, template
import sqlite3
import time
import datetime
from email.header import Header

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
    filename = ROOT+'/babyinfo.db'
    if exists(filename):
        return template(ROOT+'/index.html')
    else:
        name = "未设置"
        gender = "未设置"
        birthtime = "未设置"
        momemail = "未设置"
        return template(ROOT+'/baby.html', name=name, gender=gender, birthtime=birthtime, momemail=momemail)

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

def save():
    newline = request.forms.get('newline')
    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
    babyage = calbabyage()
    data = nowtime.decode('utf-8'), babyage, newline.decode('utf-8')
    inputnewline(data)
    return template(ROOT+'/index.html')

def history():
    conn = sqlite3.connect(ROOT+'/noterecord.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists record (time text, age text, record text)')
    cursor.execute('select * from record')
    notelist = cursor.fetchall()
    return template(ROOT+'/history.html', historylabel=notelist)

def createbaby(data):
    conn = sqlite3.connect(ROOT+'/babyinfo.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists babyinfo (name text, gender text, birthtime text, momemail text, settingtime text)')
    cursor.execute('insert into babyinfo (name, gender, birthtime, momemail, settingtime) values (?,?,?,?,?)', data)
    cursor.close()
    conn.commit()
    conn.close()

def readbaby():
    conn = sqlite3.connect(ROOT+'/babyinfo.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists babyinfo (name text, gender text, birthtime text, momemail text, settingtime text)')
    cursor.execute('select * from babyinfo')
    babyinfolist = cursor.fetchall()
    return babyinfolist

def calbabyage():
    today = datetime.date.today()
    filename = ROOT+'/babyinfo.db'
    if exists(filename):
        conn = sqlite3.connect(ROOT+'/babyinfo.db')
        cursor = conn.cursor()
        cursor.execute('select birthtime from babyinfo order by settingtime desc limit 0,1')
        bn = str(cursor.fetchall())
        babybirth = datetime.date(int(bn[4:8]), int(bn[9:11]), int(bn[12:14]))
    babyage = str((today - babybirth).days)
    return babyage

def baby():
    filename = ROOT+'/babyinfo.db'
    if exists(filename):
        conn = sqlite3.connect(ROOT+'/babyinfo.db')
        cursor = conn.cursor()
        cursor.execute('select name from babyinfo order by settingtime desc limit 0,1')
        n = str(cursor.fetchall())
        name = n[4:-4].decode('unicode_escape')
        cursor.execute('select gender from babyinfo order by settingtime desc limit 0,1')
        g = str(cursor.fetchall())
        gender = g[4:-4].decode('unicode_escape')
        cursor.execute('select birthtime from babyinfo order by settingtime desc limit 0,1')
        bn = str(cursor.fetchall())
        birthtime = datetime.date(int(bn[4:8]), int(bn[9:11]), int(bn[12:14]))
        cursor.execute('select momemail from babyinfo order by settingtime desc limit 0,1')
        em = str(cursor.fetchall())
        momemail = em[4:-4].decode('utf-8')
    else:
        name = "未设置"
        gender = "未设置"
        birthtime = "未设置"
        momemail = "未设置"
    return template(ROOT+'/baby.html', name=name, gender=gender, birthtime=birthtime, momemail=momemail)

def savebaby():
    name = request.forms.get('name')
    gender = request.forms.get('gender')
    birthtime = datetime.date(int(request.forms.get('year')), int(request.forms.get('month')), int(request.forms.get('date')))
    momemail = request.forms.get('email')
    settingtime = time.strftime("%d/%m/%Y %H:%M:%S")
    if name==None or gender==None or birthtime==None or validateEmail(momemail)== 0:
        name = "重新设置"
        gender = "重新设置"
        birthtime = "重新设置"
        momemail = "重新设置"
        return template(ROOT+'/baby.html', name=name, gender=gender, birthtime=birthtime, momemail=momemail)
    else:
        data = name.decode('utf-8'), gender.decode('utf-8'), birthtime, momemail, settingtime
        createbaby(data)
        readbaby()
        return template(ROOT+'/baby2.html', name=name, gender=gender, birthtime=birthtime, momemail=momemail)

def _format_addr(s):
    from email.utils import parseaddr, formataddr
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

def validateEmail(email):
    import re
    if len(email) > 7:
        if re.match("^.+\\@(\\[?)[a-zA-Z0-9\\-\\.]+\\.([a-zA-Z]{2,3}|[0-9]{1,3})(\\]?)$", email) != None:
            return 1
    return 0

def sendmail():
    # 导入email模块
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
    from email import encoders
    import smtplib
    # 设置邮件变量
    from_addr = "pickle.ahcai@163.com"
    password = "ahcai318"
    smtp_server = "smtp.163.com"
    filename = ROOT+'/babyinfo.db'
    if exists(filename):
        conn = sqlite3.connect(ROOT+'/babyinfo.db')
        cursor = conn.cursor()
        cursor.execute('select momemail from babyinfo order by settingtime desc limit 0,1')
        em = str(cursor.fetchall())
        momemail = em[4:-4].decode('utf-8')
    else:
        momemail = "caimeijuan@gmail.com"
    to_addr = momemail
    historyrecord = ROOT+'/noterecord.db'
    # 发邮件
    if exists(historyrecord):
        msg = MIMEMultipart()
        msg['From'] = _format_addr(u'我在长大 <%s>' % from_addr)
        msg['To'] = _format_addr(u'亲爱的妈妈 <%s>' % to_addr)
        msg['Subject'] = Header(u'您的宝宝记录……', 'utf-8').encode()
        msg.attach(MIMEText('附件是您宝宝的日常记录，请查收。祝您生活愉快！宝宝健康快乐！', 'plain', 'utf-8'))
        with open(historyrecord, 'rb') as f:
            mime = MIMEBase('database', 'db', filename='noterecord.db')
            mime.add_header('Content-Disposition', 'attachment', filename='noterecord.db')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            mime.set_payload(f.read())
            encoders.encode_base64(mime)
            msg.attach(mime)
    else:
        msg = MIMEText('您尚未开始记录宝宝的日常记录，记录后可收到带宝宝记录附件的邮件！', 'plain', 'utf-8')
        msg['From'] = _format_addr(u'我在长大 <%s>' % from_addr)
        msg['To'] = _format_addr(u'亲爱的妈妈 <%s>' % to_addr)
        msg['Subject'] = Header(u'您的宝宝记录……', 'utf-8').encode()
    server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()
    return template(ROOT+'/email.html', momemail=momemail)

def savephotoname(data):
    # 保存照片名列表
    conn = sqlite3.connect(ROOT+'/photoname.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists photoname (time text, name text)')
    cursor.execute('insert into photoname (time, name) values (?,?)', data)
    cursor.close()
    conn.commit()
    conn.close()

def readphotoname():
    conn = sqlite3.connect(ROOT+'/photoname.db')
    cursor = conn.cursor()
    cursor.execute('create table if not exists photoname (time text, name text)')
    cursor.execute('select * from photoname')
    namelist = cursor.fetchall()
    return namelist

def camerababy():
    import androidhelper
    droid = androidhelper.Android()
    if not exists(ROOT+'/photo'):
        photoid = 1
        os.makedirs(ROOT+'/photo')
    else:
        photoid = sum([len(files) for root,dirs,files in os.walk(ROOT+'/photo')]) + 1
    # 设置照片名
    photoname = str('babyrecordphoto%d.jpg' % photoid)
    # 拍照
    droid.cameraInteractiveCapturePicture(ROOT+'/photo/%s' % photoname)
    # 保存照片名
    nowtime = time.strftime("%d/%m/%Y %H:%M:%S")
    data = nowtime, photoname
    savephotoname(data)
    # 读取照片名
    namelist = readphotoname()
    return template(ROOT+'/camera.html', photoid=photoid, photoname=namelist)

app = Bottle()
app.route('/', method='GET')(home)
app.route('/index.html', method='POST')(save)
app.route('/history.html', method='GET')(history)
app.route('/baby.html', method='GET')(baby)
app.route('/baby2.html', method='POST')(savebaby)
app.route('/email.html', method='GET')(sendmail)
app.route('/camera.html', method='GET')(camerababy)
app.route('/__exit', method=['GET', 'HEAD'])(__exit)
app.route('/__ping', method=['GET', 'HEAD'])(__ping)

try:
    server = MyWSGIRefServer(host="localhost", port="8800")
    app.run(server=server, reloader=False)
except Exception, ex:
    print "Exception: %s" % repr(ex)