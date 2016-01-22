# _*_ coding:utf-8 _*_

import os  
from os.path import join, getsize

def getdirsize(dir):
	size = 0.0
	for root, dirs, files in os.walk(dir):
		size += sum([getsize(join(root, name)) for name in files])
	return size

if __name__ == '__main__':
	filesize = getdirsize('c:\\windwos')
	print 'There are %.3f' % (filesize/1024/1024), 'Mbytes in c:\\windwos'