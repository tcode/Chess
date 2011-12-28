#!/usr/bin/env python



def print_board(board):
    count = 0
    lines = 8
    while count < lines:
        count=count+1
        print board[count]

def make_board(quad_size):
    count = 0
    board = {}
    while count < quad_size:
        count=count+1
        board[count] = make_row(quad_size, count)
    set_pieces(board)
    return board


def make_row(num, row_num):
    count = 0
    row = []
    while count < num:
        row.append('--')
        count=count+1
    return row



def set_pieces(board):
    count = 0
    while count < 8:
        count=count+1
        if count == 1:
            board[count] = ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
        if count == 2:
            board[count] = ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP']
        if count == 7:
            board[count] = ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP']
        if count == 8:
            board[count] = ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']
            
def edit_board():
    return 0

#Could I get some advantage by using classes here ? There might not be that much of a different, if I am going to access the 
# Content from this file in another script, all of this is just the board implementation.
# Then should I include the edit_board function here or save that for the interface.py script ?


#All my relations should be put somewhere, without the need to call an extra function.
#The relations should be as the pieces move, so that f3 points to all squares in line f 
#and on the 3rd row, and knight jumps and all on the diagonals. (However when something 
# stands in the way it should stop to relate, but that is an inprogram problem).

nboard = make_board(8)
print_board(nboard)





