#!/usr/bin/env python3

import sys
import os

if len(sys.argv) <2:
	print('Usage:', sys.argv[0], 'NAME [NAME2 ...]')
	sys.exit(1)
elif len(sys.argv) ==2:
	print('Hello to the', len(sys.argv[1:]),'of you:','{}!'.format(sys.argv[1]))
elif len(sys.argv) ==3:
        print('Hello to the {} of you: {} and {}!' .format(len(sys.argv[1:]), sys.argv[1], sys.argv[2]))
elif len(sys.argv) >=3:
	print('Hello to the {} of you: {}, and {}!' .format(len(sys.argv[1:]), ', '.join(sys.argv[1:-1]), sys.argv[-1]))



