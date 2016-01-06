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