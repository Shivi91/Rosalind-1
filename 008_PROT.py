#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Translating RNA into Protein
Rosalind ID: PROT
Rosalind #: 008
URL: http://rosalind.info/problems/prot/
'''

from scripts import ProteinDictRNA

with open('data/rosalind_prot.txt') as input_data:
	s = input_data.read().rstrip('\n')

# Dictionary translating RNA to Protein
rna_dict = ProteinDictRNA()

s_protein = ''
for i in range(0,len(s),3):
    if rna_dict[s[i:i+3]] != 'Stop':
        s_protein+= rna_dict[s[i:i+3]]

print s_protein

with open('output/008_PROT.txt', 'w') as output_data:
	output_data.write(s_protein)
