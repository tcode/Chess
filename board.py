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
    print_board(board)
    

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
            
    
make_board(8)







