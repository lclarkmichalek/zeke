#!/usr/bin/python
# -*- coding: utf-8 -*-

from tempfile import *
from zekemods import *
from cPickle import *
from csv import *

declareglobs()

cleanup = lambda s: s[:-1] if s[-1] in ['\n', '\r'] else s


def writeAssIndex(dicAssIndex):
	
	with openassindex('w') as fileAssIndex:
		dump(dicAssIndex, fileAssIndex)
	

def writeass(intIndex1, intIndex2):
	
	if intIndex1 > intIndex2:
		intIndex1, intIndex2 = intIndex2, intIndex1
	
	fileDic = openassdic()
	listDicCont = fileDic.readlines()
	fileDic.seek(0)
	fileDic.close()
	
	listDicCont2 =[]
	for x in listDicCont:
		listDicCont2.append(x.replace('\r', '').replace('\n', ''))
	listDicCont = listDicCont2

	if len(listDicCont) - 1 < intIndex1:
		bolIndex1PreExist = False
	else:
		bolIndex1PreExist = True
	
	if len(listDicCont) - 1 < intIndex2:
		bolIndex2PreExist = False
	else:
		bolIndex2PreExist = True
	
		while intCount1 < len(listDicCont):
			
			strLineCont = ''
			for x in listDicCont[intCount1]:
				strLineCont = strLineCont + str(x) + ','
			strLineCont = strLineCont[:-1] + '\n'
			
			tempfileFakeDic.write(strLineCont)
			
			intCount1 += 1
	
	tempfileFakeDic = TemporaryFile(mode='w+')
	writerFakeDic = writer(tempfileFakeDic, delimiter=',', quotechar='')
	
	if bolIndex1PreExist and bolIndex2PreExist:
		
		for intCount1 in range(0, intIndex1):
			writerFakeDic.writerow(listDicCont[intCount1])
		
		writerFakeDic.writerow(listDicCont[intCount1] + [intIndex2])
		
		for intCount1 in range(intIndex1, intIndex2):
			writerFakeDic.writerow(listDicCont[intCount1])
		
		
		writerFakeDic.writerow(listDicCont[intCount1] + [intIndex1])
		
		for intCount1 in range(intIndex2, len(listDicCont)):
			writerFakeDic.writerow(listDicCont[intCount1])
		
		
		tempfileFakeDic.seek(0)
		with openassdic('w') as fileDic:
			fileDic.write(tempfileFakeDic.read())
		tempfileFakeDic.close()
		
		return True
		
	elif bolIndex2PreExist and not bolIndex1PreExist:
		
		for intCount1 in range(0, intIndex2):
			writerFakeDic.writerow(listDicCont[intCount1])
		
		writerFakeDic.writerow(listDicCont[intCount1] + [intIndex1])
		
		for intCount1 in range(intIndex2, len(listDicCont)):
			writerFakeDic.writerow(listDicCont[intCount1])
		
		writerFakeDic.writerow([intIndex1, intIndex2])
		
		tempfileFakeDic.seek(0)
		with openassdic('w') as fileDic:
			fileDic.write(tempfileFakeDic.read())
		tempfileFakeDic.close()
		
		return True
		
	elif not bolIndex1PreExist and not bolIndex2PreExist:
		
		for intCount1 in range(0, len(listDicCont)):
			writerFakeDic.writerow(listDicCont[intCount1])
		
		writerFakeDic.writerow([intIndex1, intIndex2])
		writerFakeDic.writerow([intIndex2, intIndex1])
		
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
	if not listReturn:
		return False
	for x in listReturn:
		listintReturn.append(int(x))
	
	return listintReturn


#checkindex = lambda intstrInput: True if type(getindex(intstrInput)) != type(True) else False

def getAssIndex():
	
	with open(GLOBALSTORAGE + 'assindex.txt') as fileAssIndex:
		if fileAssIndex.readlines() == ['\n']:
			writeAssIndex({})
		fileAssIndex.seek(0)
		return load(fileAssIndex)
	
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
#Doooone
def writewdtype(dicWrite):
	with open(GLOBALSTORAGE + 'wdtypedic.txt', 'w') as fileWdtype:
		dump(dicWrite, fileWdtype)

def getwdtype():
	with open(GLOBALSTORAGE + 'wdtypedic.txt') as fileWdtype:
		if len(fileWdtype.read()) == 0:
			dicAnswer = {}
		else:
			fileWdtype.seek(0)
			dicAnswer = load(fileWdtype)
	return dicAnswer
