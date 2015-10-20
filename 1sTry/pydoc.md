## powshell中查看
进入任意目录，如：F:\\>py>，输入： 
<pre><code>python -m pydoc 函数名</pre></code>    

可直接查看到结果。  

## 浏览器中查看
在本地机器上，按照给定的端口启动HTTP运行pydoc。  

1. 进入任意目录，如：F:\\>py>，输入：    
<pre><code>python -m pydoc -p 1234</pre></code>   
注释：#比如说: 端口为1234

2. 出现提示：
> pydoc server ready at http://localhost:1234/     

3. 即可在浏览器中输入以下地址查看pydoc文档。  
<pre><code>http://localhost:1234/</pre></code>a
