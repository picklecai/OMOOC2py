# _*_ coding:utf-8 _*_

from os.path import exists
from sys import exit
import time

def main():
	print '''
请输入你的选择：
1 打印之前的历史记录
2 输入新的内容
3 退出程序 '''
	prompt = '>'
	choose = raw_input(prompt)

	if choose =="1" :
		printhistory()
		main()
	elif choose =="2" :
		writenew()
		main()
	elif choose =="3" :
		exit(0)
	else:
		print "对不起，我不知道你想要的是什么。"
		main()

def printhistory():
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
	else:
		print "对不起，程序第一次运行，尚无历史记录可打印。你可以选择2开始输入新内容。"
		main()

def writenew():
	# 输入新的内容
	txt = open("tempfile.txt", 'a')
	newline = raw_input("今日记录，请输入： ")
	txt.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n")) #在保存当前输入的同时，也保存当前时间。
	txt.write(newline)
	txt.write("\n"+"\n")
	txt.close()

	def savenew():
		print '''
你是否想把新输入内容存为独立文件？ 
1 好的，存为独立文件。 
2 不想，只是随便写写。	'''
		prompt = '>'
		choose = raw_input(prompt)

		if choose =="1" :
			filename = raw_input("存储今日记录，请输入文件名：")
			output = open(filename + ".txt", 'w') #规定好扩展名，以免出现用户保存的文件打不开的情况。
			output.write(filename + ".txt"+"\n") #在文件中写入文件名。
			output.write(time.strftime("%d/%m/%Y %H:%M:%S"+"\n")) #在文件中写入当前时间。
			output.write(newline)
			output = open(filename + ".txt")
			output.close
			main()
		elif choose =="2" :
			main()
		else:
			print "对不起，我不知道你想要干什么。请重新选择是否要存盘。"
			savenew()

	# 新内容另存为文件
	savenew()

if __name__ == '__main__':
	main()
