# _*_ coding:utf-8 _*_

from os.path import exists

# 打印之前所有的内容
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

# 输入新的内容
txt = open("tempfile.txt", 'a')
newline = raw_input("请给记事本输入新内容： ")
txt.write(newline)
txt.write("\n")
txt.close()

# 新内容另存为文件
filename = raw_input("新内容的文件名是：")
output = open(filename + ".txt", 'w')
output.write(newline)
output = open(filename + ".txt")
output.close
