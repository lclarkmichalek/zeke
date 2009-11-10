#!/usr/bin/python
# -*- coding: utf-8 -*-

from tempfile import *
from zekemods import *

declareglobs()

cleanup = lambda s: s[:-1] if s[-1] == '\n' else s

#def writeass(s):
#    '''Writes a string to the association mapping files. Return true if succseeded. Syntax: writeass(string)'''
#    c = 0
#    res = 0
#    b = False
#    f = open('.//assindex.txt')
#    while not f.readline(c).split(',')[1] == '' and not b:
#        if s[0] == f.readline(c).split(',')[1]:
#            b = True
#        c =+ 1
#    if b == False:
#        res =+ 1
#    else:
#        while not f.readline(c).split(',')[1] == '' and not b:
#            if s[1] == f.readline(c).split(',')[1]:
#                b = True
#            c =+ 1

def writeindex(s):
	#WORKS. TESTED 02/09/09
	b = 0
	c = 0
	with open(GLOBALSTORAGE + 'assindex.txt') as f:
		a = f.readlines()
        while b == 0:
		#IF IT IS ALREADY FOUND
		if readnthline(a, c).split(',')[1] == s:
			b = 2
		#FIND FIRST BLANK LINE
		elif len(a) != c:
			b = 1
		c += 1
	if b == 2:
		return c
	with open(GLOBALSTORAGE + 'assindex.txt',  'a') as f:
		if a[-1][-2] == '\r\n':
			f.write(str(c) +  ',' +  s)
		elif a[-1][-2] != '\r\n':
			f.write('\n' + str(c + 1) +  ',' +  s)
	#RETURN INDEX NUMBER
	return c

def writeass(s, n):
	#WORKS. TESTED 02/09/09
	#Does not fucking work you twat 09/11/09
	ni = int(n)
	si = int(s)
	tf = TemporaryFile(mode='a+')
	f = openassdic('r')
	a = f.readlines()
	c = 0
	b = 0
	while b == 0:
		if int(readnthline(a, c).split(',')[0]) == s:
			b = 1
		elif readnthline(a, c).split(',')[0] == '':
			b = 2
		c += 1
	if b == 1:
		f.seek(0)
		strng = f.readlines()
		c1 = 0
		f.close
		#Everything before line n
		while c1 < ni:
			tf.write(strng[c1])
			c1 += 1
		#Insert line n, with added s
		tf.write(strng[c1].replace('\n',  '') + ',' + s + '\n')
		c1 += 1
		#Everything after line n
		while len(strng) != c1:
			tf.write(strng[c1])
			c1 += 1
		#Write the temp file to assdic.txt
		tf.seek(0)
		with open(GLOBALSTORAGE + 'assdic.txt',  'w') as f:
			f.write(tf.read())
		tf.close()
	elif b == 2:
		f.close()
		with open(GLOBALSTORAGE + 'assdic.txt',  'a') as f:
			f.write(s + ',' + n)
		tf.close
		tf = TemporaryFile(mode='a+')
		f = open(GLOBALSTORAGE + 'assdic.txt',  'r')
		a = f.readlines()
		c2 = -1
		b = 0
		while b <= 0:
			c2 += 1
			if int(readnthline(a, c2).split(',')[0]) == n:
				b = 1
			elif len(a) == c2:
				b = 2
	#Same as above, but for si
	if b == 1:
		f.seek(0)
		strng = f.readlines()
		c1 = 0
		f.close
		#Everything before line s
		while c1 < si:
			tf.write(strng[c1])
			c1 += 1
		#Insert line s, with added n
		tf.write(strng[c1].replace('\n',  '') + ',' + str(c2) + '\n')
		c1 += 1
		#Everything after line s
		while len(strng) != c1:
			tf.write(strng[c1])
			c1 += 1
		#Write the temp file to assdic.txt
		tf.seek(0)
		with open(GLOBALSTORAGE + 'assdic.txt',  'w') as f:
			f.write(tf.read())
		tf.close()
	elif b == 2:
		f.close()
		with open(GLOBALSTORAGE + 'assdic.txt',  'a') as f:
			f.write(n + ',' + s)
		tf.close


def checkass(intIndex1, intIndex2):
	
	strIndex1 = str(intIndex1)
	strIndex2 = str(intIndex2)
	
	fileDic = openassdic()
	listDicCont = fileDic.readlines()
	fileDic.seek(0)
	fileDic.close()
	
	listDicContClean = []
	for obCount in listDicCont:
		listDicContClean.append(obCount.split(','))
	listDicCont = []
	
	intCount1 = 0
	intCount2 = 0
	while len(listDicContClean) != intCount1:
		listDicCont.append([])
		while len(listDicContClean[intCount1]) != intCount2:
			listDicCont[intCount1].append(cleanup(listDicContClean[intCount1][intCount2]))
			intCount2 += 1
		intCount2 = 0
		intCount1 += 1
	
	bolResult1 = False
	if strIndex2 in listDicCont[intIndex1][1:]:
		bolResult1 = True
	
	bolResult2 = False
	if strIndex1 in listDicCont[intIndex2][1:]:
		bolResult2 = True
	
	if bolResult1 and bolResult2:
		return True
	else:
		return False


