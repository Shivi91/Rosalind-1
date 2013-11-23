#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem from the Armory problem area, 
which focuses on using prebuilt bioinformatics packages, in this case BioPython.

Problem Title: Finding Genes with ORFs
Rosalind Armory ID: ORFR
Rosalind Armory #: 015
URL: http://rosalind.info/problems/orfr/
'''

from Bio.Alphabet import IUPAC
from Bio.Seq import Seq, translate
from re import finditer

with open('data/armory/rosalind_orfr.txt') as input_data:
	dna = Seq(input_data.read().strip(),IUPAC.unambiguous_dna)

# Get the starting position for each ORF in the dna sequence and translate.
ORFs = [translate(dna[x.start():], table = 1, stop_symbol = '', to_stop= True) for x in finditer('ATG', str(dna))]
# Get the starting position for each ORF in the reverse complement sequence and translate.
ORFs += [translate(dna.reverse_complement()[x.start():], table = 1, stop_symbol = '', to_stop= True) for x in finditer('ATG', str(dna.reverse_complement()))]

# Find the longest ORF.
longest_orf = max(map(str, ORFs), key=len)

# Print and save the answer.
print longest_orf
with open('output/armory/Armory_015_ORFR.txt', 'w') as output_data:
	output_data.write(longest_orf)
