#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Genome Assembly with Perfect Coverage
Rosalind ID: PCOV
Rosalind #: 070
URL: http://rosalind.info/problems/pcov/
'''

with open('data/rosalind_pcov.txt') as input_data:
	k_mers = [line.strip() for line in input_data.readlines()]

# Begin by constructing the De Bruijn Graph
DBG_edge_elmts = set()
for kmer in k_mers:
	DBG_edge_elmts.add(kmer)

# Create the edges of the Graph.
k = len(k_mers[0])
edge = lambda elmt: [elmt[0:k-1],elmt[1:k]]
DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]

# Construct the cyclic superstring from the edges. 
temp = DBG_edges.pop(0)
cyclic = temp[0][-1]
while DBG_edges != []:
	cyclic += temp[1][-1]
	[index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp[1]]
	temp = DBG_edges.pop(index)

# Print and save the output.
print cyclic
with open('output/070_PCOV.txt', 'w') as output_file:
	output_file.write(cyclic)
