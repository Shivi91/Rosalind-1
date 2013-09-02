#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Computing GC Content
Rosalind ID: GC
Rosalind #: 005
URL: http://rosalind.info/problems/gc/
'''

from scripts import ReadFASTA

# Our data is in FASTA form.
dna_list = ReadFASTA('data/rosalind_gc.txt')

highest_GC = -1
highest_GC_name = ''
for index, dna_seq in enumerate(dna_list):
    GC_count = 0
    for nucleotide in dna_seq[1]:
        if nucleotide == 'G' or nucleotide == 'C':
            GC_count += 1
            
    GC_amount = ( (GC_count*100.0)/len(dna_seq[1]) )
    if GC_amount > highest_GC:
        highest_GC = GC_amount
        highest_GC_name = dna_list[index][0]


# Print the solution.
print highest_GC_name, '\n', highest_GC

# Write the solution to a text file.
output_file = open('output/005_GC.txt', 'w')
output_file.writelines([str(highest_GC_name),'\n', str(highest_GC)])
output_file.close()
