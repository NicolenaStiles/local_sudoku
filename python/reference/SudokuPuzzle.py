'''
Unsolved:
007528069940007002600004701301050070000786190780300020019000205073090600005840000

Answer:
137528469948167352652934781391452876524786193786319524819673245473295618265841937
'''

import sys

class puzzle:
    def __init__(self, linearArray):
        # Loading up the empty puzzle into "puzzle":

        #########################
        # PUBLIC-- GRID PROPERTIES
        #   -- initial: the unsolved sudoku puzzle in linear, integer form
        # PRIVATE-- LOCAL VARIABLES
        #   -- rowArray
        #   -- columnArray
        #   -- boxArray
        #########################

        puzzle = []
        currentColumn = []
        for k in range(0, len(linearArray)):
            if (((k+1) % 9) == 0) and (k > 0):
                currentColumn.append(linearArray[k])
                puzzle.append(currentColumn)
                currentColumn = []
            else:
                currentColumn.append(linearArray[k])
        self.grid = puzzle

        # *** NOT A PROPERTY!
        # Loading the row array with the values at each row:
        rowArray = []
        for r in range(0, len(self.grid[0])):
            rowArray.append(self.grid[r])

        # *** NOT A PROPERTY!
        # Loading the column array with values at each column:
        columnArray = []
        for q in range(0, len(self.grid[0])):
            currArray = []
            for c in range(0, len(self.grid[0])):
                currArray.append(self.grid[c][q])
            columnArray.append(currArray)

        # *** NOT A PROPERTY!
        # Loading the box array with values in each box:
        # FIND A WAY TO SPEED THIS UP???
        boxArray = []
        currBox = []

        # Box 0
        for r in range(0, 3):
            for c in range(0, 3):
                currBox.append(self.grid[r][c])
        boxArray.append(currBox)
        currBox = []

        # Box 1
        for r in range(0, 3):
            for c in range(3, 6):
                currBox.append(self.grid[r][c])
        boxArray.append(currBox)
        currBox = []

        # Box 2
        for r in range(0, 3):
            for c in range(6, 9):
                currBox.append(self.grid[r][c])
        boxArray.append(currBox)
        currBox = []

        # Box 3
        for r in range(3, 6):
            for c in range(0, 3):
                currBox.append(self.grid[r][c])
        boxArray.append(currBox)
        currBox = []

        # Box 4
        for r in range(3, 6):
            for c in range(3, 6):
                currBox.append(self.grid[r][c])
        boxArray.append(currBox)
        currBox = []

        # Box 5
        for r in range(3, 6):
            for c in range(6, 9):
                currBox.append(self.grid[r][c])
        boxArray.append(currBox)
        currBox = []

        # Box 6
        for r in range(6, 9):
            for c in range(0, 3):
                currBox.append(self.grid[r][c])
        boxArray.append(currBox)
        currBox = []

        # Box 7
        for r in range(6, 9):
            for c in range(3, 6):
                currBox.append(self.grid[r][c])
        boxArray.append(currBox)
        currBox = []

        # Box 8
        for r in range(6, 9):
            for c in range(6, 9):
                currBox.append(self.grid[r][c])
        boxArray.append(currBox)
        currBox = []

        #########################
        # PRIVATE-- GRID ACCESS FUNCTIONS
        #   -- getRow
        #   -- getColumn
        #   -- getBox
        #########################

        # Returns array of values at requested row
        def getRow(row):
            return rowArray[row]

        # Returns array of values at requested column
        def getColumn(col):
            return columnArray[col]

        # Returns array of values at requested box
        def getBox(row, col):
            # All possible box options, 0-8
            # [0-2][0-2]
            if (row <= 2) and (col <= 2):
                return boxArray[0]
            # [0-2][3-5]
            elif (row <= 2) and (col >= 3) and (col <= 5):
                return boxArray[1]
            # [0-2][6-8]
            elif (row <= 2) and (col >= 6) and (col <= 8):
                return boxArray[2]
            # [3-5][0-2]
            elif (row >= 3) and (row <= 5) and (col <= 2):
                return boxArray[3]
            # [3-5][3-5]
            elif (row >= 3) and (row <= 5) and (col >= 3) and (col <= 5):
                return boxArray[4]
            # [3-5][6-8]
            elif (row >= 3) and (row <= 5) and (col >= 6) and (col <= 8):
                return boxArray[5]
            # [6-8][0-2]
            elif (row >= 6) and (row <= 8) and (col >= 0) and (col <= 2):
                return boxArray[6]
            # [6-8][3-5]
            elif (row >= 6) and (row <= 8) and (col >= 3) and (col <= 5):
                return boxArray[7]
            # [6-8][6-8]
            elif (row >= 6) and (row <= 8) and (col >= 6) and (col <= 8):
                return boxArray[8]

        #########################
        # PUBLIC-- GRID PROPERTIES
        #   -- solution: 2D array containing the solution for the puzzle
        #########################

        def generateSolution(gridEntry):
            solution = self.grid
            solved = False
            while not solved:
                solved = True
                for r in range(0, len(solution[0])):
                    for c in range(0, len(solution[0])):
                        if solution[r][c].__class__.__name__ == 'int':
                            if solution[r][c] == 0:
                                solved = False
                                currentCell = list(range(1, 10))
                                for i in range(1, 10):
                                    if (i in getRow(r)) and (i in currentCell):
                                        currentCell.remove(i)
                                    if (i in getColumn(c)) and (i in currentCell):
                                        currentCell.remove(i)
                                    if (i in getBox(r, c)) and (i in currentCell):
                                        currentCell.remove(i)
                                solution[r].pop(c)
                                solution[r].insert(c, currentCell)
                        if solution[r][c].__class__.__name__ == 'list':
                            solved = False
                            if len(solution[r][c]) == 1:
                                print(solution[r][c])
                                toConvert = solution[r][c][0]
                                solution[r].pop(c)
                                solution[r].insert(c, toConvert)
                            else:
                                copyFix = solution[r][c]
                                for q in range(len(solution[r][c])):
                                    if q < len(solution[r][c]):
                                        if solution[r][c][q] in getRow(r):
                                            copyFix.remove(solution[r][c][q])
                                            solution[r].pop(c)
                                            solution[r].insert(c, copyFix)
                                        elif solution[r][c][q] in getColumn(c):
                                            copyFix.remove(solution[r][c][q])
                                            solution[r].pop(c)
                                            solution[r].insert(c, copyFix)
                                        elif solution[r][c][q] in getBox(r, c):
                                            copyFix.remove(solution[r][c][q])
                                            solution[r].pop(c)
                                            solution[r].insert(c, copyFix)
            return solution

        # The empty solution property:
        self.solution = generateSolution(self.grid)


'''
Function Definitions:
   Main Program
'''

def userPrompt():
    print("Hello and welcome to the sudoku solver!\n"
          "Enter the puzzle to be solved as a single linear string.\n"
          "(Blanks are zeros; no commas or spaces please!)")
    entry = raw_input()
    return entry

# Change to "convert string to puzzle object"?
def convertStringToIntArray(entryString):
    if (len(entryString) != 81):
        print("Error: entry length invalid!")
        sys.exit()
    entryArray = []
    for i in range(0, len(entryString)):
        entryArray.append(int(entryString[i]))
    return entryArray

'''
Main Program
'''

e = userPrompt()
array = convertStringToIntArray(e)
test = puzzle(array)
print(test.solution)
