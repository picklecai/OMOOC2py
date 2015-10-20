# _*_ coding:utf-8 _*_

from os.path import exists

if exists("tempfile.txt"):
	print '''
记事本现在的内容是：
-------------------------------------------'''
	txt = open("tempfile.txt")
	notelist = txt.readlines()
	txt.close()
	for i in notelist:
		print(i)
	print "-------------------------------------------"

txt = open("tempfile.txt", 'a')
newline = raw_input("请给记事本输入新内容： ")
txt.write(newline)
txt.write("\n")
txt.close()
