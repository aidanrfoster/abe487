#!/usr/bin/env python3

import os
import sys

if len(sys.argv[1:]) < 2:
	print('Usage: requires two str')
	sys.exit(1)

count = []
s = sys.argv[1]
t = sys.argv[2]

for codon in range(len(s)):
	if s[codon:codon +len(t)] == t: 
		count.append(codon +1) 

if count:
	print(*count, sep=' ')
if not count:
	print('Not found')
