import re
import json

def prep(x): #detects float, int, string
	regint = re.compile(r'^\d*$')
	regfloat = re.compile(r'^\d*\.\d*$')
	if regint.match(x):
		return int(x)
	if regfloat.match(x):
		return float(x)
	return x
	


class SuperDict(dict):
	def __init__(self, arg):
		Dictionary = {}
		if type(arg) == str:
			if len(arg) < 4:
				raise ValueError
			elif arg[-4:] == ".csv":
				FileInp = open(arg, "r")
				for current in FileInp.readlines():
					try: 
						a, b = map(prep, current.strip().split(","))
					except Exception:	
						raise ValueError
					Dictionary[a] = b
			elif len(arg) < 5:
				raise ValueError
			elif arg[-5:] == ".json":
				FileInp = open(arg, "r")
				json_str = FileInp.read()
				json_data = json.loads(json_str)
				try:
					Dictionary = json_data
				except Exception:
					raise ValueError
			else:
				raise ValueError
			self = Dictionary



		elif type(arg) == dict:
			Dictionary = arg
		else: raise TypeError 


print sd.Dictionary