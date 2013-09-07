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

output_file = open('output/012_GRPH.txt', 'w')
line_written = False

for i in range(len(dna_list)):
    checklist = range(len(dna_list))
    checklist.remove(i)
    for j in checklist:
        if  dna_list[i][1][len(dna_list[i][1])-3:len(dna_list[i][1])] == dna_list[j][1][0:3]:
            # Display the names of the adjacent DNA strands.
            print dna_list[i][0], dna_list[j][0]
            # Save the adjancent strand names to an output file.
            # No new line preceeding the first entry of output file.
            if not line_written:
                output_file.write(dna_list[i][0]+' '+dna_list[j][0])
                line_written = True
            else:
                output_file.write('\n'+dna_list[i][0]+' '+dna_list[j][0])
        
output_file.close()
