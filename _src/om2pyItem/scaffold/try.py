# _*_ coding:utf-8 _*_

from email.mime.text import MIMEText
import smtplib
from email import encoders
from email.header import Header
from email.utils import parseaddr, formataddr

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

from_addr = "pickle.ahcai@163.com"
password = "ahcai318"
smtp_server = "smtp.163.com"
to_addr = "cmj_827@163.com"

msg = MIMEText('baby record', 'plain', 'utf-8')
msg['From'] = _format_addr(u'我在成长 <%s>' % from_addr)
msg['To'] = _format_addr(u'亲爱的妈妈 <%s>' % to_addr)
msg['Subject'] = Header(u'您的宝宝记录……', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()