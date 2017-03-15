x = []
for i in range(0,2000):
	for j in range(0,2000):
		tot = i * j 
		f = list(str(tot)) + list(str(i)) + list(str(j))
		if '0' in f:
			continue
		if len(f) == 9 and len(set(f)) == 9:
			print(i,j,tot)
			x.append(tot)

print (set(x))
print (sum(set(x)))