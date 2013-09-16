#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Complementing a Strand of DNA
Rosalind ID: REVC
Rosalind #: 003
URL: http://rosalind.info/problems/revc/
'''

from string import maketrans 

with open('data/rosalind_revc.txt') as input_data:
	dna = input_data.read()

nucleotide = 'ATCG'
complement = 'TAGC'
transtab = maketrans(nucleotide, complement)
dna_reverse_complement = dna.translate(transtab)[::-1].lstrip()

with open('output/003_REVC.txt', 'w') as output_data:
	output_data.write(dna_reverse_complement)
