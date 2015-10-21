# _*_ coding:utf-8 _*_

from os.path import exists
import time

def main():
	# 打印之前所有的内容
	if exists("tempfile.txt"):
		print '''
历史记录：
-------------------------------------------'''
		txt = open("tempfile.txt")
		notelist = txt.readlines()
		txt.close()
		for i in notelist:
			print(i)
		print "-------------------------------------------"

	# 输入新的内容
	txt = open("tempfile.txt", 'a')
	newline = raw_input("今日记录，请输入： ")
	txt.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n"))
	txt.write(newline)
	txt.write("\n"+"\n")
	txt.close()

	# 新内容另存为文件
	filename = raw_input("存储今日记录，请输入文件名：")
	output = open(filename + ".txt", 'w')
	output.write(filename + ".txt"+"\n")
	output.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n"))
	output.write(newline)
	output = open(filename + ".txt")
	output.close

if __name__ == '__main__':
	main()
