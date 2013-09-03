#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Translating RNA into Protein
Rosalind ID: PROT
Rosalind #: 008
URL: http://rosalind.info/problems/prot/
'''

from scripts import RNA_to_Protein_Dict

file1 = open('data/rosalind_prot.txt')
s = file1.read().rstrip('\n')
file1.close()

# Dictionary translating RNA to Protein
rna_dict = RNA_to_Protein_Dict()

s_protein = ''
for i in range(0,len(s),3):
    if rna_dict[s[i:i+3]] != 'Stop':
        s_protein+= rna_dict[s[i:i+3]]

print s_protein

output_file = open('output/008_PROT.txt', 'w')
output_file.write(s_protein)
output_file.close()
