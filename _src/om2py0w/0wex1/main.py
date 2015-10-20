# _*_ coding:utf-8_*_

txt = open("tempfile.txt")
notelist = txt.readlines()
txt.close()
for i in notelist:
	print(i)
txt = open("tempfile.txt", 'a')
newline = raw_input(">")
txt.write(newline)
txt.write("\n")
txt.close()
