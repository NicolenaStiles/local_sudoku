# Main file for Pygame based Sudoku
#
#
# Created by Nicolena Stiles
# 06/23/2020

'''
Unsolved:
007528069940007002600004701301050070000786190780300020019000205073090600005840000

Answer:
137528469948167352652934781391452876524786193786319524819673245473295618265841937
'''

# Grid = 2-D array to initalize grid object with.
# Will generate a grid data object if one is not provided
class GridModel(object):

    def __init__(self, grid=[]):
        if self.grid==[]:
            print("Generating a random Sudoku puzzle...")
