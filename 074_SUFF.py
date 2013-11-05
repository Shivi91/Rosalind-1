#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Encoding Suffix Trees
Rosalind ID: SUFF
Rosalind #: 074
URL: http://rosalind.info/problems/suff/
'''

from scripts import SuffixTree

with open('data/rosalind_suff.txt') as input_data:
	s = input_data.read().strip()

# Most of the work is done in the Data Structures script.
suff = SuffixTree()
suff.addWord(s)

with open('output/074_SUFF.txt', 'w') as output_data:
	output_data.write('\n'.join(suff.edges.values()))
