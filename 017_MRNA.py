#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Inferring mRNA from Protein
Rosalind ID: MRNA
Rosalind #: 017
URL: http://rosalind.info/problems/mrna/
'''

from scripts import RNA_to_Protein_Dict

file1 = open('data/rosalind_mrna.txt')
protein = file1.read().strip()
file1.close()

# Dictionary translating RNA to Protein
rna_dict = RNA_to_Protein_Dict()
rna_num = rna_dict.values().count('Stop')

for p in protein:
    rna_num = rna_num * rna_dict.values().count(p) % 1000000

print rna_num
