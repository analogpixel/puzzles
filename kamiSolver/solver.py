import sys
import unittest
import os
import copy

class simpleTest(unittest.TestCase):
    
    def setUp(self):
        (self.puzzle, self.validColors, self.width, self.height, self.numMoves, self.numGroups) = loadFile("./data/puz7.txt")
        
    def test_dataLoad1(self):
        self.assertTrue( len(self.puzzle[0]) == self.width)
        self.assertTrue( len(self.puzzle) == self.height )
    
    def test_notSolved(self):
        self.assertFalse( solved(self.puzzle) )
        
    def test_fills(self):
       
        display = False
        
        # puzzle, x,y, targetColor, replacementColor, groupId
        (x,y,c) = findGroup(self.puzzle,0)
        (puz1, numGroups)  =  assignGroups( floodFill(self.puzzle, x,y, c, 1,0)  )
        if display: displayPuzzle(puz1)
        
        (x,y,c) = findGroup(puz1, 4)
        (puz1, numGroups)  =  assignGroups( floodFill(puz1, x,y, c, 1,0)  )
        if display: displayPuzzle(puz1)
        
        (x,y,c) = findGroup(puz1, 0)
        (puz1, numGroups)  =  assignGroups( floodFill(self.puzzle, x,y, c, 4,0)  )
        if display: displayPuzzle(puz1)
        
        (x,y,c) = findGroup(puz1,0)
        (puz1, numGroups)  =  assignGroups( floodFill(self.puzzle, x,y, c, 0,0)  )
        if display: displayPuzzle(puz1)
        
        self.assertTrue( solved(puz1) )
    
    def test_solver(self):
        print "\n\nSolving:"
        if solver(self.puzzle, self.numGroups, self.validColors,  self.numMoves):
            displayPuzzle(self.puzzle)
        pass
    

def solver(puzzle, numGroups, validColors,  max):
    
    if max < 0 :
        return False
    
    if numGroups == 1:
        return True
    
    for g in range(numGroups):
        for c in validColors:
            # find a location of the group
            (x,y,targetColor) = findGroup(puzzle, g)
            # puzzle, x,y, targetColor, replacementColor, groupId
            if c == targetColor: continue
            (puz1, ng) = assignGroups( floodFill(copy.deepcopy(puzzle), x,y, targetColor, c,g)  )
            
            if solver( puz1, ng, validColors, max-1):
                displayPuzzle(puz1)
                return True
    
    return False


def findGroup(puzzle, group):
    width = len(puzzle[0])
    height = len(puzzle)
    
    for x in range(width):
        for y in range(height):
            if puzzle[y][x]['groupId'] == group:
                return [x,y, puzzle[y][x]['color'] ]
    
    return [-1,-1,-1]
    
def solved(puzzle):
    width = len(puzzle[0])
    height = len(puzzle)
    c1 = puzzle[0][0]['color']
    
    for x in range(width):
        for y in range(height):
            if puzzle[y][x]['color'] == c1:
                continue
            else:
                return False
    
    return True
    
# load file and return everything you need to solve the puzzle
def loadFile(filename):
    (width, height, numMoves, puzzle, validColors) = parseData(open(filename, 'r').readlines())
    (puzzle, numGroups)= assignGroups(puzzle)
    return [puzzle, validColors, width, height, numMoves, numGroups]
    
def createNodeGraph(edges):
    output = "digraph  G {\n"
    i = 0
    for n in edges:
        for e in n:
            output = output + "n_" + str(i) + " -> " + "n_" + str(e) + ";\n"
        i = i + 1
    output = output + "}"
    return output
    
def displayPuzzle(puzzle):
    print "\nGroups"
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            print(puzzle[y][x]['groupId']),
        print
    
    print "\nColors"
    for y in range(len(puzzle)):
        for x in range(len(puzzle[0])):
            print(puzzle[y][x]['color']),
        print
   
def parseData(data):
    (width, height) = map( lambda s: int(s.strip()), data[0].split(','))
    numMoves = int(data[1].strip())
    puzzle = []
    
   
    for line in data[2:]:
        puzzle.append( map(lambda s: {'color': int(s) , 'groupId': -1, 'edges': [] } , line.strip().split(',') ))
    
    validColors = []
    for y in range(height):
        for x in range(width):
            validColors.append(puzzle[y][x]['color'])
        
    return [width, height, numMoves, puzzle, set(validColors)]

    
def floodFill(puzzle, x,y, targetColor, replacementColor, groupId):
    
    if x > len(puzzle[0])-1:
        return puzzle
    if x < 0:
        return puzzle
    if y > len(puzzle)-1:
        return puzzle
    if y< 0:
        return puzzle
    
    if puzzle[y][x]['color'] == replacementColor:
        return puzzle
    
    if puzzle[y][x]['color'] != targetColor:
        return puzzle
    
    puzzle[y][x]['color'] = replacementColor
    puzzle[y][x]['groupId'] = groupId
    
    puzzle = floodFill(puzzle, x+1, y, targetColor, replacementColor, groupId)
    puzzle = floodFill(puzzle, x-1, y, targetColor, replacementColor, groupId)
    puzzle = floodFill(puzzle, x, y+1, targetColor, replacementColor, groupId)
    puzzle = floodFill(puzzle, x, y-1, targetColor, replacementColor, groupId)
    
    return puzzle


def assignGroups(puzzle):
    groups = 0
    
    width = len(puzzle[0])
    height = len(puzzle)
    
    for x in range(width):
        for y in range(height):
            puzzle[y][x]['groupId'] = -1
            puzzle[y][x]['color'] = puzzle[y][x]['color'] + 100
        
    for x in range(width):
        for y in range(height):
            if puzzle[y][x]['groupId'] == -1:
                puzzle = floodFill(puzzle, x,y, puzzle[y][x]['color'],  puzzle[y][x]['color'] - 100, groups)
                groups = groups + 1
    
    return [puzzle, groups]


def solve_it(data):
    (puzzle, validColors, width, height, numMoves, numGroups) = loadFile(data)
    displayPuzzle(puzzle)
    print "\n\nSolving:"
    if solver(puzzle, numGroups, validColors,  numMoves):
        displayPuzzle(puzzle)    
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        solve_it(file_location)
    else:
        print 'No data given, unit test running'
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/puz1.txt)'
        unittest.main()   
