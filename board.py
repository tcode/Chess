#!/usr/bin/env python

#Here we are going to conceive of some chessboard reprensentation.
# my first attempt would be a reprensentation

def mlist(num):
    new_list=[]
    count = 0
    while count < num:
        new_list.append(0)
        count = count + 1
    print new_list
    new_board(8, new_list)


def new_board(num, blist):
    count = 0
    board = []
    while count < num:
        board.append(blist)
        count=count+1
    
        #Technically this is a board of sorts.
        #Now I just need to figure out how I do print it, but should be easy

mlist(8)

   
