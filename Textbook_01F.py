#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Approximate Pattern Matching Problem
Chapter #: 01
Problem ID: F
URL: http://rosalind.info/problems/1f/
'''

with open('data/textbook/rosalind_1f.txt') as input_data:
	pattern, dna, n = [line.strip() if index != 2 else int(line.strip()) for index, line in enumerate(input_data.readlines())]

approx_match = []
for i in xrange(len(dna)-len(pattern)+1):
	mismatch_count = 0
	for j in xrange(len(pattern)):
		if dna[i:i+len(pattern)][j] != pattern[j]:
			mismatch_count += 1
	
	if mismatch_count <= n:
		approx_match.append(str(i))

print ' '.join(approx_match)
with open('output/textbook/Textbook_01F.txt', 'w') as output_data:
	output_data.write(' '.join(approx_match))
