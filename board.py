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
    print_board(board)
    

def make_row(num, row_num):
    count = 0
    row = []
    while count < num:
        row.append(0)
        count=count+1
    return row


make_board(8)







