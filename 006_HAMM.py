#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Point Mutations
Rosalind ID: HAMM
Rosalind #: 006
URL: http://rosalind.info/problems/hamm/
'''

from scripts import HammingDistance

with open('data/rosalind_hamm.txt') as input_data:
	s, t = [line.rstrip('\n') for line in input_data.readlines()]

count = HammingDistance(s,t)

print count
with open('output/006_HAMM.txt', 'w') as output_data:
	output_data.write(str(count))
