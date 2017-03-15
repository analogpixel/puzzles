
for i in range(10,100):
	for j in range(10,100):
		if i == j: continue
		x = list(str(i))
		y = list(str(j))
		
		try:
			if x[1] == '0' and y[1] == '0': continue
			if float(i) / j > 1: continue
			if x[0] == y[0] and (float(x[1])/float(y[1]) == float(i)/float(j)):
				print(i,j)
			if x[0] == y[1] and (float(x[1])/float(y[0]) == float(i)/float(j)):
				print(i,j)
			if x[1] == y[0] and (float(x[0])/float(y[1]) == float(i)/float(j)):
				print(i,j)
			if x[1] == y[1] and (float(x[0])/float(y[0]) == float(i)/float(j)):
				print(i,j)
		except:
			pass

#387296
#38729600
#1/100