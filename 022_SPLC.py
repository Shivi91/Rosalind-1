#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: RNA Splicing
Rosalind ID: SPLC
Rosalind #: 022
URL: http://rosalind.info/problems/splc/
'''

from scripts import ReadFASTA, ProteinDictDNA

dna_list = ReadFASTA('data/rosalind_splc.txt')
exon = dna_list[0][1]

# Remove the introns.
for intron in dna_list[1:]:
	exon = exon.replace(intron[1], '')

# Translate the exons.
dna_dict = ProteinDictDNA()
exon_protein = ''
for index in range(0, len(exon), 3):
	exon_protein += dna_dict[exon[index:index+3]] if dna_dict[exon[index:index+3]]  != 'Stop' else ''

print exon_protein
with open('output/022_SPLC.txt', 'w') as output_data:
	output_data.write(exon_protein)
