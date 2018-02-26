import os


def dfs(direct, delta = 0):
	lst = os.listdir(direct)
	print "    " * delta + os.path.basename(direct) + ":"
	for i in lst:
		if os.path.isdir(direct + '/' + i):
			dfs(direct + "/" + i, delta + 1)
		else:
			print "    " * (delta+1) + i

dfs("..")