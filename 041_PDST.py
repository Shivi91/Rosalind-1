#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Creating a Distance Matrix
Rosalind ID: PDST
Rosalind #: 041
URL: http://rosalind.info/problems/PDST/
'''

from numpy import zeros
from scripts import ReadFASTA

dna_list = [fasta[1] for fasta in ReadFASTA('data/rosalind_pdst.txt')]

# All seqences have the same length.
dna_len = len(dna_list[0])

M = zeros((len(dna_list),len(dna_list)))
for i in range(len(dna_list)):
	for j in range(len(dna_list)):
		
		if i < j:
			for k in range(dna_len):
				if dna_list[i][k] != dna_list[j][k]:
					M[i][j] += 1.0/dna_len

		elif i > j:
			M[i][j] = M[j][i]

print M
with open('output/041_PDST.txt', 'w') as output_data:
	output_data.write(' '.join(map(str,M[0])))
	for row in range(1, len(dna_list)):
		output_data.write('\n'+(' '.join(map(str,M[row]))))
