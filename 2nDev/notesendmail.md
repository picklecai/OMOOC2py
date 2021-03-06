## 邮箱  

[SMTP发送邮件 - 廖雪峰的官方网站](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832745198026a685614e7462fb57dbf733cc9f3ad000)  

[企业退信的常见问题？-163邮箱常见问题](http://help.163.com/09/1224/17/5RAJ4LMH00753VB8.html)  

尝试代码：  

    # _*_ coding:utf-8 _*_

	from email.mime.text import MIMEText
	import smtplib
	
	from_addr = "pickle.ahcai@163.com"
	password = "ahcai318"
	smtp_server = "smtp.163.com"
	to_addr = "cmj_827@163.com"
	msg = MIMEText('baby record', 'plain', 'utf-8')
	server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
	server.set_debuglevel(1)
	server.login(from_addr, password)
	server.sendmail(from_addr, [to_addr], msg.as_string())
	server.quit()


运行结果：  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-25/9166882.jpg)  

错误代码：554,DT SPAM  
> •554 DT:SPM 发送的邮件内容包含了未被许可的信息，或被系统识别为垃圾邮件。请检查是否有用户发送病毒或者垃圾邮件；  

[网易反垃圾邮件政策说明-163邮箱常见问题](http://help.163.com/09/1224/14/5RAB4VK500753VB8.html?servCode=6010330)  

> 垃圾邮件的属性  
发送到网易邮箱服务或通过网易邮箱服务发送或导致发送的电子邮件不允许：  
1、收件人事先没有提出要求或者同意接收且无法拒收的；  
2、使用或包括无效的或伪造的邮件头；  
3、使用或包括伪造的、无效的或者不存在的域名；  
4、利用任何技术伪造、隐藏或掩盖传输路径来源的识别信息；  
5、使用任何方式生成欺骗性地址信息；  
6、在没有获得第三方许可的情况下使用、中继或通过第三方的互联网设备；  
7、主题行或内容包含错误、误导或虚假的信息；  
8、违反了国家相关法律规定和网易服务条款。  

按照廖雪峰的做法，修改补充邮件信息。  
代码：  

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

运行，邮件发送成功。  

将以上代码移到main.py中，运行，出现错误仍然是550。  
![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-25/84823780.jpg)  

错误代码：550 Invalid User
> 550 Invalid User 请求的用户不存在；  

这是因为页面刚打开，没有设置收件地址。    
按照之前思路，把收件箱填入数据库，再从数据库读出email地址。打开发送邮件页时，直接就读取数据库email地址进行邮件发送。  

把发送动作放在history，不行。发送成功后，history页面的内容无法查看。需要另外再设置一个页面做这件事。  

另外增加了一个email页面，并把链接放到菜单中。修改sendmail的返回为email.html地址，成功运行。  

![](http://7xotr7.com1.z0.glb.clouddn.com/15-12-25/51461470.jpg)  

按照廖雪峰的笔记，添加附件。为了安全起见，在sendemail中，加入了if判断：如果有记录文件，就发送带附件email。如果没有，就发送原来的纯文本无附件email。  

[18.1.4. email.mime: Creating email and MIME objects from scratch — Python 2.7.11 documentation](https://docs.python.org/2/library/email.mime.html#email.mime.base.MIMEBase)

根据global name未定义的提示，加入了两句导入：  

    from email.mime.multipart import MIMEMultipart
	from email.mime.base import MIMEBase

将廖雪峰的图片附件改为db文件时，  

    mime = MIMEBase('database', 'db', filename='noterecord.db')  

猜测了database这个主类型，居然正确。  
