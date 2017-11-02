#!/usr/bin/env python3
import argparse
import sys
from Bio import SeqIO
import os

#----------------------------------------------------

def get_args():
	parser = argparse.ArgumentParser(description='FASTA Read Trimmer')
	parser.add_argument('file', metavar='file', help='FASTA file')	
	parser.add_argument('-s', '--start', help='Start position',
		metavar='int', type=int, default=1)
	parser.add_argument('-e', '--end', help='End position',
		metavar='int', type=int, default=None)
	parser.add_argument('-m', '--min', help='Minimum length',
		metavar='int', type=int, default=0)
	parser.add_argument('-o', '--outfile', help='Output file',
		metavar='str', type=str, default='')

	return parser.parse_args()

#-----------------------------------------------------

def main():
	"""main"""
	args = get_args()
	start_pos = args.start
	end_pos = args.end
	low = args.min
	output = args.outfile
	file = args.file
	
	if start_pos > 0:
		start_pos -= 1

	if len(output) == 0:
		output = file + '.trimmed'

	out_fh = open(output, 'w')

	num_taken = 0
	with open(file) as handle:
		for record in SeqIO.parse(handle, "fasta"):
			seq = str(record.seq[start_pos:end_pos])
			if len(seq) >= low:
				num_taken += 1
				out_fh.write('\n'.join(['>' + record.id, seq, '']))
	print('Wrote {} sequence{} to "{}"'.format(num_taken,
		'' if num_taken == 1 else 's',
		output))

#-----------------------------------------------------

if __name__ == '__main__':
        main()

