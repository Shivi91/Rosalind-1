#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Interleaving Two Motifs
Rosalind ID: SCSP
Rosalind #: 050
URL: http://rosalind.info/problems/scsp/
'''

# Need to do an unsual import since the name beings with an integer.
LCSQ = __import__('038_LCSQ')

# Read in the input data.
with open('data/rosalind_scsp.txt') as input_data:
	dna1, dna2 = [line.strip() for line in input_data.readlines()]

# Get the longest common subsequnce of dna1 and dna2.
lcsq = LCSQ.longest_common_subsequence(dna1,dna2)

# Initialize variables.
superseq = ['']*(len(lcsq)+1)
dna1_index = dna2_index = 0

# Insert non-longest_common_subsequence symbols while preserving the symbol order to get the shortest common supersequence.
for i in xrange(len(lcsq)+1):
	if i == len(lcsq):
		# If on the last step, add the remaining terms and combine the supersequence.
		superseq[len(lcsq)] = dna1[dna1_index:]+dna2[dna2_index:]
		superseq = ''.join(superseq)
	else:
		# Increment the DNA indicies while each corresponding character is not equal to the ith character of the longest subsequence.
		# Append the unequal characers.
		while dna1[dna1_index] != lcsq[i] and dna1_index < len(dna1):
			superseq[i] += dna1[dna1_index]
			dna1_index += 1
		while dna2[dna2_index] != lcsq[i] and dna2_index < len(dna2):
			superseq[i] += dna2[dna2_index]
			dna2_index += 1
		# Add the ith character from the longest common subsequence, increment the DNA sequences.
		superseq[i] += lcsq[i]
		dna1_index += 1
		dna2_index += 1

# Print and save the output.
print superseq
with open('output/050_SCSP.txt', 'w') as output_file:
	output_file.write(superseq)
