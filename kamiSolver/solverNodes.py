import sys
import unittest
import os
import copy

class simpleTest(unittest.TestCase):
    
    #def setUp(self):
    #    (self.puzzle, self.validColors, self.width, self.height, self.numMoves, self.numGroups) = loadFile("./data/puz7.txt")
        
    def test_dataLoad1(self):
        (self.puzzle, self.validColors, self.width, self.height, self.numMoves, self.numGroups) = loadFile("./data/puz7.txt")
        self.assertTrue( len(self.puzzle[0]) == self.width)
        self.assertTrue( len(self.puzzle) == self.height )
    
         
    def test_solver(self):
        print "\n\nSolving:"
        (self.puzzle, self.validColors, self.width, self.height, self.numMoves, self.numGroups) = loadFile("./data/puz9.txt")
        displayPuzzle(self.puzzle)
        print "Valid Colors:", self.validColors
        solver( buildNodes( self.puzzle), self.validColors, self.numMoves)
        
    #def test_nodeBuilder7(self):
    #    (self.puzzle, self.validColors, self.width, self.height, self.numMoves, self.numGroups) = loadFile("./data/puz7.txt")
    #    displayPuzzle(self.puzzle)
    #    node1 = buildNodes(self.puzzle)
    #    
    #    (node2,count) = mergeNodes(node1, 0, 1)
    #    (node3,count) = mergeNodes(node2, 6,1)
    #    (node4,count) = mergeNodes(node3, 0, 4)
    #    (node5,count) = mergeNodes(node4, 0, 0)
    #    print node5
    #    self.assertTrue( count == 1)
    
    """
    def test_nodeBuilder9(self):
        (self.puzzle, self.validColors, self.width, self.height, self.numMoves, self.numGroups) = loadFile("./data/puz9.txt")
        displayPuzzle(self.puzzle)
        
        node1 = buildNodes(self.puzzle)
        print node1
        (node2, count) = mergeNodes(node1, 2, 0)
        print "2->0", node2, count
        (node3, count) = mergeNodes(node2, 5, 0)
        print "5->0", node3,count
        (node4, count) = mergeNodes(node3, 5, 4)
        print "5->4", node4,count        
        (node5, count) = mergeNodes(node4, 5, 3)
        print "5->3", node5,count
        
        self.assertTrue(count ==1)
       """ 
        
        
def solver(nodes, validColors, max):
    
    if max == 0 :
        return False
    
    for v in nodes:
        if v == -1:
            continue
        for c in validColors:
            if nodes[v[0]][1] == c:
                continue
    
            (nextNodes, count) = switchColor(nodes, v[0], c)
            
            if count == 1:
                print "Solution Found"
                print "Change group %d to color %d" % (v[0],c) , nextNodes
                return True
            else:
                if solver( nextNodes, validColors, max -1):
                    print "Change group %d to color %d" % (v[0],c) , nextNodes
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
        
# load file and return everything you need to solve the puzzle
def loadFile(filename):
    (width, height, numMoves, puzzle, validColors) = parseData(open(filename, 'r').readlines())
    (puzzle, numGroups)= assignGroups(puzzle)
    return [puzzle, validColors, width, height, numMoves, numGroups]

def getColorGroup(puzzle, x,y):
    width = len(puzzle[0])
    height = len(puzzle)
    
    if x >= 0 and x < width and y >= 0 and y < height:
        return [ puzzle[y][x]['color'], puzzle[y][x]['groupId'] ]
    else:
        return [-1, -1]
        
def buildNodes(puzzle):
    width = len(puzzle[0])
    height = len(puzzle)
    
    neigh = []
    colors = []
    
    for i in range(90):
        neigh.append( [] )
        colors.append(-1)
        
    # find Neighbor groups
    for x in range(width):
        for y in range(height):
            group = puzzle[y][x]['groupId']
            colors[group] = puzzle[y][x]['color']
            for pos in [ [-1,0], [1,0], [0,-1], [0,1] ]:
                (c,g) = getColorGroup(puzzle, x + pos[0] , y+ pos[1])
                if g != -1:
                    if g != group:
                        neigh[group].append(g)
    
    nodes = []
    for i in range(90):
        if colors[i] != -1:
            nodes.append( [i, colors[i], list(set(neigh[i])) ] )
            
    return nodes        

def mergeNodes(nodes, group1, group2):
    returnNodes = copy.deepcopy(nodes)
    
    superNode = [ nodes[group1][0] , nodes[group1][1], list(set(nodes[group1][2] + nodes[group2][2])) ]
    
    if group1 in superNode[2]:
        superNode[2].remove(group1)
    if group2 in superNode[2]:
        superNode[2].remove(group2)
        
    # make sure everyone that was linking to the old node is now linking to new node
    for n in returnNodes:
        if n != -1:
            if group2 in n[2]:
                n[2].remove(group2)
                n[2].append(group1)
    
    returnNodes[group2] = -1
    returnNodes[group1] = superNode
    
    return returnNodes

def switchColor(nodes, group1, newColor):
    count = 0
    returnNodes = []
    
    returnNodes = copy.deepcopy(nodes)
    returnNodes[group1][1] = newColor # change the color
    
    for n in returnNodes[group1][2]: # find all attachednodes
        if returnNodes[n][1] == newColor: # this is a valid node of the same color
            returnNodes = mergeNodes(returnNodes, group1, returnNodes[n][0] )
    
    count = 0
    for n in returnNodes:
        if n != -1:
            count = count + 1
                 
    return [returnNodes, count]
    
    
    
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
    solver( buildNodes( puzzle), validColors, numMoves)
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        solve_it(file_location)
    else:
        print 'No data given, unit test running'
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/puz1.txt)'
        unittest.main()   
