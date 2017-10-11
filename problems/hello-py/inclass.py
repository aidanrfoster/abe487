#!/usr/bin/env python3

import sys
import os

names = sys.argv[1:]

if len(args) <1:
	print('usage {} NAME'.format(os.path.basename(sys.argv[0])))
	sys.exit(1)

print('Names is "{}"'.format(','.join(names)))

num_people = len(names)

if num_people == 1:
	print('hello to the 1 of you: ' + names[0])
elif num_people ==2:
	print('hello to the 2 of you: {} and {}
else: 
	gr
