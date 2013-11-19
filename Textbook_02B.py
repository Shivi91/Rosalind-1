#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Peptide Encoding Problem
Chapter #: 02
Problem ID: B
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/How-Do-Bacteria-Make-Antibiotics-96/#step-6
'''

from scripts import ProteinDictDNA
from scripts import ReverseComplementDNA as RevComp

with open('data/textbook/rosalind_2b.txt') as input_data:
	dna, peptide = [line.strip() for line in input_data.readlines()]

# Dictionary translating RNA to Protein
dna_dict = ProteinDictDNA()

encodings = []
for i in range(0,len(dna)-3*len(peptide)+1):
	# Get translate the current slice and its reverse complement to protein.
	dna_slice = dna[i:i+3*len(peptide)]
	proteins = [dna_dict[dna_slice[3*(j-1):3*j]]  for j in range(1,len(peptide)+1)]
	proteins_rc =[dna_dict[RevComp(dna_slice)[3*(j-1):3*j]]  for j in range(1,len(peptide)+1)] 
    
	# Check if either translation matches the peptide.
	if ''.join(proteins) == peptide or ''.join(proteins_rc) == peptide:
		encodings.append(dna_slice)

print '\n'.join(encodings)
with open('output/textbook/Textbook_02B.txt', 'w') as output_data:
	output_data.write('\n'.join(encodings))
