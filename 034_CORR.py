#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Error Correction in Reads
Rosalind ID: CORR
Rosalind #: 034
URL: http://rosalind.info/problems/corr/
'''

from scripts import ReadFASTA, ReverseComplementDNA as RevComp, HammingDistance as Hamm

# Group together identical DNA sequences, up to reverse complement.
dna_groups = []
for dna in [fasta[1] for fasta in ReadFASTA('data/rosalind_corr.txt')]:
	in_group = False
	for index, group in enumerate(dna_groups):
		if dna in group or RevComp(dna) in group:
			dna_groups[index].append(dna)
			in_group = True
			break

	if not in_group:
		dna_groups.append([dna])

# Sort the DNA groups as either being a correct read in index 0, or incorrect read in index 1.
dna_groups = [[],[]]+dna_groups
while len(dna_groups)>2:
	if len(dna_groups[len(dna_groups)-1]) > 1:
		# Convert to set to eliminate repeats.
		dna_groups[0].append(dna_groups.pop(len(dna_groups)-1))
	else:
		dna_groups[1] += dna_groups.pop(len(dna_groups)-1)

# Correct read errors.
corrections = []
for error in dna_groups[1]:
	for group in dna_groups[0]:
		if Hamm(error, group[0]) == 1:
			corrections.append(error+'->'+group[0])
			break
		elif Hamm(error, RevComp(group[0])) == 1:
			corrections.append(error+'->'+RevComp(group[0]))
			break

# Print and write output.
print '\n'.join(corrections)
with open('output/034_CORR.txt', 'w') as output_data:
	output_data.write('\n'.join(corrections))
