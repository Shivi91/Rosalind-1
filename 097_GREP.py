#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Genome Assembly with Perfect Coverage and Repeats
Rosalind ID: GREP
Rosalind #: 097
URL: http://rosalind.info/problems/grep/
'''

def coverings(s, edges, k):
	'''Generate all possible complete cycle coverings from the given edges.'''
	# Determine the possible next elements to add to the covering.
	add_on = [index for index, item in enumerate(edges) if item[0] == s[-k+1:]]

	# If there's nothing left to add, return the string if we have a perfect covering (no edges left).
	# If we don't have perfect covering, return an empty list, which gets removed when flattened.
	if len(add_on) == 0:
		return [s if edges == [] else []]
	# Otherwise, proceed with all possible coverings.
	else:
		return [coverings(s+edges[i][1][-1], edges[:i]+edges[i+1:], k) for i in add_on]

def flatten(lst):
	'''Unpacks nested lists as a generator.'''
	for element in lst:
		if isinstance(element, list):
			for subelement in flatten(element):
				yield subelement		
		else:
			yield element

if __name__ == '__main__':

	with open('data/rosalind_grep.txt') as input_data:
		k_mers = [line.strip() for line in input_data.readlines()]

	# Create the edges of the De Bruijn Graph.
	k = len(k_mers[0])
	edge = lambda elmt: [elmt[0:k-1],elmt[1:k]]
	DBG_edges = [edge(elmt) for elmt in k_mers[1:]]

	# Get the circular strings.  Flatten and cut the coverings output appropriately.
	# Initiate the coverings with k_mers[0] since we want the circular coverings to start with the first element.
	circular_strings = [circular[:len(k_mers)] for circular in set(flatten(coverings(k_mers[0], DBG_edges, k)))]

	# Print and save the output.
	print '\n'.join(circular_strings)
	with open('output/097_GREP.txt', 'w') as output_data:
		output_data.write('\n'.join(circular_strings))
