#!/usr/bin/env python3

import sys

if len(sys.argv) <2:
	print('Usage:', sys.argv[0], 'STRING')
	sys.exit(1)
else:
	num_vowels = 0
	for char in sys.argv[1]:
		if char in 'aeiou':
			num_vowels = num_vowels + 1
	if num_vowels == 1:
		print('There is',num_vowels,'vowel in','"{}."'.format(sys.argv[1]))
	else:
		num_vowels = 0
		for char in sys.argv[1]:
			if char in 'aeiou':
				num_vowels = num_vowels + 1
		if num_vowels >=2:
			print('There are',num_vowels,'vowels in','"{}."'.format(sys.argv[1]))
		else:
			for char in sys.argv[1]:
				if char in 'aeiou':
					num_vowels = num_vowels + 1
			if num_vowels == 0:
				print('There are',num_vowels,'vowels in','"{}."'.format(sys.argv[1]))

