#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Calculating Protein Mass
Rosalind ID: PRTM
Rosalind #: 020
URL: http://rosalind.info/problems/prtm/
'''

from scripts import Protein_Weight_Dict

# Load the data.
file1 = open('data/rosalind_prtm.txt')
protein_str = file1.read().strip()
file1.close()

# Load the dictionary that translates protein to monoisotipic weight.
weight_dict = Protein_Weight_Dict()

# Calculate the weight protein by protein.
monoisotopic_weight = 0
for protein in protein_str:
	monoisotopic_weight += weight_dict[protein]


# Print and save the weight.
print monoisotopic_weight
output_file = open('output/020_PRTM.txt', 'w')
output_file.write(str(monoisotopic_weight))
output_file.close()