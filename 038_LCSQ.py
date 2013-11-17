#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding a Shared Spliced Motif
Rosalind ID: LCSQ
Rosalind #: 038
URL: http://rosalind.info/problems/lcsq/
'''

from numpy import zeros
from scripts import ReadFASTA

def longest_common_subsequence(dna1, dna2):
	'''Returns the longest longest common subsequence of dna1 and dna2.'''
	# Compute each entry of M.
	M = zeros((len(dna1)+1,len(dna2)+1))
	for i in xrange(len(dna1)):
		for j in xrange(len(dna2)):
			if dna1[i] == dna2[j]:
				M[i+1][j+1] = M[i][j]+1
			else:
				M[i+1][j+1] = max(M[i+1][j],M[i][j+1])

	# Recover a maximum substring.
	longest_sseq = ''
	i,j = len(dna1), len(dna2)
	while i*j != 0:
		if M[i][j] == M[i-1][j]:
			i -= 1
		elif M[i][j] == M[i][j-1]:
			j -= 1
		else:
			longest_sseq = dna1[i-1] + longest_sseq
			i -= 1
			j -= 1

	return longest_sseq

if __name__ == '__main__':
	# Read FASTA DNA sequences.
	dna1, dna2 = [fasta[1] for fasta in ReadFASTA('data/rosalind_lcsq.txt')]
	
	# Solve the problem
	lcsq = longest_common_subsequence(dna1,dna2)

	# Print and save the output.
	print lcsq
	with open('output/038_LCSQ.txt', 'w') as output_file:
		output_file.write(lcsq)
