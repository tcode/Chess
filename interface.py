#!/usr/bin/env python


# Seemingly nobody have written something that parse pgn's in python so I want to do that myself.
#  Take apart the file import it into a bytecompiled version of the tree of games representated in the pgn
# In that way it could become a lot faster to search and find a certain position and relevant branches from there.
# Of course this is a rather abstract idea I have no good idea for how to implement this bytecode for making a pgn tree

#      $ start position
#     / \ Branches in the database
#    /  /\   And in chess the branches increases for everymove, at least sometimes, in some variations the branches really only
# increase after 10 moves or so.

def generate_tree():
    tbyte = 0x00000000000000000000000000000000 #<- 32 bit hash Hopefully that is sufficient
    return tbyte

    





def update_tree(tbyte):
    if tbyte == 0x0000000000000000000000000000000:
        print "This is the starting position"
    else:
        #So here we should have some magic stuff that can turn data from hex into other
        # information.



# This is a probably very unclever way of representing this information.
# But I have to store it as something.
    





