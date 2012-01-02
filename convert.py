#!/usr/bin/env python

import re

def import_pgn():
    pushed_file = raw_input('Enter what file you want to push to the database> ')
    fil = open(pushed_file, 'r')
    content = fil.read()
    



def extract_info(fi):
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
    return moves.group()

extract_info('game.pgn')



