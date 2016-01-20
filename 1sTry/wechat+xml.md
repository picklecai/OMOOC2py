## 材料学习：  
### 1. 学习微信公众平台   

1.1 区别**微信公众平台**和**微信开发平台**  

> 微信公众平台开发是指为微信公众号进行业务开发，为移动应用、PC端网站、公众号第三方平台（为各行各业公众号运营者提供服务）的开发，请前往微信开放平台接入。  

微信公众平台：为微信公众号进行业务开发  
微信开发平台：为移动应用、PC端网站、公众号第三方平台（为各行各业公众号运营者提供服务）开发  

1.2 填写服务器配置

登录微信公众平台官网后，在公众平台后台管理页面 - 开发者中心页，点击“修改配置”按钮，填写服务器地址（URL）、Token和EncodingAESKey，其中URL是开发者用来接收微信消息和事件的接口URL。Token可由开发者可以任意填写，用作生成签名（该Token会和接口URL中包含的Token进行比对，从而验证安全性）。EncodingAESKey由开发者手动填写或随机生成，将用作消息体加解密密钥。

同时，开发者可选择消息加解密方式：明文模式、兼容模式和安全模式。模式的选择与服务器配置在提交后都会立即生效，请开发者谨慎填写及选择。加解密方式的默认状态为明文模式，选择兼容模式和安全模式需要提前配置好相关加解密代码，详情请参考消息体签名及加解密部分的文档。   

1.3 接受普通消息  
文本消息  

    <xml>
    <ToUserName><![CDATA[toUser]]></ToUserName>
    <FromUserName><![CDATA[fromUser]]></FromUserName> 
    <CreateTime>1348831860</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[this is a test]]></Content>
    <MsgId>1234567890123456</MsgId>
    </xml>  

凑巧又看见时间戳。  

参数：

![](http://i5.tietuku.com/9807a3d370cf250c.png)  

### 2. 学习XML  

在学习目录（i:/py）下依照教程建立country_data.xml文件。打开命令行，转入学习目录，再进入python。

2.1 import xml:   

    import xml.etree.ElementTree as ET
    tree = ET.parse('country_data.xml')
    root = tree.getroot()

2.2 tag、attrib和text  

tag相对于其他地方的type。  

    >>> for child in root:
    ...   print child.tag, child.attrib
    ...
    country {'name': 'Liechtenstein'}
    country {'name': 'Singapore'}
    country {'name': 'Panama'}

注意：在命令行中写for语句，for的内部代码之前要空两格，否则提示错误 `IndentationError:expected an indented block`。例如上面的“print”之前。  

有text和没有的区别：  
有text：  

    >>> root[0][1].text
    '2008'

没有text：  

    >>> root[0][1]
    <Element 'year' at 0x23c3da0> 

2.3 修改xml文件  

用Element.set()和ElementTree.write()  

    >>> for rank in root.iter('rank'):
    ...   new_rank = int(rank.text) + 1
    ...   rank.text = str(new_rank)
    ...   rank.set('updated', 'yes')
    ...
    >>> tree.write('output.xml')

查看新生成的output.xml，rank变成了2，5，69。  
注意：做好格式转换。int()和str()   

2.4 subelement和NameSpace  

SubElement:  

    >>> a = ET.Element('a')
    >>> b = ET.SubElement(a, 'b')
    >>> c = ET.SubElement(a, 'c')
    >>> d = ET.SubElement(c, 'd')
    >>> ET.dump(a)
    <a><b /><c><d /></c></a>

看上去xml用了存储二叉树是极好的。  

Namespace: 

加前缀和不加前缀的区别：  

    <?xml version="1.0"?>
	    <actors xmlns:fictional="http://characters.example.com"
	        xmlns="http://people.example.com">
	    <actor>
	        <name>John Cleese</name>
	        <fictional:character>Lancelot</fictional:character>
	        <fictional:character>Archie Leach</fictional:character>
	    </actor>
	    <actor>
	        <name>Eric Idle</name>
	        <fictional:character>Sir Robin</fictional:character>
	        <fictional:character>Gunther</fictional:character>
	        <fictional:character>Commander Clement</fictional:character>
	    </actor>
    </actors>

在这个文件中，不加前缀的是actor本人信息，加前缀的是他所表演的角色信息。所以一个actor可以对应好几个fictional角色。

从people里取name，从characters里取char。  
以下代码没能在命令行中正确运行，提示说fromstring未定义。  

    root = fromstring(xml_text)
	for actor in root.findall('{http://people.example.com}actor'):
	    name = actor.find('{http://people.example.com}name')
	    print name.text
	    for char in actor.findall('{http://characters.example.com}character'):
	        print ' |-->', char.text

2.5 URI  

URI，大妈已经讲了好几次了：  

> 在电脑术语中，统一资源标识符（Uniform Resource Identifier，或URI)是一个用于标识某一互联网资源名称的字符串。 该种标识允许用户对网络中（一般指万维网）的资源通过特定的协议进行交互操作。URI的最常见的形式是统一资源定位符（URL），经常指定为非正式的网址。更罕见的用法是统一资源名称（URN），其目的是通过提供一种途径。用于在特定的命名空间资源的标识，以补充网址。
> —— From [统一资源标志符 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E7%BB%9F%E4%B8%80%E8%B5%84%E6%BA%90%E6%A0%87%E5%BF%97%E7%AC%A6)  

