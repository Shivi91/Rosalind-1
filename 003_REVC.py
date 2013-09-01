#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Complementing a Strand of DNA
Rosalind ID: REVC
Rosalind #: 003
URL: http://rosalind.info/problems/revc/
'''

from string import maketrans 

input_file = open('data/rosalind_revc.txt')
dna = input_file.read()
input_file.close()

nucleotide = 'ATCG'
complement = 'TAGC'
transtab = maketrans(nucleotide, complement)

dna_reverse_complement = dna.translate(transtab)[::-1].lstrip()

output_file = open('output/003_REVC.txt', 'w')
output_file.write(dna_reverse_complement)
output_file.close()
