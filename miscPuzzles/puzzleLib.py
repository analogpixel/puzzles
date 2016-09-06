# DESCRIPTION||library to solve @puzzles in @python
"""
Given a 2 dimensional list return column X
"""
def getCol(a, i):
	return  "".join( [ a[x][i] for x in range(0, 1+len(a[0]))] )

"""
Given a 2 dimension list rotate row X by 1

shift right
"""
def rotateRow(a, x):
	a[x] = [a[x][-1]] + a[x][:-1]
	return a

"""
Load english dictionary into a list, return dictionary as a list
"""
def loadEnglishDictionary():
	return [x.strip() for x in open("e:/reference/lists/englishWords.txt").readlines()]



"""
given a list of words, and a list/string, check if they are all
in the list of words
"""
def inDictionary(wordList, checkWords):
	if type(checkWords) is list:
		return all( x in wordList for x in checkWords )
	if type(checkWords) is str:
		return checkWords in wordList
	else:
		return False