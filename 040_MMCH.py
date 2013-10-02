#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Maximum Matchings and RNA Secondary Structures 
Rosalind ID: MMCH
Rosalind #: 040
URL: http://rosalind.info/problems/mmch/
'''

from math import factorial
from scripts import ReadFASTA

def nPr(n, k):
	'''Returns the number of k-pernumatations of n.'''
	return factorial(n)/factorial(n-k)

rna = ReadFASTA('data/rosalind_mmch.txt')[0][1]

# Counts the number of each times each nucleotide appears in the RNA string.
AU_num = [rna.count(nucleotide) for nucleotide in 'AU']
GC_num = [rna.count(nucleotide) for nucleotide in 'GC']

# There are nPr(max, min) edges for each AU, CG.  Total number of edges is then the product.
max_matchings = nPr(max(AU_num), min(AU_num))*nPr(max(GC_num), min(GC_num))

print max_matchings
with open('output/040_MMCH.txt', 'w') as output_data:
	output_data.write(str(max_matchings))
