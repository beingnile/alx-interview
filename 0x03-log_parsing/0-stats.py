import sys
import re

data = sys.stdin.readlines()
for pos, line in enumerate(data):
    line = line.rstrip('\n')
    stuff = line.split(" ")
    print('This is from the program')
    print(line)
    if pos == 9:
        print('Wazzuuh')
