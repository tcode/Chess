#!/usr/bin/env python

#This is where all the heavy data processing power should be housed!
#So this is to me the most critical part of this app.

#This might be a particularly critical part of the product


def main():
        fi = raw_input('please enter your desired file> ')
        f = open(fi, 'r') 
        data = f.read()
        print data

        #to have a reprensentation of the moves you got to have a way to 
        #structure the board in memory.
        #and while you do that, you might as well do bitboards 
        #that identifies wether a certain piece is at a certain 
        #sqaure.

        """
        I would forinstance think that a board of 8x8 or 12x12 several times could be advantageus since then you have
        to only write a lot less in terms of algorithms for figuring out where exactly the different pieces are

        However there can be a certain pitfall in this as it might burn a lot of memory.
        """
        # This was written in 25 minutes about, and now it is about time for a little break to figure
        # out how the rest of my code should be structured to fit in with my overall scheme....





if __name__=='__main__':
        main()
