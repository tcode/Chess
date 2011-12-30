#!/usr/bin/env python
import re

# Seemingly nobody have written something that parse pgn's in python so I want to do that myself.
#  Take apart the file import it into a bytecompiled version of the tree of games representated in the pgn
# In that way it could become a lot faster to search and find a certain position and relevant branches from there.
# Of course this is a rather abstract idea I have no good idea for how to implement this bytecode for making a pgn tree

#      $ start position
#     / \ Branches in the database
#    /  /\   And in chess the branches increases for everymove, at least sometimes, in some variations the branches really only
# increase after 10 moves or so.

# def generate_tree():
#     tbyte = 0x00000000000000000000000000000000 #<- 32 bit hash Hopefully that is sufficient
#     return tbyte



# def update_tree(tbyte):
#     if tbyte == 0x0000000000000000000000000000000:
#         print "This is the starting position"
#     else:
#         # So here we should have some magic stuff that can turn data from hex into other
#         #  information.


# def convert_moves_to_tree():
#     user_input = str(raw_input('input the path to the file you wish to have analyzed> '))
#     f = open(user_input_file, 'r')
#     str_input = f.readline() #Please format the text properly, I should create a script
# #check the format of the target file please like : 1 white-move black-move \n
#     #Do I really need to write a whole lot of this nasty if-statements ?
    

def extract_info():
    fi = raw_input('Input file: ')
    pgn = open(fi, 'r')
    cont = pgn.read()
    event = re.search(r'.Event.+', cont)
    site = re.search(r'.Site.+', cont)
    date = re.search(r'.Date.+', cont)
    mround = re.search(r'.Round.+', cont)
    white = re.search(r'.White.+', cont)
    black = re.search(r'.Black.+', cont)
    result = re.search(r'.Result.+', cont)
    moves = re.search(r'1\.\s.+(1|0|1/2)', cont)
    nmoves = re.sub('', '5', cont)
    print event.group(), "\n", site.group(), "\n", date.group(), "\n", mround.group(), "\n", white.group(), "\n", black.group(), "\n", result.group(), "\n", moves.group(), "\n\n", nmoves


extract_info()


# def convert_pgn():
#     moves = re.sub('e', 5, moves)
#     print moves.group()

# convert_pgn
