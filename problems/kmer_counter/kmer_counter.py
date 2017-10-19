#!/usr/bin/env python3

import os
import sys
from collections import defaultdict
from collections import Counter

args = sys.argv[1:]

if len(args) != 2:
	print('Usage: kmer_counter.py LEN STR')
	exit(1)

if len(args) == 2:
	if not args[0].isdigit():
		print('Kmer size "{}" is not a number' .format(args[0]))
		sys.exit(1)
	if int(args[0]) <= 0:
		print('Kmer size "{}" must be > 0' .format(args[0]))
		sys.exit(1)
	if int(args[0]) > len(args[1]):
		print('There are no {}-mers in "{}"' .format(args[0],args[1]))
		sys.exit(1)

seq = args[1]
kmer_len = int(args[0])
kmer = len(seq) - int(args[0]) +1
inp = defaultdict(int)

for bases in range(kmer):
	kmer_range = seq[bases:bases+kmer_len]
	inp[kmer_range] += 1

print(seq)
for key, value in sorted(inp.items()):
	print(key, value)
