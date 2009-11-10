#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import *
from zekemods import *
declareglobs()
from storage import *
from sys import *
path = [GLOBALLIB] + path

#Debug area


c = 0
c1 = 0
t = 0
v1 = 0
v2 = 0
a = ''
ass1 = ''
ass2 = ''
wdtype = getdic('wdtype')
wdtypen = 'noun'				
wdtypep = 'pronoun'
wdtypea = 'adjective'
wdtypev = 'verb'
queswds = ['who', 'how', 'why', 'where', 'when', 'what', 'which']
cleanup = lambda s: s[:-1] if s[-1] == '\n' else s
while c1 < 20:
	a = raw_input('I am thinking of an object. Ask me a yes/no question about itw. ')
	if a == '':
		exit('Next time, enter something')
	a = rmpunc(a)[0]
	if a == 'stop' or a == 'Stop':
		writedic(wdtype,'wdtype')
		exit()
	elif a == 'wdtype':
		print wdtype
	elif a == 'ass':
		#broke this, 10/11/09
		c2 = 0
		asses = []
		tm = raw_input('What word would you like the acociations for? ')
		tmout = pollassdic(pollassindex(tm))
		tmoutnew = []
        	for ent in tmout:
			asses.append(pollassindexrev(int(cleanup(str(ent)))))
		print '%s is asociated with:' % tm
		for ent in asses:
			print ent
	elif len(a.split(' ')) < 3:
		exit('A question you numscull')
	elif lastletter(a) and ass1 == '':
		ass1 = lastwords(a, 1)[0]
	elif not lastletter(a) and ass1 != '':
		ass2 = lastwords(a, 1)[0]
	if not '' in (ass1, ass2) and checkass(ass1, ass2) in [1, 2, 3, 5]:
        #If one or more is found not to exist, or they aint accosiated, do it through the ubiquotus writeassindex func
		writeassdic(writeassindex(ass1), writeassindex(ass2))
		ass1, ass2 = '', ''
	if not lastwords(a, 1)[0] in wdtype:
		if lastwords(a, 2)[0] in ['a', 'an']:
			wdtype[lastwords(a, 1)[0]] = wdtypen
		else:
			wdtype[lastwords(a, 1)[0]] = wdtypea
	if not firstwords(a, 2)[1] in wdtype:
		wdtype[firstwords(a, 2)[1]] = wdtypep
	#Actualy respond
	if lastletter(a):
		print 'Yes'
	else:
		print 'No'
	c1 += 1


writedic(wdtype,'wdtype')

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
