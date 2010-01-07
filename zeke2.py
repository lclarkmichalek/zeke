#!/bin/python

import anydbm

global db
db = anydbm.open('/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/words', 'c')

class Super(object):
	def __init__(self, data=None):
		self.data = data
		
		self.place = -1
		
		self.words = []
	
	def __eq__(self, other):
		if not self.data.lower() == other.data.lower():
			return False
		else: return True
	
	def __repr__(self):
		return self.data
	
	def __getitem__(self, index):
		return self.words[index]
	
	def __iter__(self):
		return self
	
	def next(self):
		if self.place == len(self.words) - 1:
			self.place = -1
			raise StopIteration
		self.place += 1
		return self.words[self.place]
	
	def _StatusDiv(self, other):
		if type(other) == type(Status()):
			ret = []
			for x in words:
				#get the word from db, we only have name. so aslong as they're stored by name, it'll be cool
				x = db[x]
				if x.status == other: ret.append(x.data)
				del x
			return ret
	def _UseDiv(self, other):
		if type(other) == type(Use()):
			ret = []
			for x in words:
				#get the word from db, we only have name. so aslong as they're stored by name, it'll be cool
				x = db[x]
				if x.use == other: ret.append(x.data)
				del x
			return ret
	def _TypeDiv(self, other): pass
		

class Word(Super):
	def __init__(self, word=None):
		#for iters
		self.place = -1
		
		self.data = word
		
		#asses = list of words
		self.asses = []
	
	def __add__(self, other):
		if type(other) == type(Word()):
			if other.data in self.asses:
				return None
			self.asses.append(other.data)
			other.asses.append(self.data)
		elif type(other) == type(Type()):
			if other.type:
				raise TypeDefined(other.data, other.type)
			else:
				self.words.append(other.data)
				other.type = self.type
		elif type(other) == type(Use()):
			if other.use:
				raise UseDefined(other.data, other.use)
			else:
				self.words.append(other.data)
				other.use = self.use
		elif type(other) == type(Status()):
			if other.data:
				raise StatusDefined(other.data, other.data)
			else:
				self.words.append(other.data)
				other.data = self.use


class Type(Super):
	def __div__(self, other):
		a = Super._StatusDiv(self, other)
		if not a:
			a = Super._UseDiv(self, other)
		return a

class Use(Super): pass

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