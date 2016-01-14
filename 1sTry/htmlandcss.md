# HTML和CSS学习记录  

## CSS  

### 1. 用margin居中
margin:auto用来居中，这个用法，不能用在全长度上，要用在宽度width是固定数值或固定比例上。   
代码举例：  

    .content_li
	{
		width: 70%;
		margin: auto;
	}

### 2. id和class	 
\#用在id前面，\.用在class前面。  
代码举例：  
class

    .footer
	{
		background-color: #85c80f;
		font-family: "Microsoft YaHei" ! important;
	}

html中写：  

    class="";

id

    #footer
	{
		background-color: #85c80f;
		font-family: "Microsoft YaHei" ! important;
	}

html中写：  

    id="";

id的优先级高于class。  

### 3.菜单的下划线  
实际上是菜单的下边框。  

按照《十天学会DIV+CSS.chm》中的做法，下划线始终只出现在文字下。  

用chrome的审查元素，一个样式一个样式地去勾选，终于发现问题出现在全局样式的ul li。前几天为了省事，写了一个全局的ul li{float:left} 把这个去掉，只在需要的地方写。结果就好了。  

更改情况：  
![](http://7xotr7.com1.z0.glb.clouddn.com/16-1-14/92476318.jpg)  

