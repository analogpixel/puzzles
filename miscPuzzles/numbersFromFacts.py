import itertools

# the letters a through f stand for the numbers 1-9 
# d+b=c  b+e=f  the digits "abc" = the digits "ad" squared

for x in itertools.permutations( range(1,10) ,6):
	if x[3] + x[1] == x[2] and x[1] + x[4] == x[5]:
		if pow(x[0] * 10 +  x[3],2) == (x[0] * 100) + (x[1] * 10) + x[2]:
			print(list(zip( ['a','b','c','d','e','f'], x )))	