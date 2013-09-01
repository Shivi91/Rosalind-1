#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
URL: http://rosalind.info/problems/dna/
'''

input_file = open('data/rosalind_dna.txt')
dna = input_file.read()
input_file.close()

nuc_count = []
for nucleotide in ['A', 'C', 'G', 'T']:
	nuc_count.append(str(dna.count(nucleotide)))

print ' '.join(nuc_count)
