def spiral(n):
	i = 3
	total = 1
	while True:
		a = i ** 2
		b = a - (i - 1)
		c = b - (i - 1)
		d = c - (i - 1)
		#print(a,b,c,d)
		total = total + a + b + c + d
		i = i + 2
		if (i > n): return total

print(spiral(1001))