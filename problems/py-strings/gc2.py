#!/usr/bin/env python3

import os
import sys
count_GCgc = 0

if len(sys.argv) <2:
        print('Usage: {} FILE'.format(os.path.basename(sys.argv[0])))
        exit(1)
if not os.path.isfile(sys.argv[1]):
        print('"{}" is not a file'.format(sys.argv[1]))
        sys.exit(1)
for line in open(sys.argv[1]):
	count_GCgc = 0
	for line in line.lower():
		if line in 'GCgc':
			count_GCgc +=1
	print('{}'.format(int(count_GCgc/len(sys.argv[1])*100)))
