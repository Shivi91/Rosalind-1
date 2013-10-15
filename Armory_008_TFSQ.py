#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem from the Armory problem area, 
which focuses on using prebuilt bioinformatics packages, in this case BioPython.

Problem Title: FASTQ format introduction
Rosalind Armory ID: TFRQ
Rosalind Armory #: 008
URL: http://rosalind.info/problems/tfrq/
'''

from Bio import SeqIO

with open('data/armory/rosalind_tfsq.txt') as input_data, open('output/armory/Armory_008_TFSQ.txt', 'w') as output_data:
	SeqIO.convert(input_data, 'fastq', output_data, 'fasta' )
