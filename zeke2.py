#!/bin/python

import anydbm

global db
db = anydbm.open('/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/words', 'c')

class word(object):
	def __init__(self, word=None):
		#for iters
		self.place = -1
		
		self.word = word
		#asses = list of words
		self.asses = []
	
	def __add__(self, other):
		if other.word in self.asses:
			return None
		self.asses.append(other.word)
		other.asses.append(self.word)
	
#	def __setattr__(self, attr, value):
#		raise Forbidden(attr)
	
	def __eq__(self, other):
		if not self.word.lower() == other.word.lower():
			return False
		else: return True
	
	def __str__(self):
		return self.word
	
	def __getitem__(self, index):
		return self.asses[index]
	
	def __iter__(self):
		return self
	
	def next(self):
		if self.place == len(self.asses) - 1:
			self.place = -1
			raise StopIteration
		self.place += 1
		return self.asses[self.place]
	
	def settype(self, type):
		if not self.type:
			raise TypeDefined(self.name, self.type)
		self.type = type
		type.words.append(self.name)
	
	def setstatus(self, status):
		if not self.status:
			raise StatusDefined(self.name, self.type)
		self.status = status
		status.words.append(self.name)
	
	def setuse(self, use):
		if not self.use:
			raise UseDefined(self.name, self.type)
		self.use = use
		use.words.append(self.name)
	
#	It would be LOVELY if this worked :(
#	def __del__(self):
#		db[self.name] = self


class type(object):
	def __init__(self, type=None):
		self.type = type
		
		self.place = -1
		
		self.words = []
	
	def __add__(self, other):
		if other.type:
			raise TypeDefined(other.name, other.type)
		else:
			self.words.append(other.name)
			other.type = self.type
	
	def __floordiv__(self, other):
		if type(other) == type(status()):
			ret = []
			for x in words:
				#get the word from db, we only have name. so aslong as they're stored by name, it'll be cool
				x = db[x]
				if x.status == other: ret.append(x.name)
				del x
			return ret
		
		if type(other) == type(use()):
			ret = []
			for x in words:
				#get the word from db, we only have name. so aslong as they're stored by name, it'll be cool
				x = db[x]
				if x.use == other: ret.append(x.name)
				del x
			return ret
	
	def __str__(self):
		return self.type
	
	def __getitem__(self, index):
		return self.type[index]
	
	def __iter__(self):
		return self
	
	def next(self):
		if self.place == len(self.words) - 1:
			self.place = -1
			raise StopIteration
		self.place += 1
		return self.asses[self.place]

class use(object): pass

class OwnErrors(Exception): pass

class WordErrors(OwnErrors): pass

class DefenitionError(WordErrors):
	def __init__(self):
		print 'Variable already set'

class TypeDefined(DefenitionError):
	def __init__(self, word, type):
		print '%s already has type: %s' % (word, type)

class StatusDefined(DefenitionError):
	def __init__(self, word, status):
		print '%s already has status: %s' % (word, status)

class UseDefined(DefenitionError):
	def __init__(self, word, use):
		print '%s already has use: %s' % (word, use)

class Forbidden(WordErrors): 
	def __init__(self, attr):
		print 'Please don\'t set %s manualy.' % attr

if __name__ == '__main__':
	pass