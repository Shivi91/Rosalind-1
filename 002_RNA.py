#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Transcribing DNA into RNA
Rosalind ID: RNA
Rosalind #: 002
URL: http://rosalind.info/problems/rna/
'''

with open('data/rosalind_rna.txt') as input_data:
	dna = input_data.read().strip()

with open('output/002_RNA.txt', 'w') as output_data:
	output_data.write(dna.replace('T', 'U'))
	print dna.replace('T', 'U')
