#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import *
from zekemods import *
declareglobs()
from storage import *
from sys import *
path = [GLOBALLIB] + path

#Debug area
#a = writeass(8, 9)
#print a

c = 0
c1 = 0
ass1 = ''
ass2 = ''
wdtype = getwdtype()
wdNoun = 'noun'				
wdPro = 'pronoun'
wdAdj = 'adjective'
wdVer = 'verb'
wdNam = 'name'
queswds = ['who', 'how', 'why', 'where', 'when', 'what', 'which']
cleanup = lambda s: s[:-1] if s[-1] == '\n' else s

listKeywords = ['ass', 'wdtype',  'edit']

while c1 < 20:
	a = raw_input('I am thinking of an object. Ask me a yes/no question about it. ')
	if a == '':
		exit('Next time, enter something')
		
	a = rmpunc(a)[0]
	
	if a == 'stop' or a == 'Stop':
		writewdtype(wdtype)
		exit()
		
	elif a == 'wdtype':
		print wdtype
		
	elif a == 'ass':
		c2 = 0
		asses = []
		tm = raw_input('What word would you like the acociations for? ')
		tmindex = getindex(tm)
		if str(tmindex) == 'False':
			print '%s is not associated with anything' % tm
		else:
			tmasses = getass(tmindex)
			print '%s is assosiated with:' % tm
			for x in tmasses:
				print getindex(x)
				
	elif a == 'edit':
		strEditChoice = raw_input('What would you like to edit? Word types, or Word associations? ')
		
		if 'types' in strEditChoice:
			strWichEntryChoice = raw_input('Currently, the word type collection is %len entrys. Would you like to search them, or list them? ' % int(len(wdtype)))
			
			if 'search' in strWichEntryChoice:
				strSearchChoice = raw_input('Enter the word you would like to search for ')
				try:
					wdtype[strSearchChoice]
				except NameError and KeyError:
					print 'That is not a recorded word'
				else:
					strNewValue = raw_input('%s currently is %s. What would you like it to be (noun,pronoun,adjective,verb or name) ' % (strSearchChoice, wdtype[strSearchChoice]))
					if strNewValue in [wdNoun, wdPro, wdAdj, wdVer, wdNam]:
						wdtype[strEditChoice] = wdNam
						print '%s now is %s.' % (strSearchChoice, strNewValue)
				
			elif 'list' in strWichEntryChoice:
				intCount = 0
				listKeys = wdtype.keys()
				listValues = wdtype.values()
				while intCount != len(wdtype):
					print listKeys[intCount] + (' ' * (30 - len(listKeys[intCount]) + 1)) + listValues[intCount]
					intCount += 1
				strEditChoice = raw_input('What word has the incorrect type at the moment? ')
				try:
					wdtype[strEditChoice]
				except NameError and KeyError:
					print 'That is not a recorded word'
				else:
					strNewValue = raw_input('%s currently is %s. What would you like it to be (noun,pronoun,adjective,verb or name) ' % (strEditChoice, wdtype[strEditChoice]))
					if strNewValue in [wdNoun, wdPro, wdAdj, wdVer, wdNam]:
						wdtype[strEditChoice] = wdNam
						print '%s now is %s.' % (strEditChoice, strNewValue)
						
		elif 'associations' in strEditChoice:
			print 'Dont think this works ATM'
			
			strEditChoice = raw_input('Enter your search query ')
			tmindex = getindex(strEditChoice)
			if str(tmindex) == 'False':
				print '%s is not found' % strEditChoice
			else:
				tmasses = getass(tmindex)
				print '%s is assosiated with:' % strEditChoice
				for x in tmasses:
					print getindex(x)
				strNewAss = raw_input('What would you like to add its association with? ')
				if not getass(strNewAss):
					writeindex(strNewAss)
				writeass(getindex(strNewAss), tmindex)
				print 'Done'
	elif len(a.split(' ')) < 3:
		exit('A question you numscull')
		
	elif lastletter(a) and ass1 == '':
		ass1 = lastwords(a, 1)[0]
		
	elif not lastletter(a) and ass1 != '':
		ass2 = lastwords(a, 1)[0]
		
	if not '' in (ass1, ass2):
		if checkindex(ass1) and checkindex(ass2):
			
			if not checkass(getindex(ass1), getindex(ass2)):
				writeass(getindex(ass1), getindex(ass2))
			
		elif not checkindex(ass1) and not checkindex(ass2):
			
			writeindex(ass1)
			writeindex(ass2)
			
			if not checkass(getindex(ass1), getindex(ass2)):
				writeass(getindex(ass1), getindex(ass2))
				
		elif not checkindex(ass1):
			
			writeindex(ass1)
			
			if not checkass(getindex(ass1), getindex(ass2)):
				writeass(getindex(ass1), getindex(ass2))
			
		elif not checkindex(ass2):
			
			writeindex(ass2)
			
			if not checkass(getindex(ass1), getindex(ass2)):
				writeass(getindex(ass1), getindex(ass2))
		
		ass1, ass2 = '', ''
		
	if not a in listKeywords and not lastwords(a, 1)[0] in wdtype:
		
		if lastwords(a, 2)[0] in ['a', 'an']:
			wdtype[lastwords(a, 1)[0]] = wdNoun
			
		else:
			wdtype[lastwords(a, 1)[0]] = wdAdj
			
	if not a in listKeywords and not firstwords(a, 2)[1] in wdtype:
		
		if firstwords(a, 2)[1][0].isupper():
			wdtype[firstwords(a, 2)[1]] = wdNam
			i
		else:
			wdtype[firstwords(a, 2)[1]] = wdPro
			
	#Actualy respond
	if not a in listKeywords and lastletter(a) :
		print 'Yes'
		
	elif not a in listKeywords:
		print 'No'
	c1 += 1


writewdtype(wdtype)

while True:
	a = raw_input('Ok, I\'m sorry, there was no object. I\' still learning about the world. Can you help me? ')
	a = rmpunc(a)[0]
	if a != 'no':
		print 'I\'ll take that as a yes'
		break
	else:
		exit('Ok then')

        
while True:
	a = raw_input('Tell me something, and I will try and respond. ')
	a = rmpunc(a)[0]
	if firstwords(a, 1)[0] in queswds:
		exit('Trechery on all frontiers, I asked for a statment')
	elif wdtype[firstwords(a, 1)[1]] == wdtypep:
		tmpvar = raw_imput('Is ' + firstwords(a, 1)[1] + ' the variable? ')
		if tmpvar == 'yes':
			wdtype[firstwords(a, 1)][1] = wdtypep
	if lastwords(a, 1)[0] in wdtype or lastwords(a, 1)[0] in ass:
		q = queswds[randrange(0, len(queswds))]
		if wdtype[lastwords(a, 1)[0]] == wdtypea:
			wdtype[firstwords(a, 1)[1]] = wdtypev
        elif wdtype[firstword(a, 2)[1]] == wdtypen:
            if not firstword(a, 0)[0] in wdtype:
                wdtype[firstword(a, 0)[0]] = wdtypep
            if not firstword(a, 2)[1] in wdtype:
                wdtype[firstword(a, 2)[1]] = wdtypev
                
	
	
	
	
	else:
		print 'I\' sorry, I havn\' a clue'
