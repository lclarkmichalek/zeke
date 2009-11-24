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
	
	return intLastLine


def writeass(intIndex1, intIndex2):
	
	if intIndex1 < intIndex2:
		tmp = intIndex2
		intIndex2 = intIndex1
		intIndex2 = tmp
	
	tempfileFakeDic = TemporaryFile(mode='a+')
	
	
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
	
	
	if len(listDicCont) - 1 < intIndex1:
		bolIndex1PreExist = False
	else:
		bolIndex1PreExist = True
	
	if len(listDicCont) - 1 < intIndex2:
		bolIndex2PreExist = False
	else:
		bolIndex2PreExist = True
	
	if bolIndex1PreExist and bolIndex2PreExist:
		
		intCount1 = 0
		while intCount1 < intIndex1:
			
			strLineCont = ''
			for x in listDicCont[intCount1]:
				strLineCont = strLineCont + str(x) + ','
			#Get rid of trailing comma
			strLineCont = strLineCont[:-1] + '\n'
			
			tempfileFakeDic.write(strLineCont)
			
			intCount1 += 1
		
		strLineCont = ''
		for x in listDicCont[intCount1]:
			strLineCont = strLineCont + str(x) + ','
		strLineCont = strLineCont[:-1]
		
		tempfileFakeDic.write(strLineCont + ',' + str(intIndex2) + '\n')
		
		intCount1 += 1
		
		while intCount1 < intIndex2:
			
			strLineCont = ''
			for x in listDicCont[intCount1]:
				strLineCont = strLineCont + str(x) + ','
			strLineCont = strLineCont[:-1] + '\n'
			
			tempfileFakeDic.write(strLineCont)
			
			intCount1 += 1
		
		
		strLineCont = ''
		for x in listDicCont[intCount1]:
			strLineCont = strLineCont + str(x) + ','
		strLineCont = strLineCont[:-1]
		
		tempfileFakeDic.write(strLineCont + ',' + str(intIndex1) + '\n')
		
		intCount1 += 1
		
		while intCount1 < len(listDicCont):
			
			strLineCont = ''
			for x in listDicCont[intCount1]:
				strLineCont = strLineCont + str(x) + ','
			strLineCont = strLineCont[:-1] + '\n'
			
			tempfileFakeDic.write(strLineCont)
			
			intCount1 += 1
		
		tempfileFakeDic.seek(0)
		with openassdic('w') as fileDic:
			fileDic.write(tempfileFakeDic.read())
		tempfileFakeDic.seek(0)
		tempfileFakeDic.close()
		
		return True
		
	elif bolIndex2PreExist:
		
		intCount1 = 0
		while intCount1 < intIndex1:
			
			strLineCont = ''
			for x in listDicCont[intCount1]:
				strLineCont = strLineCont + str(x) + ','
			#Get rid of trailing comma
			strLineCont = strLineCont[:-1] + '\n'
			
			tempfileFakeDic.write(strLineCont)
			
			intCount1 += 1
		
		strLineCont = ''
		for x in listDicCont[intCount1]:
			strLineCont = strLineCont + str(x) + ','
		strLineCont = strLineCont[:-1]
		
		tempfileFakeDic.write(strLineCont + ',' + str(intIndex2) + '\n')
		
		intCount1 += 1
		
		while intCount1 < len(listDicCont):
			
			strLineCont = ''
			for x in listDicCont[intCount1]:
				strLineCont = strLineCont + str(x) + ','
			strLineCont = strLineCont[:-1] + '\n'
			
			tempfileFakeDic.write(strLineCont)
			
			intCount1 += 1
		
		tempfileFakeDic.write(str(intIndex2) + ',' + str(intIndex1) + '\n')
		
		tempfileFakeDic.seek(0)
		with openassdic('w') as fileDic:
			fileDic.write(tempfileFakeDic.read())
		tempfileFakeDic.seek(0)
		tempfileFakeDic.close()
		
		return True
		
	elif not bolIndex1PreExist and not bolIndex2PreExist:
		
		intCount1 = 0
		
		while intCount1 < len(listDicCont):
			
			strLineCont = ''
			for x in listDicCont[intCount1]:
				strLineCont = strLineCont + str(x) + ','
			strLineCont = strLineCont[:-1] + '\n'
			
			tempfileFakeDic.write(strLineCont)
			
			intCount1 += 1
		
		tempfileFakeDic.write(str(intIndex1) + ',' + str(intIndex2) + '\n')
		tempfileFakeDic.write(str(intIndex2) + ',' + str(intIndex1) + '\n')
		
		tempfileFakeDic.seek(0)
		with openassdic('w') as fileDic:
			fileDic.write(tempfileFakeDic.read())
		tempfileFakeDic.seek(0)
		tempfileFakeDic.close()
		
		return True


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
	try:
		strIndex2 in listDicCont[intIndex1][1:]
	except IndexError:
		return False
	else:
		bolResult1 = True
	
	bolResult2 = False
	try:
		strIndex1 in listDicCont[intIndex2][1:]
	except IndexError:
		return False
	else:
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
	
	listintReturn = []
	for x in listReturn:
		listintReturn.append(int(x))
	
	return listintReturn


checkindex = lambda intstrInput: True if type(getindex(intstrInput)) != type(True) else False

def getindex(unkInput):
	
	fileIndex = openassindex()
	listIndexCont = fileIndex.readlines()
	fileIndex.seek(0)
	fileIndex.close()
	
	listIndexContClean = []
	for obCount in listIndexCont:
		listIndexContClean.append(obCount.split(','))
	listIndexCont = []
	
	intCount1 = 0
	intCount2 = 0
	while len(listIndexContClean) != intCount1:
		listIndexCont.append([])
		while len(listIndexContClean[intCount1]) != intCount2:
			listIndexCont[intCount1].append(cleanup(listIndexContClean[intCount1][intCount2]))
			intCount2 += 1
		intCount2 = 0
		intCount1 += 1
	
	if unkInput == str(unkInput):
		strInput = unkInput
		intCount = 0
		Answer = ''
		while Answer == '':
			if len(listIndexCont) != intCount and strInput == listIndexCont[intCount][1]:
				Answer = intCount
			elif len(listIndexCont) == intCount:
				Answer = False
			intCount += 1
	
	else:
		#change it to string because thats how it's stored
		strInput = str(unkInput)
		Answer = []
		intCount = 0
		while Answer == []:
			if len(listIndexCont) != intCount and strInput == listIndexCont[intCount][0]:
				Answer = listIndexCont[intCount][1]
			elif len(listIndexCont) == intCount:
				Answer = False
			intCount += 1
	
	return Answer



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

