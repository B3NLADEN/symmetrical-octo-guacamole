#!/usr/bin/python

import sys

def print5times(line2print):
    for count in range(5):
        print line2print


print5times(sys.argv[1])  



