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

### 3. 菜单的下划线  
实际上是菜单的下边框。  

按照《十天学会DIV+CSS.chm》中的做法，下划线始终只出现在文字下。  

用chrome的审查元素，一个样式一个样式地去勾选，终于发现问题出现在全局样式的ul li。前几天为了省事，写了一个全局的ul li{float:left} 把这个去掉，只在需要的地方写。结果就好了。  

更改情况：  
![](http://7xotr7.com1.z0.glb.clouddn.com/16-1-14/92476318.jpg)   

### 4. div的显示与隐藏  

被显示和隐藏的div，初始display为none。这个要写在元素里，不能写到外部样式表中去。  

代码：  

![](http://7xotr7.com1.z0.glb.clouddn.com/16-1-15/20087293.jpg)  

写js时，注意“=”和“==”不能误用：  

    	function showandhidden(){ 
			var div1=document.getElementById("babymenu"); 
			if(div1.style.display=='none')
				{
					div1.style.display='block';
				}
			else
				{
					div1.style.display='none';
				} 
			}
if判断中，起初写的“=”，结果就只能执行一次，后面就无效了……  这个错误应该是后来引入的，昨天写的还是“==”呢。  

### 5. div显示后其他元素移位问题  

菜单div显示后，conten中其他的元素（分类列表）下移。试图用div覆盖来解决，但是div覆盖多为覆盖到之前元素的（见：[CSS中div覆盖另一个div](http://blog.csdn.net/jimmy609/article/details/7619464)），方法是margin-top为负值。  

后来在[隐藏与显示：display/visibility/visible区别](http://www.cnblogs.com/kandyvip/p/3210296.html)中发现其他显示和隐藏方法：  

	<div style="display:">显示</div>
	<div style="display:none;">隐藏不占位</div>
	
	<div style="visibility:">显示</div>
	<div style="visibility:hidden;">隐藏占位</div>
	
	<div visible="true" runat="server">显示</div>
	<div visible="false" runat="server">消失不占位</div>

隐藏还占位的,就是visibility的hidden了.于是改代码为:  

    <div id="babymenu" style="visibility:hidden; ">
	……
	……
    <script type="text/javascript"> 
		function showandhidden(){ 
			var div1=document.getElementById("babymenu"); 
			if(div1.style.visibility=='hidden')
				{
					div1.style.visibility='';
				}
			else
				{
					div1.style.visibility='hidden';
				} 
			}
	</script>  

运行结果暂时可以：  

点击前：  
![](http://7xotr7.com1.z0.glb.clouddn.com/16-1-15/93410722.jpg)  

点击后：  
![](http://7xotr7.com1.z0.glb.clouddn.com/16-1-15/41937062.jpg)  

但是：当增加了宝宝信息后，菜单变长了。这些元素列表再下移，就不好看了。  

所以这是临时解决方案，还是要找到覆盖列表的方法。   

### 6. div显示与隐藏功能的复用  

在原来的脚本中，showandhidden函数，在另一个地方想再实现这个功能——例如右边的搜索框，点击放大镜图片，显示搜索框，再点击隐藏——就需要再抄一遍代码，另外给div1赋值。感觉这个重复劳动可以省去。  

起先试图类，搜索了一下，[Javascript定义类（class）的三种方法 - 阮一峰的网络日志](http://www.ruanyifeng.com/blog/2012/07/three_ways_to_define_a_javascript_class.html)，阮一峰说这个本来是不支持类的，只能模拟。支持类的我也还闹不清楚。放弃。  

中间试着给function加参数，加了两个参数，divcontrol和div1。然后发现divcontrol，其他人是在另一个函数来定义的，效果是让html中少写一个onclick。[javascript如何实现点击切换div的显示和隐藏-蚂蚁部落](http://www.softwhy.com/forum.php?mod=viewthread&tid=7957) 根据这里用的window.onload思索，估计也就只能一次性用用。  

接着把divcontrol去掉，仍然在html中加上onclick动作。  

突然发现：有了参数div1之后，它不会在我未赋值时说div1未赋值了。于是改成这样：  

    <script type="text/javascript">
		function showandhidden(div1){
			if(div1.style.visibility=='hidden')
				{
					div1.style.visibility='';
				}
			else
				{
					div1.style.visibility='hidden';
				} 
			}
	</script> 

最简方法函数了。  

在html中：  

    <div class="headerleft" onclick="showandhidden(babymenu)";>  

注意不能在babymenu上加引号。  

运行成功。  

于是在搜索按钮上照旧：  

    <img src="/assets/images/search.png" width="30" height="30" onclick="showandhidden(searchbar);" />  

完美实现！ XD  

回想一下，就应该直接用参数控制。因为使用形参不熟练，所以绕了一大圈，又回到这里来了。  