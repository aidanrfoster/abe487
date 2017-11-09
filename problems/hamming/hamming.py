#!/usr/bin/env python3

import sys
import os

args = sys.argv[1:]

if len(args) != 2:
        print('Usage: [string] [string]')
        sys.exit(1)


string1 = args[0]
string2 = args[1]
hamm_dist = 0
if len(string1) == len(string2):		
	seq= zip(string1,string2)
	for char1,char2 in seq:
		if char1 != char2:
			hamm_dist +=1
	print(hamm_dist)
	
if len(string1) != len(string2):
	string_diff = abs(len(string1) - len(string2))
	seq= zip(string1,string2)
	for char1,char2 in seq:
		if char1 != char2:
			hamm_dist +=1
	print(hamm_dist + string_diff)


