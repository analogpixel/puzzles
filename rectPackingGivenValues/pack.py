box = [ 
		[4,0,0,0,0,0,0,0,8,0],
		[0,0,0,0,4,0,0,0,0,0],
		[4,0,0,0,0,9,10,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,6,0,0,0,0,0,0,0,10],
		[0,6,0,0,0,3,0,0,0,0],
		[0,0,0,4,0,0,0,0,0,0],
		[2,0,0,0,0,0,10,0,0,0]
	  ]

moves = {}
moves[2] = [(1,2), (2,1)]
moves[3] = [(3,1), (1,3)]
moves[4] = [(2,2), (1,4), (4,1)]
moves[6] = [(2,3), (3,2), (1,6), (6,1)]
moves[8] = [(4,2), (2,4), (1,8), (8,1)]
moves[9] = [(1,9), (9,1), (3,3)]
moves[10] = [(1,10), (10,1), (2,5), (5,2)]

checks = []
for y in range(0, len(box)):
	for x in range(0, len(box[0])):
		if box[y][x] != 0:
			checks.append( {'n': box[y][x], 'x': x, 'y': y})


def validMoves():
	pass

validMoves(10, 6,7, box)