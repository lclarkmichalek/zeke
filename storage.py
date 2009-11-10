#!/usr/bin/python
# -*- coding: utf-8 -*-

from tempfile import *
from zekemods import *

declareglobs()

cleanup = lambda s: s[:-1] if s[-1] == '\n' else s


def writeindex(strIndex):
	
	fileIndex = openassindex('a+')
	listIndexCont = fileIndex.readlines()
	intLastLine = len(listIndexCont)
	
	if listIndexCont[-1][-1] in ('\r', '\n'):
		fileIndex.write(str(intLastLine) + ',' + strIndex)
	else:
		fileIndex.write('\n' + str(intLastLine) + ',' + strIndex)
	
	fileIndex.seek(0)
	fileIndex.close()


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


def getass(intIndex):
	#Re-writen to be simpler, and nicer. 10/11/09
	
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
	
	try:
		listReturn = listDicCont[intIndex][1:]
	except:
		listReturn = False
	else:
		listReturn = listDicCont[intIndex][1:]
	return listReturn


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
	if 'w' in args or 'a' in args:
		global globintIndexWriteCount
		globintIndexWriteCount += 1
	fileAssIndex = open(GLOBALSTORAGE + 'assindex.txt',  *args)
	global globintIndexOpenCount
	globintIndexOpenCount += 1
	return fileAssIndex

def openassdic(*args):
	if 'w' in args or 'a' in args:
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

