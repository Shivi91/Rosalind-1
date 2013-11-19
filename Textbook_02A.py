#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Protein Translation Problem
Chapter #: 02
Problem ID: A
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/How-Do-Bacteria-Make-Antibiotics-96/#step-3
'''

# This is a repeat of Rosalind Problem 008: Translating RNA into Protein.
from scripts import ProteinDictRNA

with open('data/textbook/rosalind_2a.txt') as input_data:
	s = input_data.read().strip()

# Dictionary translating RNA to Protein
rna_dict = ProteinDictRNA()

s_protein = ''
for i in range(0,len(s),3):
    if rna_dict[s[i:i+3]] != 'Stop':
        s_protein += rna_dict[s[i:i+3]]

print s_protein

with open('output/textbook/Textbook_02A.txt', 'w') as output_data:
	output_data.write(s_protein)
