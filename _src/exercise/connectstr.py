def buildconnectstr(string):
	"""This is a programme to connect two strings in a dictionary."""
	result = ";".join(["%s=%s" %(k,v) for k, v in string.items()])
	return result

if __name__ == "__main__":
	mystring = {"xiaoming":"165", \
	"baoyu":"180", \
	"xiangyun":"165", "daiyu":"155"}
	print buildconnectstr(mystring)