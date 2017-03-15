import math

z = []

for a in range(3,2000000):
	if a == sum(map( lambda x: math.factorial(int(x)), list(str(a)))):
		print(a)
		z.append(a)


print(sum(z))