#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Introduction to Random Strings
Rosalind ID: PROB
Rosalind #: 028
URL: http://rosalind.info/problems/prob/
'''

from math import log10

with open('data/rosalind_prob.txt') as input_data:
	dna, gc_content = input_data.readlines()

gc_content = map(float, gc_content.split())

# Counts in the number of G/C codons in index 0 and A/T codons in index 1.
codon_count = [0, 0]
for codon in dna:
	if codon in ['C', 'G']:
		codon_count[0] += 1
	elif codon in ['A', 'T']:
		codon_count[1] += 1


# We use the exponent and product rules for logarithms as a shortcut. 
# This is why we calculated the codon counts.
gc_prob = []
for gc_value in gc_content:
	log_prob = codon_count[0]*log10(0.5*gc_value) + codon_count[1]*log10(0.5*(1-gc_value))
	# Append as a string since we'll use a string join later.
	gc_prob.append(str(log_prob))

with open('output/028_PROB.txt', 'w') as output_file:
	output_file.write(' '.join(gc_prob))
