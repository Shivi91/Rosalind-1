#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Consensus and Profile
Rosalind ID: SUBS
Rosalind #: 009
URL: http://rosalind.info/problems/subs/
'''

from numpy import zeros
from scripts import ReadFASTA

# Data is in FASTA form
dna_list = ReadFASTA('data/rosalind_cons.txt')

# Setup an array and count into the array
M = zeros((4,len(dna_list[0][1])), dtype = int)
snp_dict = {'A':0, 'C':1, 'G':2, 'T':3}
for dna in dna_list:
    for index, snp in enumerate(dna[1]):
        M[snp_dict[snp]][index] += 1

# Determine the consensus string
consensus = ''
to_snp = {0:'A', 1:'C', 2:'G', 3:'T'}
for i in range(0,len(dna_list[0][1])):
    maxval = [-1,-1]
    for j in range(0,4):
        if maxval[1] < M[j][i]:
            maxval = [j, M[j][i]]
    consensus += to_snp[maxval[0]]

# Format the count properly
consensus = [consensus, 'A:', 'C:', 'G:', 'T:']
for index, col in enumerate(M):
    for val in col:
        consensus[index+1] += ' '+str(val)

# Print and write the output
print '\n'.join(consensus)
with open('output/010_CONS.txt', 'w') as output_data: 
    output_data.write('\n'.join(consensus))
