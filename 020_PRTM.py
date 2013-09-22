#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Calculating Protein Mass
Rosalind ID: PRTM
Rosalind #: 020
URL: http://rosalind.info/problems/prtm/
'''

from scripts import ProteinWeightDict

# Load the data.
file1 = open('data/rosalind_prtm.txt')
protein_str = file1.read().strip()
file1.close()

# Load the dictionary that translates protein to monoisotipic weight.
weight_dict = ProteinWeightDict()

# Calculate the weight protein by protein.
monoisotopic_weight = 0
for protein in protein_str:
	monoisotopic_weight += weight_dict[protein]


# Print and save the weight.
print monoisotopic_weight
with open('output/020_PRTM.txt', 'w') as output_data:
	output_data.write(str(monoisotopic_weight))
