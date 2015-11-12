# Web版记事本说明书  

##功能说明：  
1. 输入网址：[http://localhost:8800/index](http://localhost:8800/index)，进入网站。  
2. 在history[http://localhost:8800/history](http://localhost:8800/history)页面可直接查看之前输入历史。  
3. 在index页面，可以输入新记录，点击save即在当前页面打印输入内容。如需继续输入，则后退。  

##使用帮助：  
1. 首先在命令行终端运行主程序notebookweb.py，运行起来后，到浏览器输入网址[http://localhost:8800/index](http://localhost:8800/index)进入记事本记录输入和查看。  
2. 在命令行终端输入Ctrl+C退出后，进入等待命令行输入模式，用另一个终端运行客户端程序notebooknetc.py，即可如3w一般输入和接受。  
3. 无论是网页输入还是命令行输入，都会存储在tempfile文件中，可在下一次运行网站时，到history界面找到所有记录。
