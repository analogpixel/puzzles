from constraint import *

class solvePuz():
	allLetters = ['a','b','c','d','e','f','g','h','i','j','k','l','m']

	def __init__(self, puzSize, constraints):
		problem = Problem()
		self.letters = self.allLetters[0:puzSize]
		self.nums    = range(1, puzSize+1)

		print("letters:", self.letters)
		print("numbers:", self.nums)

		for j in self.letters:
			for k in self.nums:
				print("add variable:", j + str(k) )
				problem.addVariable(j + str(k), self.nums)

		# soduku constraints
		for j in self.letters:
			problem.addConstraint(AllDifferentConstraint(), [ j + str(b) for b in self.nums ]  )

		for k in self.nums:
			problem.addConstraint(AllDifferentConstraint(), [ b + str(k) for b in self.letters ]  )	

		# add all the constrains
		for c in constraints:
			print(c)
			if c[0] == 'gt':
				problem.addConstraint(lambda a,b: a>b, c[1] )
			elif c[0] == 'lt':
				problem.addConstraint(lambda a,b: a<b, c[1] )
			elif c[0] == 'eq':
				problem.addConstraint(lambda a: a==c[2], [c[1]] )
				#problem._variables[c[1]] = [c[2]]
			elif c[0] == 'dif':
				d = c[2]
				problem.addConstraint(lambda a,b: abs(a-b) == d , c[1] )
				
   		self.solutions = problem.getSolutions()

if __name__ == "__main__":
	
	"""
	s = solvePuz(2, [
		['lt', ['a1', 'a2']],
		['sum', ['a1', 'b1'], 3]
		])
	
	s = solvePuz(4, [
		['gt', ['a1','a2'] ],
		['lt', ['a3','b3'] ],
		['lt', ['b1','b2'] ],
		['lt', ['c3','c4'] ],
		['lt', ['c1','d1'] ],
		['lt', ['d3','d4'] ],
		['eq', 'a4',2] 
		])
	"""
	s = solvePuz(4,[
		["lt",["a2","b2"]],
		["gt",["b1","c1"]],
		["gt",["c2","c3"]],
		["gt",["c4","d4"]],
		["lt",["a4","b4"]],
		['eq', 'b4',2]
		])

	print(s.solutions)
