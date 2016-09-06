# DESCRIPTION||read in all the words from a textfile, and then get the frequency of the letters
import pandas as pd
words = "".join(open("alice.txt").readlines())

d = {}
for letters in words:
	letter = letters.lower()
	if letter in d:
		d[letter]+=1
	else:
		d[letter] = 1

print(d)
	