import random

class Suggest():
	lst=list()
	def randomize(self,lst):
		try:
			return random.choice(lst)
		except:
			return None