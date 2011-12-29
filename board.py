#!/usr/bin/env python



def print_board(board):
    count = 0
    lines = 8
    while count < lines:
        count=count+1
        print board[count]

def make_board():
    count = 0
    quad_size=8
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

nboard = make_board()
print_board(nboard)


def bishop_move(board):
    row = input('What row do you want ? ')
    line = raw_input('What line do you want ? ')
    # Some row and file
    # Now for some evaluation of this information to retrieve where the pieces are.
    current_row = board[row]
    #The nasty part here is that I want to check for both the text and number representation
    if str(line) == 'a' or int(line) == 1:
        print current_row[1]
    if str(line) == 'b' or int(line) == 2:
         print current_row[2]
    if str(line) == 'c' or int(line) == 3:
        print current_row[3]
    if str(line) == 'd' or int(line) == 4:
        print current_row[4] 
    if str(line) == 'e' or int(line) == 5:
        print current_row[5]
    if str(line) == 'f' or int(line) == 6:
        print current_row[6]
    if str(line) == 'g' or int(line) == 7:
        print current_row[7]
    if str(line) == 'h' or int(line) == 8:
        print current_row[8]
#The above is great there is a minimal of if statements so it is not so cluttered.
#However I have not began to define any movement yet, but I am to tired to do it now.

