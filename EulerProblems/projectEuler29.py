a = []

for x in range(2,101):
	for y in range(2,101):
		a.append(x ** y)

print(len(set(a)) )