#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem from the Armory problem area, 
which focuses on using prebuilt bioinformatics packages, in this case BioPython.

Problem Title: Introduction to the Bioinformatics Armory
Rosalind Armory ID: INI
Rosalind Armory #: 001
URL: http://rosalind.info/problems/ini/
'''

from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

with open('data/armory/rosalind_ini.txt') as input_data:
	dna = Seq(input_data.read().strip(),IUPAC.unambiguous_dna)

dna_count = [str(dna.count(nucleotide)) for nucleotide in 'ACGT']

print ' '.join(dna_count)
with open('output/armory/Armory_001_INI.txt', 'w') as output_data:
	output_data.write(' '.join(dna_count))
