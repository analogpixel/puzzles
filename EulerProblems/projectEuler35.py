import json
import profile

# 55 for 1 million records

# https://projecteuler.net/thread=35
# but, besides the single digit numbers, only numbers containg 1,3,7,9  are valid

"""
print("loading")
primes = json.load( open("primes.json") )
primes = [str(x) for x in primes]
print("loaded")
"""

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True   

"""
def main():
	count = 0
	for x in filter(lambda z: is_prime(z), range(0,100) ):
		x = str(x)
		if all( is_prime(j) for j in  sorted([ int("".join([x[a:],x[:a]]))for a in range(len(x)) ])  ):
			count += 1

	print(count)
"""

"""
def main():
  count = 0
  #for x in filter(lambda z: is_prime(z), range(0,1000000000) ):
  for x in primes:
    #x = str(x)
    count = count + 1
    for a in range(len(x)):
      if not is_prime( int("".join([x[a:],x[:a]]))):
        count = count -1
        break
  print("count:", count)
"""

def main():
  count = 0
  for i in range(0, 1000000000):
    x = list(str(i))
    if all( [not '2' in x,  not '5' in x,  not '4' in x,  not '6' in x,  not '8' in x, is_prime(i) ] ):
      count = count + 1
      #print(x)

  print("count:", count + 1 ) # add one for 2

profile.run('main()')

