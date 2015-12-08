# GitBook 私人教程

## 背景

win7或win8；  
Github帐号已经与Gitbook帐号关联。

## 步骤

1. 在github上新建一个repository（可以完全新建，也可以fork已有模板）。   
2. 新建的repository种至少含有三个文件：  
  2.1 README.md  
  其内容作为书的简介。   
  2.2 SUMMARY.md  
  其中所索引的文件将会出现在book中，如果没有，则不会出现在book里。  
  2.3 book.json  
  为了配置DISQUS而存在，代码见后。  
3. 在gitbook中新建一本书，填入自己想要写的书名，在书的相对地址中填入github里新建的repository名字。描述可空，日后再补。  
4. 从MY BOOKS中进入该书的details页面，点击右边的settings，先检查GIT URL是否正确（正确形式是：`https://github.com/用户名/新建repository目录名.git`）。  
5. 如果正确，在右列菜单中点击GitHub菜单，检查GitHub Repository是否填写，如果没有填写，填入相对地址`用户名/新建repository目录名`。  
6. 注意！每一步更改都记得点击绿色的Save按钮进行保存。没有保存的话，离开当前页面不会有系统提示。  
7. 最后还可能会让你添加webhook。点击add webhook，则进入github菜单，地址已有，只要点击Add webhook即可。  

附book.json代码：

    {
		"plugins": ["disqus"],
		"pluginsConfig": {
		  "disqus": {
		      "shortName": "picklecai"
		  }
		}
	}

DISQUS配置详见[DISQUS配置教程](DISQUS.md)。

## 使用

使用GitBook，可以完全在GitHub上操作：  
1. 在GitHub上更新章节内容。  
2. 在GitHub上更新SUMMARY.md的链接（文件均采用相对链接，在SUMMARY中出现的链接，需要注明文件所在文件夹）  
3. 在GitHub上更新章节首页的链接（同一个文件夹下的链接只要文件名即可），如果需要章节首页有链接的话。  

补充：如果内文链接中链接的文件，在SUMMARY中没有（SUMMARY链接写错了就等于没有），这个链接文件仍然可以打开，但是不带左边栏，是光秃秃的一个md页面。  

## 体验

