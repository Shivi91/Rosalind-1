#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem from the Armory problem area, 
which focuses on using prebuilt bioinformatics packages, in this case BioPython.

Problem Title: Protein Translation
Rosalind Armory ID: PTRA
Rosalind Armory #: 010
URL: http://rosalind.info/problems/ptra/
'''

from Bio.Seq import translate, CodonTable

with open('data/armory/rosalind_ptra.txt') as input_data:
	coding_dna, protein = [line.strip() for line in input_data.readlines()]

for table_id in CodonTable.ambiguous_generic_by_id.keys():
	if translate(coding_dna, table = table_id, stop_symbol = '', to_stop=False) == protein:
		genetic_code_variant = str(table_id)
		break

print genetic_code_variant
with open('output/armory/Armory_010_PTRA.txt', 'w') as output_data:
	output_data.write(genetic_code_variant)
