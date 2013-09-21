#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Open Reading Frames
Rosalind ID: ORF
Rosalind #: 018
URL: http://rosalind.info/problems/orf/
'''

from scripts import ReadFASTA, DNA_to_RNA, ReverseComplementRNA, RNA_to_Protein_Dict

dna = ReadFASTA('data/rosalind_orf.txt')
rna_list = [DNA_to_RNA(dna[0][1])]
rna_list.append(ReverseComplementRNA(rna_list[0]))
rna_dict = RNA_to_Protein_Dict()

# Use a set since we want to return distinct protein.
# Sets keep track of distinct elements without us needing to worry about adding duplicates.
protein_orf = set()
for rna in rna_list:
	for i in range(len(rna)-2):
		# Check for the Start codon.
		if rna[i:i+3] == 'AUG':
			# Use a new index since we'll want to return to the ith position of the strand in case there are multiple start codons in a row.
			j = i
			current_protein = ''
			# Continue, if necessary, until we hit the end of the rna sequence.
			while j+3 < len(rna)-1:
				# Add the protein and break if we hit a Stop codon.
				if rna_dict[rna[j:j+3]] == 'Stop':
					protein_orf.add(current_protein)
					break
				# Otherwise, add to the current protein.
				else:
					current_protein += rna_dict[rna[j:j+3]]
				j += 3

# Convert protein from a set to list of strings to allow output to be written in the correct form more efficiently.
protein_orf = map(str, protein_orf)

with open('output/018_ORF.txt', 'w') as output_data:
	output_data.write(protein_orf[0])
	for protein in protein_orf[1:]:
		output_data.write('\n'+protein)
