sol = []

for i in range(2,200000):
	t = 0
	for x in list(str(i)):
		t = t + (int(x) ** 5)
	if i == t:
		sol.append(i)

print(sum(sol))
