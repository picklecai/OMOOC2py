# _*_ coding:utf-8 _*_

from os.path import exists
import time

def main():
	# 打印之前所有的内容
	if exists("tempfile.txt"):   #如果tempfile不存在，说明程序是第一次运行，没有历史内容可打印。
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
	txt.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n")) #在保存当前输入的同时，也保存当前时间。
	txt.write(newline)
	txt.write("\n"+"\n")
	txt.close()

	# 新内容另存为文件
	filename = raw_input("存储今日记录，请输入文件名：")
	output = open(filename + ".txt", 'w') #规定好扩展名，以免出现用户保存的文件打不开的情况。
	output.write(filename + ".txt"+"\n") #在文件中写入文件名。
	output.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n")) #在文件中写入当前时间。
	output.write(newline)
	output = open(filename + ".txt")
	output.close

if __name__ == '__main__':
	main()
