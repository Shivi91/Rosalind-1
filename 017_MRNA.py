#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Inferring mRNA from Protein
Rosalind ID: MRNA
Rosalind #: 017
URL: http://rosalind.info/problems/mrna/
'''

from scripts import ProteinDictRNA

with open('data/rosalind_mrna.txt') as input_data:
	protein = input_data.read().strip()

# Dictionary translating RNA to Protein
rna_dict = ProteinDictRNA()
rna_num = rna_dict.values().count('Stop')

for p in protein:
    rna_num = rna_num * rna_dict.values().count(p) % 1000000

print rna_num
