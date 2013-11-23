#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem from the Armory problem area, 
which focuses on using prebuilt bioinformatics packages, in this case BioPython.

Problem Title: Complementing a Strand of DNA
Rosalind Armory ID: RVCO
Rosalind Armory #: 013
URL: http://rosalind.info/problems/rvco/
'''

from Bio import SeqIO

# This is very straight forward.
with open('data/armory/rosalind_rvco.txt') as input_data, open('output/armory/Armory_013_RVCO.txt', 'w') as output_data:
	# Check if the dna sequence matches its complement, add #Trues to get the number.
	rev_comp_match = sum([str(dna.seq) == str(dna.reverse_complement().seq) for dna in SeqIO.parse(input_data, 'fasta')])
	print rev_comp_match
	output_data.write(str(rev_comp_match))
