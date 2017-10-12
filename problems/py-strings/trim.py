#!/usr/bin/env python3

import os
import sys

if len(sys.argv) <2:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        exit(1)

if len(sys.argv) == 2:
	if os.path.isfile(sys.argv[1]):
		for letter in open(sys.argv[1]):
			for letter in letter.upper().split():
				if len(letter) > 5:
					print(letter[:5])
	else:
		args = sys.argv[1]
		if len(sys.argv[1]) > 5:
			print(args[:5])
if len(sys.argv) == 3:
	trim = int(sys.argv[2])
	if os.path.isfile(sys.argv[1]):
		for letter in open(sys.argv[1]):
			for letter in letter.upper().split():
				if len(letter) > trim:
					print(letter[:trim])
	else:
		if not os.path.isfile(sys.argv[1]):
			args = sys.argv[1]
			if len(args) > trim:
				print(args[:trim])

