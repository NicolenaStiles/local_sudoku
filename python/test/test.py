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

    # formatting controls
    GRID_HEIGHT = 13
    BOX_WIDTH = 4

    # index from zero
    TEXT_HEIGHT = 4
    TEXT_WIDTH = 6

    # test array values
    puzzle_input = 

    text_array = [text_1,text_2,text_3,text_4,text_5,
                    text_6, text_7, text_8, text_9]

    for nums in range(0,9):
        print()
        for h in range(0, 5):
            print(text_array[nums][h])

#    for q in range (0,9):
#       print(test_array[q])

#    for i in range(0,GRID_HEIGHT):
#        print('||{}|{}|{}||{}|{}|{}||{}|{}|{}||'.format(*test_array))
