import os


def dfs(direct, delta = 0):
	lst = os.listdir(direct)
	print "    " * delta + os.path.basename(direct) + ":"
	for i in lst:
		try:
			dfs(direct + "/" + i, delta + 1)
		except Exception:
			print "    " * delta + i

dfs(".")