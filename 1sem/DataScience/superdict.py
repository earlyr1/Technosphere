import re
import json
import random

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
		self.Dictionary = {}
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
					self.Dictionary[a] = b
			elif len(arg) < 5:
				raise ValueError
			elif arg[-5:] == ".json":
				FileInp = open(arg, "r")
				json_str = FileInp.read()
				json_data = json.loads(json_str)
				try:
					self.Dictionary = json_data
				except Exception:
					raise ValueError
			else:
				raise ValueError

		elif type(arg) == dict:
			self.Dictionary = arg
		else: 
			raise TypeError 

	def __getitem__(self, arg):
		try:
			return self.Dictionary[arg]
		except Exception:
			raise KeyError

	def __add__(self, other):
		res = self.Dictionary.copy()
		res.update(other.Dictionary)
		return SuperDict(res)

	def __repr__(self):
		return self.Dictionary.__repr__()

	def clear(self):
		self.Dictionary.clear()

	def items(self):
		return self.Dictionary.items()

	def keys(self):
		return self.Dictionary.keys()

	def values(self):
		return self.Dictionary.values()

	def iteritems(self):
		return self.Dictionary.iteritems()

	def iterkeys(self):
		return self.Dictionary.iterkeys()

	def itervalues(self):
		return self.Dictionary.itervalues()

	def __iter__(self):
		return self.Dictionary.__iter__()

	def get_random_key(self):
		return random.choice(self.Dictionary.keys())

	def to_csv(self, filename):
		pass

	def to_json(self, filename):
		pass

	def __len__(self):
		return len(self.Dictionary)

	def __eq__(self, other):
		return self.Dictionary == other.Dictionary

	def get_key_starts_from(self, pattern):
		if type(pattern) != str:
			raise TypeError
		res = ()
		for i in self.keys():
			if type(i) == str and i.startswith(pattern):
				res += (i,)
		return res

	def max_key_len(self):
		ans = -1
		for i in self.keys():
			if type(i) == str:
				if len(i) > ans:
					ans = len(i)
		if ans == -1:
			raise IndexError
		return ans

