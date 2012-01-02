#!/usr/bin/env python

# Copyright Tobias Lindgaard 2012, part of ChessPath
# Distributed under the GNU GPL
# For more information about the License see LICENSE.

from board import *

board = make_board()




def extract_row(num):
    row = board[num]
    return row

def return_row(num, row):
    board[num] = row

# crow = extract_row(10)
# crow[6] = '--'
# crow = extract_row(8)
# crow[5] = 'WN'

def move(srow, sline, erow, eline):
    working = extract_row(srow)
    tmp = working[sline]
    working[sline] = '--'
    end = extract_row(erow)
    end[eline] = str(tmp)

# The above could should be a function, but with how many elements ? 4 2 ?
# with 4 there is a lot of parameters to put in, but perhaps it is a little easier to make it automatic 
# and thus make it easier to make the program work a little better, 2 variables would be nicer if it 
# involves direct human interaction with this part of the package. - well even if it is designed for
# automatically generating appropriate data from part to part, it can still work with human 
# interaction. That could be an important part of the program later.
#move(3-10, 0-7, 3-10, 0-7)


#move(9, 4, 7, 4) # <- This actually works the 4 numbers are just becourse it is a internal function
# Not meant to be directly exposed to the user, then I would have done it a little nicer, but internally
# This seems a little easier to work with.

print_board(board)


