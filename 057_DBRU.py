#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Constructing a De Bruijn Graph
Rosalind ID: DBRU
Rosalind #: 057
URL: http://rosalind.info/problems/dbru/
'''

from scripts import ReverseComplementDNA as RevComp

with open('data/rosalind_dbru.txt') as input_data:
	k_mers = [line.strip() for line in input_data.readlines()]

# Get the edge elements.
DBG_edge_elmts = set()
for kmer in k_mers:
	DBG_edge_elmts.add(kmer)
	DBG_edge_elmts.add(RevComp(kmer))

# Create the edges.
k = len(k_mers[0])
edge = lambda elmmt: '('+elmt[0:k-1]+', '+elmt[1:k]+')'
DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]

# Write and save the adjacency list.
print '\n'.join(DBG_edges)
with open('output/057_DBRU.txt', 'w') as output_file:
	output_file.write('\n'.join(DBG_edges))
