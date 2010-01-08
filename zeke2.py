#!/bin/python

import shelve
from random import randint

global words
words = shelve.open('/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/words.slv')

global types
types = shelve.open('/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/types.slv')

global uses
uses = shelve.open('/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/uses.slv')

global statuses
statuses = shelve.open('/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/statuses.slv')

#Some other thingys that I want to keep
global persistence
persistence = shelve.open('/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/persistence.slv')

#########################################
#          CLASSES                      #
#########################################

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
	
	def __len__(self):
		return len(self.wordss)
	
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
		

class Word(Super):
	
	type = None
	use = None
	status = None
	
	def __add__(self, other):
		#May seem big, but only need one, words are special
		if type(other) == type(Word()):
			if other.data in self.words:
				return None
			self.words.append(other.data)
			other.words.append(self.data)
		elif type(other) == type(Type()):
			if self.type:
				raise TypeDefined(self.data, self.type)
			else:
				other.words.append(self.data)
				self.type = other.data
		elif type(other) == type(Use()):
			if self.use:
				raise UseDefined(self.data, self.use)
			else:
				other.words.append(self.data)
				self.use = other.data
		elif type(other) == type(Status()):
			if self.status:
				raise StatusDefined(self.status, self.data)
			else:
				other.words.append(self.data)
				self.status = other.data


class Type(Super):
	def __div__(self, other):
		a = self._StatusDiv(other)
		if not a:
			a = self._UseDiv(other)
		return a

class Use(Super):
	def __div__(self, other):
		self._UseDiv(other)

class Status(Super):
	def __init__(self, data=None, start=5, end=5):
		Super.__init__(self, data)
		
		self.range = range(start, end + 1)

#########################################
#            FUNCTIONS                  #
#########################################

def getword(status, type, use):
	ret = []
	for word in use:
		word = db[word]
		if word.type == type:
			status1 = db[word.status]
			if status in status1.range:
				ret.append(word)
	#If they get this far, skip status bit
	if not ret:
		for word in use:
			word = db[word]
			if word.type == type:
				ret.append(word)
	#Now choose a random word
	return ret[randint(0,len(ret) - 1)]

def exist(word):
	'''See if the word exists. Return True or False'''
	try:
		words[word]
	except KeyError:
		return False
	else:
		return True

def findstatus(number):
	'''Find statuses that have number in their range'''
	ret = []
	for status in statuses:
		if number in status.range:
			ret.append(status.data)
	return ret

#########################################
#          EXCEPTIONS                   #
#########################################

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
	print getword(statuses[persistence[status]], types[greeting], uses[greeting])
	input = raw_input()
	#Use whole input, not input.split(), because a relpy to greeting is useualy greeting phrase/word
	if exist(input):
		a = words[input] + types[greeting]
		a = words[input] + uses[greeting] 
		if persistence[status] < 5:
			a = findstatus(persistence[status])
			a = words[input] + statuses[a[randint(0, len(a) - 1)]]
		else:
			#Inverse. example, butler: Good morning sir
			#Person: Morning Jeeves
			#Buter: Formal, Person: Informal
			a = findstatus(10 - persistence[status])
			a = words[input] + statuses[a[randint(0, len(a) - 1)]]