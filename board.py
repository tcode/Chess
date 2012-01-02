#!/usr/bin/env python

# Copyright Tobias Lindgaard [2012] part of ChessPath
# Distributed under the terms of the GNU GPL
# For information about the GPL see LICENSE in the root.



def print_board(board):
    count = 0
    lines = 10
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
    while count < 10:
        count=count+1
        if count == 1:
            board[count] = ['AA', 'BB', 'CC', 'DD', 'EE', 'FF', 'GG', 'HH']
        if count == 2:
            board[count] = ['==', '==', '==', '==', '==', '==', '==', '==']
        if count == 3:
            board[count] = ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
        if count == 4:
            board[count] = ['WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP', 'WP']
        if count == 9:
            board[count] = ['BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP', 'BP']
        if count == 10:
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


# def bishop_move(board):
#     row = input('What row do you want ? ')
#     line = raw_input('What line do you want ? ')
#     # Some row and file
#     # Now for some evaluation of this information to retrieve where the pieces are.
#     current_row = board[row]
#     #The nasty part here is that I want to check for both the text and number representation
#     if row == 1:
#         board_1_row = True
#         # this should be good.
#         # But then again 
#     elif row == 8:
#         board_8_row = True

#     if str(line) == 'a' or int(line) == 1:
#         print current_row[1]
#         board_a_line = True 
#         # So now I want to make a diagonal search feature..
#         # So now I need to retrieve information from board.
#         if board_1_row:
#             next_row = board[row+1]
#             new_square = next_row[1+1]
#             if new_sqaure == '--':
#                 cont = True
#                 another_row=board[next_row+1]
                
#             else:
#                 cont = False
            
#         #Perhaps the code above is a bit to crude ?
#         #What can I do to lessen the if statements.
#         else:
#             if row == 2:
#                 next_row = board[row+1]
#     if str(line) == 'b' or int(line) == 2:
#         print current_row[2]
#         board_b_line = True
#     if str(line) == 'c' or int(line) == 3:
#         print current_row[3]
#         board_c_line = True
        
#     if str(line) == 'd' or int(line) == 4:
#         print current_row[4] 
#         board_d_line = True
#     if str(line) == 'e' or int(line) == 5:
#         print current_row[5]
#         board_e_line = True
#     if str(line) == 'f' or int(line) == 6:
#         print current_row[6]
#         board_f_line = True
#     if str(line) == 'g' or int(line) == 7:
#         print current_row[7]
#         board_g_line = True
#     if str(line) == 'h' or int(line) == 8:
#         print current_row[8]
#         board_h_line = True
#The above is great there is a minimal of if statements so it is not so cluttered.
#However I have not began to define any movement yet, but I am to tired to   

# do   it now.

