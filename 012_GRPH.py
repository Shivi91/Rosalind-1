#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Overlap Graphs
Rosalind ID: GRPH
Rosalind #: 012
URL: http://rosalind.info/problems/grph/
'''

from scripts import ReadFASTA

# Data is in FASTA form
dna_list = ReadFASTA('data/rosalind_grph.txt')

overlaps = []
for i in range(len(dna_list)):
    for j in filter(lambda j: j!=i, range(len(dna_list))):
        if  dna_list[i][1][-3:] == dna_list[j][1][0:3]:
            overlaps.append(dna_list[i][0]+' '+dna_list[j][0])

# Just for fun, the following list comprehension does the same thing in one line!
# overlaps2 = [dna_list[i][0]+' '+dna_list[j][0] for i in range(len(dna_list)) for j in range(len(dna_list)) if i!=j if dna_list[i][1][-3:] == dna_list[j][1][0:3]]

# Print and save the answer.
print '\n'.join(overlaps)
with open('output/012_GRPH.txt', 'w') as output_data:
    output_data.write('\n'.join(overlaps))
