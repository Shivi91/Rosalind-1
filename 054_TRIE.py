#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Introduction to Pattern Matching
Rosalind ID: TRIE
Rosalind #: 054
URL: http://rosalind.info/problems/trie/
'''

from scripts import Trie

with open('data/rosalind_trie.txt') as input_data:
	dna = [line.strip() for line in input_data.readlines()]

# The heavy lifting is done by the Trie class in the Data Structures script.
myTrie = Trie(dna)
adjacency_list = [edge.getInfo() for edge in myTrie.edges]

print '\n'.join(adjacency_list)
with open('output/054_TRIE.txt', 'w') as output_file:
	output_file.write('\n'.join(adjacency_list))