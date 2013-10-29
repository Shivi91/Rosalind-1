#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Comparing Spectra with the Spectral Convolution
Rosalind ID: CONV
Rosalind #: 055
URL: http://rosalind.info/problems/conv/
'''

with open('data/rosalind_conv.txt') as input_data:
	S1,S2 = [map(float,line.strip().split()) for line in input_data.readlines()]

# Create a dictionary to store each value in the spectral convolution multiset along with its count.
spectral_convolution = dict()
for s1 in S1:
	for s2 in S2:
		element = str(s1 - s2)
		if element in spectral_convolution:
			spectral_convolution[element] += 1
		else:
			spectral_convolution[element] = 1

# Get the maximum multiplicity from the spectral convolution.
max_multiplicty = max([val for val in spectral_convolution.values()])
# Get the keys corresponding to the maximum multiplicities.
max_x = [item[0] for item in spectral_convolution.items() if item[1] == max_multiplicty]

# Print and save the solution.
print str(max_multiplicty)+'\n'+max_x[0]
with open('output/055_CONV.txt', 'w') as output_file:
	output_file.write(str(max_multiplicty)+'\n'+max_x[0])
