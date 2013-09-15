#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Enumerating k-mers Lexicographically
Rosalind ID: LEXF
Rosalind #: 023
URL: http://rosalind.info/problems/lexf/
'''

from itertools import product

# Read and parse the input data.
with open('data/rosalind_lexf.txt') as input_data:
	letters, n = input_data.readlines()
	letters = ''.join(letters.split())
	n = int(n)

# The itertools.product function does exactly what we want.
# No use reinventing the wheel...
k_mers = [''.join(item) for item in product(letters, repeat=n)]

# Write the answer to the output file in the proper format.
with open('output/023_LEXF.txt', 'w') as output_file:
	output_file.write(k_mers[0])
	for item in k_mers[1:]:
		output_file.write('\n'+item)
