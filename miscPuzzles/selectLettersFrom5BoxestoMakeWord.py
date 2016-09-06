
# DESCRIPTION||use itertools to search for words. @puzzle

import itertools
import puzzleLib


a = [ ['g','r','a'],
      ['b','l','o'],
      ['a','c','l'],
      ['q','k','d'],
      ['s','y','u'] ]

b = [ 
	['i','h','f'],
	['a','a','e'],
	['r','t','l'],
	['u','g','o'],
	['o','h','n']
	]


wl =  puzzleLib.loadEnglishDictionary()

for i in itertools.product( *a):
	word = str("".join(i))
	if puzzleLib.inDictionary(wl, word):
		print( "".join(i) )