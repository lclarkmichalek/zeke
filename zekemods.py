#!/usr/bin/env python
# -*- coding: utf-8 -*-

cleanup = lambda s: s[:-1] if s[-1] == '\n' else s

def readnthline(s, n):
	c = 0
	while c != len(s):
		#-1 because \n is one character
		if s[c][-1:] == '\n':
			s[c] = s[c][:-1]
		c += 1
	c = 0
	while c != len(s) and s[c][-2:] == '\r\n': 
		s[c] = s[c].replace('\r\n', '')
		c += 1
	res = s[n]
	return res

def declareglobs():
    #GLOBAL INSTALL BINARY PATH
    global GLOBALBIN
    GLOBALBIN = '/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/zeke.py'

    #GLOBAL INSTALL LIB PATH
    global GLOBALLIB
    GLOBALLIB = '/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/'

    #GLOBAL INSTALL STORAGE PATH
    global GLOBALSTORAGE
    GLOBALSTORAGE = '/home/laurie/PersonalMedia/Code/Python/Zeke/Maintrunk/'
    
    #No need to change these
    global globintDicOpenCount
    globintDicOpenCount = 0
    
    global globintAssOpenCount
    globintAssOpenCount = 0
    
    global globintDicWriteCount
    globintDicWriteCount = 0
    
    global globintAssWriteCount
    globintAssWriteCount = 0
    
    
def firstwords(s, n):
    '''
    Get's the first words of a string. Syntax: firstwords(string, number of words)
    '''
    lw = s.split(' ')[:n]
    return lw

def vardef(s):
    '''
    Tests if a variable is defined. If it is, return True, else return False. Syntax: vardef(variable)
    '''
    RES=True
    try:
        s
    except NameError:
        RES=False
    return RES

def lastwords(s, n):
    '''
    Get's the last words of a string. Syntax: lastwords(string, number of words)
    '''
    rec1l = s.split(' ')
    lw = rec1l[-n:]
    return lw

def rmpunc(s):
    '''
    Removes punctuation from a string. Syntax: rmpunc(string)
    '''
    l = c = 0
    punc = ['?', '!', '.' ,',']
    while c != 1:
        l += 1
        if s[-1] in punc:
	    s = s[:-1]
        else:
            c = 1
	return [s, l]

def lastletter(s):
    '''Tests if last letter is vowel. If it is, return True. Syntax: lastletter(string)'''
    vowel = ['a', 'e', 'i', 'o', 'u', 'y']
    if s[-1] in vowel:
		o = True
    else:
        o = False
    return o
