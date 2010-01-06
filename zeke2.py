#!/bin/python

import anydbm

db = anydbm.open('/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/words', 'c')

class word(str):
	def __init__(self, word):
		#for iters
		self.place = 0
		
		self.word = word
		#asses = list of words
		self.asses = []
	
	def __add__(self, other):
		self.asses.append(other.word)
		other.asses.append(self.word)
	
#	def __setattr__(self, attr, value):
#		raise Forbidden(attr)
	
	def __str__(self):
		return self.word
	
	def __getitem__(self, index):
		return self.asses[index]
	
	def __iter__(self):
		return self
	
	def next(self):
		if self.place == len(self.asses) - 1:
			raise StopIteration
		self.place += 1
		return self.asses[self.place]
	
	def addass(self, other):
		self.asses.append(other)


class OwnErrors(Exception): pass

class WordErrors(OwnErrors): pass

class Forbidden(WordErrors): 
	def __init__(self, attr):
		print 'Please don\'t set %s manualy.' % attr

if __name__ == '__main__':
	pass
