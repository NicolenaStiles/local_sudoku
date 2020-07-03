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

text_1 = '   ██  \n' +
         ' ████  \n' +
         '   ██  \n' +
         '   ██  \n' +
         '   ██  \n'

text_2 = '██████ \n' +
         '     ██\n' +
         ' █████ \n' +
         '██     \n' +
         '███████\n'

text_3 = '██████ \n' +
         '     ██\n' +
         ' █████ \n' +
         '     ██\n' +
         '██████ \n'

text_4 = '██   ██\n' +
         '██   ██\n' +
         '███████\n' +
         '     ██\n' +
         '     ██\n'

text_5 = '███████\n' +
         '██     \n' +
         '███████\n' +
         '     ██\n' +
         '███████\n'

text_6 = ' ██████\n' +
         '██     \n' +
         '███████\n' +
         '██   ██\n' +
         ' ██████\n'

text_7 = '███████\n' +
         '     ██\n' +
         '    ██ \n' +
         '   ██  \n' +
         '   ██  \n'

text_8 = ' █████ \n' +
         '██   ██\n' +
         ' █████ \n' +
         '██   ██\n' +
         ' █████ \n'

text_9 = ' █████ \n' +
         '██   ██\n' +
         ' ██████\n' +
         '     ██\n' +
         ' █████ \n'

if __name__ == '__main__':

    # formatting controls
    GRID_HEIGHT = 13
    BOX_WIDTH = 4

    test_list = range(0,9)

    for i in range(0,GRID_HEIGHT):
        if (i % BOX_WIDTH) == 0:
            print('||===========||===========||===========||')
        else:
            print('|| {}   {}   {} || {}   {}   {} || {}   {}   {} ||'.format(*test_list))
