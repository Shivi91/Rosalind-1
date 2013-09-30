#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: k-Mer Composition
Rosalind ID: KMER
Rosalind #: 036
URL: http://rosalind.info/problems/kmer/
'''

from itertools import product
from scripts import ReadFASTA

dna = ReadFASTA('data/rosalind_kmer.txt')[0][1]

# Get a list of all 4-mers in lexiographic order.
kmer_list =  [''.join(kmer) for kmer in list(product('ACGT', repeat = 4))]

# Initialize the count of each 4-mer at zero for each 4-mer.
kmer_count = [0]*(4**4)

# Count each 4-mer
for i in range(len(dna)-3):
	kmer_count[kmer_list.index(dna[i:i+4])] += 1

print ' '.join(map(str,kmer_count))
with open('output/036_KMER.txt', 'w') as output_data:
	output_data.write(' '.join(map(str,kmer_count)))
