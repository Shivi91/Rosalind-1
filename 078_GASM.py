#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Genome Assembly with Perfect Coverage
Rosalind ID: GASM
Rosalind #: 078
URL: http://rosalind.info/problems/gasm/
'''

from scripts import ReverseComplementDNA as RevComp

with open('data/rosalind_gasm.txt') as input_data:
	k_mers = [line.strip() for line in input_data.readlines()]

# We don't know which k value gives exactly two directed cycles, so iterate until we find the right value.
for kval in xrange(1,len(k_mers[0])):
	# Begin by constructing the De Bruijn Graph 
	DBG_edge_elmts = set()
	for kmer in k_mers:
		for i in xrange(kval):
			DBG_edge_elmts.add(kmer[i:len(kmer)+i-kval+1])
			DBG_edge_elmts.add(RevComp(kmer[i:len(kmer)-kval+i+1]))

	# Create the edges of the Graph.
	k = len(list(DBG_edge_elmts)[0])
	edge = lambda elmmt: [elmt[0:k-1],elmt[1:k]]
	DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]

	# Construct the cyclic superstrings from the edges. 
	cyclics = []
	for repeat in xrange(2):
		temp_kmer = DBG_edges.pop(0)
		cyclic = temp_kmer[0][-1]
		while temp_kmer[1] in [item[0] for item in DBG_edges]:
			cyclic += temp_kmer[1][-1]
			[index] = [i for i, pair in enumerate(DBG_edges) if pair[0] == temp_kmer[1]]
			temp_kmer = DBG_edges.pop(index)
		cyclics.append(cyclic)

	# Break if we've found exactly two directed cycles.
	if len(DBG_edges) == 0:
		break

# Print and save the output.
print cyclics[0]
with open('output/078_GASM.txt', 'w') as output_file:
	output_file.write(cyclics[0])
