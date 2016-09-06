#DESCRIPTION||rotate lists in odometer fashion; when first goes around, seonnd tics up once.

import sys
from puzzleLib import *


"""
you have 5 Columns of letters, columns can shift up and down by one.

shift the columns up and down until you all the rows spell an english word.
"""

a = [
  ['a','c','d','f'],
  ['r','i','l','a'],
  ['e','g','r','o'],
  ['w','n','a','o'],
  ['d','e','m','n']
  ]

		
count = 0
wordList = loadEnglishDictionary()

while count < 5 * 5 * 5 * 5:
	
	if inDictionary(wordList, [getCol(a,x) for x in range(0,4)] ):
		print( ",".join( [getCol(a,x) for x in range(0,4)] ))
		sys.exit()

	a = rotateRow(a,1)
	if count % 4 == 0:
		a = rotateRow(a,2)
	if count % 8 == 0:
		a = rotateRow(a,3)
	if count % 12 == 0:
		a = rotateRow(a,4)

	count = count + 1

	