def getass(s, n):
	'''Checks if a string is already associted with another. Sytax: checkass(string1,string2)
	Return values:
	0 - strings are accosiated;
	1 - 1st string not found;
	2 - 2nd string not found;
	3 - strings found, but not accosiated;	
	4 - strings accosiated but there is database coruption.
	5 - both strings not found
	6 - one or more input = \"\"'''
	#WORKS. TESTED FOR ALL RETURN CODES APART FROM 4 01/09/09
	#APPARENTLY DOSN'T 08/11/09
	#Fix, 09/11/09. If either input = '' then return 3
	#What about when both strings not found? return 5? 09/11/09
	if '' in [s, n]:
		return 6
	s = ''
	r = 0
	b = False
	c = 0
	c2 = 0
	arevised = []
	f = open(GLOBALSTORAGE + 'assindex.txt')
	a = f.readlines()
	f.seek(0)
	for ent in a:
		arevised.append(cleanup(ent.split(',')))
	a = []
	while len(arevised) != c:
		a.append([])
		while len(arevised[c]) != c2:
			a[c].append(cleanup(arevised[c][c2]))
			c2 += 1
		c2 = 0
		c += 1
	c = 0
	while len(a) != c and not b:
		if s == a[c][1]:
			b = True
			d1 = int(a[c][0])
		c += 1
	if b == False:
		f.close
		bolFirst = False
        #Set false, s was not found, so we have some record, and can check for the second
	else:
		bolFirst = True
	c = 0
	b = False
	while not len(a) == c and not b:
		if n == a[c][1]:
			b = True
			d2 = int(a[c][0])
		c += 1
	f.close
	if False in (b, bolFirst):
		return 2
		#Was s found? no? then return 2
	elif not b and not bolFirst:
		return 5
		#otherwise, it's a general faliure, as indicated by returning 5
	f = open(GLOBALSTORAGE + 'assdic.txt')
	c = 0
	b = False
	a = f.readlines()
	for ent in a:
		cleanup(ent)
	list = readnthline(a, d1).split(',')
	if d2 in list:
		b = True
	if not b:
		r = 1
	c = 0
	b = False
	list = readnthline(a, d2).split(',')
	if d1 in list:
		b = True
	if not b:
		r += 1
	if r == 0:
		return 0
	elif r == 1:
		return 4
	elif r == 2:
		return 3

checkindex = lambda intstrInput: True if not getindex(intstrInput) else False

def getindex(s):
	'''Gets the index number of a string. If found return index number, else return False. Syntax: pollassindex(string)'''
	#WORKS. TESTED 01/09/09
	#Does not 09/11/09
	#Changed to take string or int input, and return string or int out. changed name to getindex from pollassindex 10/11/09
	if s == str(s):
		c = 0
		d = ''
		f = open(GLOBALSTORAGE + 'assindex.txt')
		a = f.readlines()
		while d == '':
			if len(a) != c and s == readnthline(a, c).split(',')[1]:
				d = c
			elif len(a) == c:
				d = False
			c += 1
		f.close()
		return d
	else:
		with open(GLOBALSTORAGE + 'assindex.txt') as f:
			a = f.readlines()
			d = []
			c = 0
			while d == []:
				if len(a) != c and s == int(readnthline(a, c).split(',')[0]):
					d = readnthline(a, c).split(',')[1]
				elif len(a) == c:
					d = False
				c += 1
		return d


def pollassindexrev(s):
    '''Gets the string for an index number. If index number is not found, return false. Syntax: pollassindexrev(int)'''
    #fixed, and marginly check 09/11/09
    with openassindex as f:
        a = f.readlines()
	d = 0
	c = 0
        while d == 0 and d != 3:
            if len(a) != c and s == int(readnthline(a, c).split(',')[0]):
                d = readnthline(a, c).split(',')[1]
            elif len(a) == c:
                d = 3
            c += 1
    return d

def pollassdic(s):
    '''Gets the associated index numbers for an index number. Syntax: pollassdic(index no)'''
    #WORKS
    f = open(GLOBALSTORAGE + 'assdic.txt')
    a = f.readlines()
    tmp = readnthline(a, s).split(',')[1:]
    f.close
    return tmp
    
    
#def pollassdic(s):
#    '''Get the index numbers of words associated with the input index number. Syntax: pollassdic(index number)'''
#    res = []
#    b = 1
#    if b == 1:
#        res1 = True
#        f = open('assdic.txt')
#        c = 0
#        tmp = f.readline(s).split(',')[0:]
#        f.close()
#        tmpf = open('assindex.txt')
#        for a in tmp:
#            res[c] = tmpf.readline(a).split(',')[1]
#            c =+ 1
#        tmpf.close()
#    elif b == 2 or b == 0:
#        res1 = False

def openassindex(*args):
	if 'w' in args:
		global globintIndexWriteCount
		globintIndexWriteCount += 1
	fileAssIndex = open(GLOBALSTORAGE + 'assindex.txt',  *args)
	global globintIndexOpenCount
	globintIndexOpenCount += 1
	return fileAssIndex

def openassdic(*args):
	if 'w' in args:
		global globintDicWriteCount
		globintDicWriteCount += 1
	fileAssDic = open(GLOBALSTORAGE + 'assdic.txt', *args)
	global globintDicOpenCount
	globintDicOpenCount += 1
	return fileAssDic


#SOME POINT USE PICKLE SEE ISSUE 8
def writedic(s,n):
    c = 0
    f = open(GLOBALSTORAGE + n + 'dic.txt')
    pre = f.read()
    f.close()
    pre = pre.split(' ')
    while c < len(s.keys()):
        if not s.keys()[c] in pre:
            f = open(n + 'dic.txt', 'a')
            f.write(' ' + s.keys()[c] + ' ' + s.values()[c])
            f.close()
        c += 1
    return

def getdic(s):
    dic = {}
    c = 0
    f = open(GLOBALSTORAGE + s + 'dic.txt')
    dicf = f.read()
    f.close()
    dicf = dicf.split(' ')
    while c < len(dicf):
        dic[dicf[c]] = dicf[c + 1]
        c += 2
    return dic

