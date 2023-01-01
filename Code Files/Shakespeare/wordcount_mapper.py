#!/usr/bin/python3.10
# the above just indicates to use phthon to interpret this file

#-------------------------------------
#This mapper code transforms (a line of text) as an input to an output <word , 1>
#-------------------------



import sys
import itertools

# sys.stdin call 'sys' to read a line from standard input
# the 'line' is a string object
for line in sys.stdin:
    line = line.strip()
    keys = line.split()

    for key in keys:
        value = 1
        print('{0}\t{1}'.format(key, value))




"""
test = "123 456 789 101112\n45678918    193874918   "
print(test.strip())
"""