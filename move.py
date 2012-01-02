#!/usr/bin/env python

# Copyright Tobias Lindgaard 2012, part of ChessPath
# Distributed under the GNU GPL
# For more information about the License see LICENSE.

from board import *

board = make_board()

def extract_row(num):
    row = board[num]

