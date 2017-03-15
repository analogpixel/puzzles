sol = 0
for a in range(0,201):
	for b in range(0,101):
		if a + b*2 > 200:
			break
		for c in range(0,41):
			if a + b*2 + c*5 > 200:
				break
			for d in range(0,21):
				if a + b*2 + c*5 + d*10 > 200:
					break
				for e in range(0,11):
					if a + b*2+c*5 +d*10 +e*20 > 200:
						break
					for f in range(0,5):
						if a + b*2+c*5 +d*10 +e*20 +f*50> 200:
						for g in range(0,3):
							if a + b*2 + c *5 + d*10 + e*20 + f*50 + g*100 == 200:
								sol = sol + 1
								print(sol)

# add one for using 2pound note
print(sol + 1)
