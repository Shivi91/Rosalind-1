#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Inferring Protein from Spectrum
Rosalind ID: SPEC
Rosalind #: 053
URL: http://rosalind.info/problems/spec/
'''

from scripts import ProteinWeightDict

# The only major issue is that the given values aren't as precise as those in the table.
# Need to find the closest match (or rewrite the weight dictionary with less precision).
with open('data/rosalind_spec.txt') as input_data:
	masses = [float(line.strip()) for line in input_data.readlines()]

# Load a list of (protein, weight) pairs.
weight_list = ProteinWeightDict().items()

# Gives the difference between a given weight and the protein at position i in the weight list.
weight_diff = lambda (i, weight): abs(weight - weight_list[i][1])

# Returns the protein whose mass is closest to specified weight.
closest_prot = lambda weight: weight_list[min(zip(range(len(weight_list)), [weight]*len(weight_list)), key=weight_diff)[0]][0]

# Determine each protein.
prot = [closest_prot(masses[i+1]-masses[i]) for i in range(len(masses)-1)]

# Concatonate to get the desired protein.
print ''.join(prot)
with open('output/053_SPEC.txt', 'w') as output_data:
	output_data.write(''.join(prot))
