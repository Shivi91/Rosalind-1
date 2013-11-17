#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Wobble Bonding and RNA Secondary Structures
Rosalind ID: RNAS
Rosalind #: 064
URL: http://rosalind.info/problems/rnas/
'''

def wobble_bonding(rna):
	'''Returns the number of noncrossing bonding graphs for a given RNA sequence.'''
	if len(rna) <= 3:
		# Only one possible way to match if the length is at most one.
		return 1

	else:
		# If we've already computed the value, return it!
		if rna in wobble_dict:
			return wobble_dict[rna]
		# Otherwise, calculate the value, add it to the dictionary, and return it.
		else:
			subintervals = []
			for i in xrange(4, len(rna)):
				if rna[0] in matchings[rna[i]]:
					subintervals.append([rna[1:i],rna[i+1:]])

			# Reduce the problem to noncrossing matchings over the matching substrings, and the matchings for the next starting point.
			wobble_dict[rna] =  (sum([wobble_bonding(subint[0])*wobble_bonding(subint[1]) for subint in subintervals]) + wobble_bonding(rna[1:]))
			
			return wobble_dict[rna]


with open('data/rosalind_rnas.txt') as input_data:
	rna = input_data.read().strip()

matchings = {'A':'U', 'U':'AG', 'C':'G', 'G':'CU'}
wobble_dict = {}
wobble = wobble_bonding(rna)

print wobble
with open('output/064_RNAS.txt', 'w') as output_file:
	output_file.write(str(wobble))
