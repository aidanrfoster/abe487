#!/usr/bin/env python3

import os
import sys
count_GCgc = 0

if len(sys.argv) <2:
	print('Usage: {} STRING'.format(os.path.basename(sys.argv[0])))
	exit(1)

for char in sys.argv[1]:
	if char in 'GCgc':
		count_GCgc +=1
print('{}% GC'.format(int(count_GCgc/len(sys.argv[1])*100)))	

