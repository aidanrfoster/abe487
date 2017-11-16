#!/usr/bin/env python3

import os
import sys
import argparse

# --------------------------------------------------
def get_args():

	parser = argparse.ArgumentParser(description='Parse Blast Into Tabular')
	parser.add_argument('tab', metavar='tab', help='Blast Tab Output')
	parser.add_argument('-p', '--pct_id', help='Percent_ID',
		metavar='float', type=float, default=0.0)
	parser.add_argument('-e', '--evalue', help='Maximum E_value',
		metavar='float', type=float, default=1.0)

	return parser.parse_args()

# --------------------------------------------------
def main():

	args = get_args()
	blast_csv = args.tab
	percent_ID = args.pct_id
	E_value = args.evalue
	fields = 'qseqid sseqid pident length mismatch gapopen qstart qend sstart send e_value bitscore'.split()


	for line in open(blast_csv):
		row = dict(zip(fields, line.split('\t')))
		if float(row['pident']) >= percent_ID: 
			if float(row['e_value']) <= E_value:
				print('{}\t{}\t{}\t{}'.format(row['qseqid'], row['sseqid'], 
					row['pident'], row['e_value']))   
    
# --------------------------------------------------
if __name__ == '__main__':
	main()
