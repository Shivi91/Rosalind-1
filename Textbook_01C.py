#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Pattern Matching Problem
Chapter #: 01
Problem ID: C 
URL: http://rosalind.info/problems/1c/
'''

with open('data/textbook/rosalind_1c.txt') as input_data:
	pattern, text = [line.strip() for line in input_data.readlines()]

pattern_loc = []
for i in xrange(len(text)-len(pattern)+1):
	if text[i:i+len(pattern)] == pattern:
		pattern_loc.append(str(i))

print ' '.join(pattern_loc)
with open('output/textbook/Textbook_01C.txt', 'w') as output_data:
	output_data.write(' '.join(pattern_loc))
