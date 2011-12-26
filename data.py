#!/usr/bin/env python
import pgn
#This is where all the heavy data processing power should be housed!
#So this is to me the most critical part of this app.

#This might be a particularly critical part of the product


def main():
       ofile = raw_input('File read> ')
       open_file(ofile)

def open_file(fi):
        pgn_text = open(fi).read()
        pgn_game = pgn.PGNGame(pgn_text)

        #print pgn.loads(pgn_text)
        print pgn.dumps(pgn_game)


if __name__=='__main__':
        main()
