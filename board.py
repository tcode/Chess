#!/usr/bin/env python

def make_row(num, row_num):
    count = 0
    row = []
    while count < num:
        row.append(0)
        count=count+1
    
    return row


row1 = make_row(8, 1)


print row1

