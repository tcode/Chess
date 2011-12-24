#!/usr/bin/env python

#This is where all the heavy data processing power should be housed!
#So this is to me the most critical part of this app.

#This might be a particularly critical part of the product


def main():
        print "I am the data processing unit of this app!"
        fi = raw_input('please enter your desired file> ')
        f = open(fi, 'r') 
        data = f.read()
        print data



if __name__=='__main__':
        main()