与URL和URN的关系：  

> URI可被视为定位符（URL），名称（URN）或两者兼备。统一资源名（URN）如同一个人的名称，而统一资源定位符（URL）代表一个人的住址。换言之，URN定义某事物的身份，而URL提供查找该事物的方法。  
> —— From [统一资源标志符 - 维基百科，自由的百科全书](https://zh.wikipedia.org/wiki/%E7%BB%9F%E4%B8%80%E8%B5%84%E6%BA%90%E6%A0%87%E5%BF%97%E7%AC%A6#.E4.B8.8EURL.E5.92.8CURN.E7.9A.84.E5.85.B3.E7.B3.BB)  

标记语言中URI引用的使用  
> 在HTML中，img元素的src属性值是URI引用，a或link元素的href属性值亦如是。  
> 在XML中，在一个DTD中的SYSTEM关键字之后出现的系统描述符是一个无片段的URI引用。  
> 在XSLT中，xsl:import元素/指令的href属性值是一个URI引用，document()函数的第一个参数与之相仿。  

绝对URI的例子   
> http://example.org/absolute/URI/with/absolute/path/to/resource.txt  
> ftp://example.org/resource.txt  
> urn:issn:1535-3613   

与XML命名空间的关系
> XML拥有一个叫命名空间的，一个可包含元素集和属性名称的抽象域的概念。命名空间的名称（一个必须遵守通用URI文法的字符串）用于标识一个XML命名空间。但是，命名空间的名称一般不被认为是一个URI，因为URI规范定义了字符串的“URI性”是根据其目的而不是其词法组成决定的。一个命名空间名称同时也并不一定暗示任何URI协议的语义；例如，一个以“http:”开头的命名空间名称很可能与HTTP协议没有任何关系。XML专家们就这一问题在XML开发电子邮件列表上进行了深入的辩论；一部分人认为命名空间名称可以是URI，由于包含一个具体命名空间的名称集可以被看作是一个被标识的资源，也由于“XML中的命名空间”规范的一个版本指出过命名空间名称“是”一个URI引用。但是，集体共识似乎指出一个命名空间名称只是一个凑巧看起来像URI的字符串，仅此而已。

> 早先，命名空间名称是可以匹配任何非空URI引用的语法的，但后来的一个对于“XML命名空间建议”的订正废弃了相对URI引用的使用。一个独立的、针对XML 1.1的命名空间的规范允许使用IRI引用作为命名空间名称的基准，而不仅是URI引用。

> 为了消除XML新人中产生的对于URI（尤其是HTTP URL）的使用的困惑，一个被称为RDDL（资源目录描述语言）的描述语言被创建了，虽然RDDL的规范并没有正式地位，也并没有获得任何相关组织（例如W3C）的检查和支持。一个RDDL文档可以提供关于一个特定命名空间和使用它的XML文档的，机器与人类都能读懂的信息。XML文档的作者鼓励使用RDDL文档，这样一旦文档中的命名空间名称被索引，（系统）就会获取一个RDDL文档。这样，许多开发者对于让命名空间名称指向网络可达资源的需求就能得到满足。