大妈说写网页用Template很好用，今天看QPython的查询公交项目，也用到template了。  

搜索试运行一段代码：  


    from string import Template

	def main():
		str = "My name is $name, my age is $age"
		map = {"name":"picklecai", "age":"34"}
		temp = Template(str)
		result = temp.substitute(map)
		print result
	
	if __name__ == '__main__':
		main()

其中，起先犯的错误是：map赋值时name和age没有带引号，系统运行提示错误为：name变量未定义。  

稍后发现这个template并不是bottle里的template。所以搞错了。  


--  

查看bottle里的template代码，是个函数：  

    def template(*args, **kwargs):
	    '''
	    Get a rendered template as a string iterator.
	    You can use a name, a filename or a template string as first parameter.
	    Template rendering arguments can be passed as dictionaries
	    or directly (as keyword arguments).
	    '''
说的第一个参数就是一个名字。  

查询公交项目中的用法，最简单的是home：  

    def home():
    	return template(ROOT+'/index.html')

只有一个参数，发现这是定义网址的。   
回看常量定义中的ROOT：`ROOT = os.path.dirname(os.path.abspath(__file__))`  

detail中的用法：  

    def detail():
	    city = request.GET['city']
	    q = request.GET['keyword']
	
	    data = _get_json_content(API_URL+"&city="+city+"&q="+q)
	
	    return template(ROOT+'/detail.html', data=data)

第二个参数好像是设置页面内容。

所以使用template的几个函数，就是定义几个网页的。  


