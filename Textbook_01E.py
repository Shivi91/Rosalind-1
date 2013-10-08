#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Minimum Skew Problem
Chapter #: 01
Problem ID: E
URL: http://rosalind.info/problems/1e/
'''

with open('data/textbook/rosalind_1e.txt') as input_data:
	dna = input_data.read().strip()

skew_value, min_skew, min_ind = 0, 1, []
for index, nucleotide in enumerate(dna):
	# Determine the skew value.
	if nucleotide == 'C':
		skew_value -= 1
	elif nucleotide == 'G':
		skew_value += 1
	# Check if it matches the current minimum, or is a new minimum.
	if skew_value == min_skew:
		min_ind.append(str(index+1))
	elif skew_value < min_skew:
		min_skew = skew_value
		min_ind = [str(index+1)]

print ' '.join(min_ind)
with open('output/textbook/Textbook_01E.txt', 'w') as output_data:
	output_data.write(' '.join(min_ind))
