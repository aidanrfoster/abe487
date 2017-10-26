#!/usr/bin/env python3

import os
import sys

args= sys.argv[1:]

if len(args) != 1:
	print('Usage: prot.py SEQ')
	sys.exit(1)

if len(args) == 1:
	with open('codons.rna') as f:
		AA_code = {}	
		for line in f:
			(key, value) = line.split()
			if key in AA_code:
				AA_code[key].append(value)
			else:
				AA_code[key] = value

	seq = (args[0].upper())
	k = 3
	protein = []	
	for bases in range(0, len(seq), k):
		if seq[bases:bases+k] in AA_code:
			protein.append(AA_code[seq[bases:bases+k]])

print(''.join(protein))


