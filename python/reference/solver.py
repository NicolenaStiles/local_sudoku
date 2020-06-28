'''
# Sudoku Solver
# Nicolena Stiles

# Version 1.0
# 11/26/2016

# TODO:
# Add in constant variables for certain numbers?
# Add version control


# 81 digit test string
# 123456789123456789123456789123456789123456789123456789123456789123456789123456789

Sudoku puzzle test string
(from NYtimes website-- they offer partial solutions ;D)

Unsolved:
007528069940007002600004701301050070000786190780300020019000205073090600005840000

Answer:
137528469948167352652934781391452876524786193786319524819673245473295618265841937
'''

import sys

'''
Class Definition:
   Sudoku Puzzle Obj.
'''

class puzzle:
    def __init__(self, linearArray):
        # Loading up the empty puzzle into "puzzle":
        puzzle = []
        currentColumn = []
        for k in range(0, len(array)):
            if (((k+1) % 9) == 0) and (k > 0):
                currentColumn.append(array[k])
                puzzle.append(currentColumn)
                currentColumn = []
            else:
                currentColumn.append(array[k])
        self.grid = puzzle

        # Loading the row array with the values at each row:
        rowArray = []
        for r in range(0, len(self.grid[0])):
            rowArray.append(self.grid[r])
        self.rowArray = rowArray

        # Loading the column array with values at each column:
        columnArray = []
        for q in range(0, len(self.grid[0])):
            currArray = []
            for c in range(0, len(self.grid[0])):
                currArray.append(self.grid[c][q])
            columnArray.append(currArray)
        self.columnArray = columnArray

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

        # Final box array:
        self.boxArray = boxArray

        # The empty solution property:
        self.solution = []

    # Adapt this to print both puzzle and solution?
    def printPuzzle(self):
        rowString = '--------------------------------\n'
        for x in range(0, len(self.grid)):
            rowString = rowString + '| '
            for y in range(0, len(self.grid[0])):
                if (((y+1) % 3) == 0):
                    rowString = rowString + ' %s |' % (str(self.grid[x][y]));
                else:
                    rowString = rowString + ' %s ' % (str(self.grid[x][y]));
            rowString = rowString + '\n'
            if (((x+1) % 3) == 0):
                rowString = rowString + '--------------------------------\n'
        print(rowString)

    # Returns array of values at requested row
    def getRow(self, row):
        return(self.rowArray[row])

    # Returns array of values at requested column
    def getColumn(self, col):
        return(self.columnArray[col])

    # Returns array of values at requested box
    def getBox(self, row, col):
        # All possible box options, 0-8
        # [0-2][0-2]
        if (row <= 2) and (col <= 2):
            return self.boxArray[0]
        # [0-2][3-5]
        elif (row <= 2) and (col >= 3) and (col <= 5):
            return self.boxArray[1]
        # [0-2][6-8]
        elif (row <= 2) and (col >= 6) and (col <= 8):
            return self.boxArray[2]
        # [3-5][0-2]
        elif (row >= 3) and (row <= 5) and (col <= 2):
            return self.boxArray[3]
        # [3-5][3-5]
        elif (row >= 3) and (row <= 5) and (col >= 3) and (col <= 5):
            return self.boxArray[4]
        # [3-5][6-8]
        elif (row >= 3) and (row <= 5) and (col >= 6) and (col <= 8):
            return self.boxArray[5]
        # [6-8][0-2]
        elif (row >= 6) and (row <= 8) and (col >= 0) and (col <= 2):
            return self.boxArray[6]
        # [6-8][3-5]
        elif (row >= 6) and (row <= 8) and (col >= 3) and (col <= 5):
            return self.boxArray[7]
        # [6-8][6-8]
        elif (row >= 6) and (row <= 8) and (col >= 6) and (col <= 8):
            return self.boxArray[8]

    # Returns array of options for each cell
    # Currently stuck here.
    def cellSolutionOptions(self):
        possCellSolutionsRow = []
        possCellSolutionsCol = []
        for r in range(0, len(self.grid[0])):
            for c in range(0, len(self.grid[0])):
                currCell = list(range(1, 10))
                if self.grid[r][c] == 0:
                    for i in range(1, 10):
                        if (i in self.getRow(r)) and (i in currCell):
                            currCell.remove(i)
                        if (i in self.getColumn(c)) and (i in currCell):
                            currCell.remove(i)
                        if (i in self.getBox(r, c)) and (i in currCell):
                            currCell.remove(i)
                    possCellSolutionsCol.append(currCell)
                if self.grid[r][c] != 0:
                    possCellSolutionsCol.append(self.grid[r][c])
                if (((c+1) % 9) == 0) and (c > 0):
                    possCellSolutionsRow.append(possCellSolutionsCol)
                    possCellSolutionsCol = []
        return possCellSolutionsRow


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
test.printPuzzle()
print(test.grid)
solutionOptArray = test.cellSolutionOptions()
print(solutionOptArray)

'''
print(test.rowArray)
print(test.columnArray)
print(test.boxArray)

'''
