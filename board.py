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

def edit_board(start, end, board):
    if start[1:] == 1:
        tmplist = board[1]
        if start[:1] == 'a':
            tmplist[0] = None
        if start[:1] == 'b':
            tmplist[0] = None
        if start[:1] == 'c':
            tmplist[0] = None        
        if start[:1] == 'd':
            tmplist[0] = None
        if start[:1] == 'e':
            tmplist[0] = None
        if start[:1] == 'f':
            tmplist[0] = None
        if start[:1] == 'g':
            tmplist[0] = None
        if start[:1] == 'h':
            tmplist[0] = None
                        

    if start[1:] == 2:
        tmplist = board[2]
        if start[:1] == 'a':
            tmplist[0] = None
        if start[:1] == 'b':
            tmplist[0] = None
        if start[:1] == 'c':
            tmplist[0] = None        
        if start[:1] == 'd':
            tmplist[0] = None
        if start[:1] == 'e':
            tmplist[0] = None
        if start[:1] == 'f':
            tmplist[0] = None
        if start[:1] == 'g':
            tmplist[0] = None
        if start[:1] == 'h':
            tmplist[0] = None


    if start[1:] == 3:
        tmplist = board[3]
        if start[:1] == 'a':
            tmplist[0] = None
        if start[:1] == 'b':
            tmplist[0] = None
        if start[:1] == 'c':
            tmplist[0] = None        
        if start[:1] == 'd':
            tmplist[0] = None
        if start[:1] == 'e':
            tmplist[0] = None
        if start[:1] == 'f':
            tmplist[0] = None
        if start[:1] == 'g':
            tmplist[0] = None
        if start[:1] == 'h':
            tmplist[0] = None

    if start[1:] == 4:
        tmplist = board[4]
        if start[:1] == 'a':
            tmplist[0] = None
        if start[:1] == 'b':
            tmplist[0] = None
        if start[:1] == 'c':
            tmplist[0] = None        
        if start[:1] == 'd':
            tmplist[0] = None
        if start[:1] == 'e':
            tmplist[0] = None
        if start[:1] == 'f':
            tmplist[0] = None
        if start[:1] == 'g':
            tmplist[0] = None
        if start[:1] == 'h':
            tmplist[0] = None

    if start[1:] == 5:
        tmplist = board[5]
        if start[:1] == 'a':
            tmplist[0] = None
        if start[:1] == 'b':
            tmplist[0] = None
        if start[:1] == 'c':
            tmplist[0] = None        
        if start[:1] == 'd':
            tmplist[0] = None
        if start[:1] == 'e':
            tmplist[0] = None
        if start[:1] == 'f':
            tmplist[0] = None
        if start[:1] == 'g':
            tmplist[0] = None
        if start[:1] == 'h':
            tmplist[0] = None

    if start[1:] == 6:
        tmplist = board[6]
        if start[:1] == 'a':
            tmplist[0] = None
        if start[:1] == 'b':
            tmplist[0] = None
        if start[:1] == 'c':
            tmplist[0] = None        
        if start[:1] == 'd':
            tmplist[0] = None
        if start[:1] == 'e':
            tmplist[0] = None
        if start[:1] == 'f':
            tmplist[0] = None
        if start[:1] == 'g':
            tmplist[0] = None
        if start[:1] == 'h':
            tmplist[0] = None

    if start[1:] == 7:
        tmplist = board[7]
        if start[:1] == 'a':
            tmplist[0] = None
        if start[:1] == 'b':
            tmplist[0] = None
        if start[:1] == 'c':
            tmplist[0] = None        
        if start[:1] == 'd':
            tmplist[0] = None
        if start[:1] == 'e':
            tmplist[0] = None
        if start[:1] == 'f':
            tmplist[0] = None
        if start[:1] == 'g':
            tmplist[0] = None
        if start[:1] == 'h':
            tmplist[0] = None

    if start[1:] == 8:
        tmplist = board[8]
        if start[:1] == 'a':
            tmplist[0] = None
        if start[:1] == 'b':
            tmplist[0] = None
        if start[:1] == 'c':
            tmplist[0] = None        
        if start[:1] == 'd':
            tmplist[0] = None
        if start[:1] == 'e':
            tmplist[0] = None
        if start[:1] == 'f':
            tmplist[0] = None
        if start[:1] == 'g':
            tmplist[0] = None
        if start[:1] == 'h':
            tmplist[0] = None

    return board

    
make_board(8)







