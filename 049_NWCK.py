#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Distances in Trees
Rosalind ID: NWCK
Rosalind #: 049
URL: http://rosalind.info/problems/nwck/
'''

from scripts import Newick

with open('data/rosalind_nwck.txt') as input_data:
	trees = [line.split('\n') for line in input_data.read().strip().split('\n\n')]

# The majority of the work is done by the Newick class in the Data Structures script.
distances = [str(Newick(tree[0]).distance(*tree[1].split())) for tree in trees]

# Print and save the answer.
print ' '.join(distances)
with open('output/049_NWCK.txt', 'w') as output_data:
	output_data.write(' '.join(distances))
