# Main test file for python-based Sudoku
#
#
# Created by Nicolena Stiles
# 06/26/2020

'''
||=============================||=============================||=============================||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
||---------|---------|---------||---------|---------|---------||---------|---------|---------||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
||---------|---------|---------||---------|---------|---------||---------|---------|---------||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
||=============================||=============================||=============================||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
||---------|---------|---------||---------|---------|---------||---------|---------|---------||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
||---------|---------|---------||---------|---------|---------||---------|---------|---------||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
||=============================||=============================||=============================||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
||---------|---------|---------||---------|---------|---------||---------|---------|---------||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
||---------|---------|---------||---------|---------|---------||---------|---------|---------||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
|| xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx || xxxxxxx | xxxxxxx | xxxxxxx ||
||=============================||=============================||=============================||

5 tall
7 wide

Text references:

   ██     ██████      ██████      ██   ██     ███████      ██████      ███████      █████       █████ 
  ███          ██          ██     ██   ██     ██          ██                ██     ██   ██     ██   ██ 
   ██      █████       █████      ███████     ███████     ███████          ██       █████       ██████ 
   ██     ██               ██          ██          ██     ██    ██        ██       ██   ██          ██ 
   ██     ███████     ██████           ██     ███████      ██████         ██        █████       █████       

   01234567890123456789012345678901234567890
0  ||===========||===========||===========||0
1  || x   x   x || x   x   x || x   x   x ||
2  || x   x   x || x   x   x || x   x   x ||
3  || x   x   x || x   x   x || x   x   x ||
4  ||===========||===========||===========||4
5  || x   x   x || x   x   x || x   x   x ||
6  || x   x   x || x   x   x || x   x   x ||
7  || x   x   x || x   x   x || x   x   x ||
8  ||===========||===========||===========||8
9  || x   x   x || x   x   x || x   x   x ||
10 || x   x   x || x   x   x || x   x   x ||
11 || x   x   x || x   x   x || x   x   x ||
12 ||===========||===========||===========||12

taking input:

name = input("Enter test string:")
print(name)                                                                                                       
'''

import sys
import math

text_1 = ['   ██  ',
          ' ████  ',
          '   ██  ',
          '   ██  ',
          '   ██  ']

text_2 = ['██████ ',
          '     ██',
          ' █████ ',
          '██     ',
          '███████']

text_3 = ['██████ ',
          '     ██',
          ' █████ ',
          '     ██',
          '██████ ']

text_4 = ['██   ██',
          '██   ██',
          '███████',
          '     ██',
          '     ██']

text_5 = ['███████',
          '██     ',
          '███████',
          '     ██',
          '███████']

text_6 = [' ██████',
          '██     ',
          '███████',
          '██   ██',
          ' ██████']

text_7 = ['███████',
          '     ██',
          '    ██ ',
          '   ██  ',
          '   ██  ']

text_8 = [' █████ ',
          '██   ██',
          ' █████ ',
          '██   ██',
          ' █████ ']

text_9 = [' █████ ',
          '██   ██',
          ' ██████',
          '     ██',
          ' █████ ']

if __name__ == '__main__':

    # display constants
    GRID_HEIGHT = 13
    BOX_WIDTH = 4

    # index from zero
    TEXT_HEIGHT = 4
    TEXT_WIDTH = 6

    # Build "golden sudoku" puzzle
    # INDEX AS: 0-8
    # VALUES FROM: 1-9
    SUDOKU_GRID_SIZE = 3
    SUDOKU_VALUE = SUDOKU_GRID_SIZE * SUDOKU_GRID_SIZE

    # Build out a reference array of numbers 1-9.
    reference_array = []
    for val in range(1,SUDOKU_VALUE+1):
        reference_array.append(val)

    # Map the reference array to a golden sudoku puzzle.
    offset = 0
    golden_puzzle = []
    for n in range(0,SUDOKU_VALUE):
        for m in range(0,SUDOKU_VALUE):
            pass
        if (n % SUDOKU_GRID_SIZE == 0):
            offset = (n / SUDOKU_GRID_SIZE)
            print(offset)
        else:
            offset = offset + SUDOKU_GRID_SIZE
            print(offset)

    #for i in range(0,GRID_HEIGHT):
        #print('||{}|{}|{}||{}|{}|{}||{}|{}|{}||'.format(*test_array))

    text_array = [text_1,text_2,text_3,text_4,text_5,
                    text_6, text_7, text_8, text_9]

    #for nums in range(0,9):
        #print()
        #for h in range(0, 5):
            #print(text_array[nums][h])

#    for q in range (0,9):
#       print(test_array[q])
