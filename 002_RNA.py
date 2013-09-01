#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Transcribing DNA into RNA
Rosalind ID: RNA
Rosalind #: 002
URL: http://rosalind.info/problems/rna/
'''

input_file = open('data/rosalind_rna.txt')
dna = input_file.read().strip()
input_file.close()


output_file = open('output/002_RNA.txt', 'w')
output_file.write(dna.replace('T', 'U'))
print dna.replace('T', 'U')
output_file.close()



