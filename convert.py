#!/usr/bin/env python

import re

def import_pgn():
    pushed_file = raw_input('Enter what file you want to push to the database> ')
    fil = open(pushed_file, 'r')
    content = fil.read()
    
