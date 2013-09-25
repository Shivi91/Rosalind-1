#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Matching Random Motifs
Rosalind ID: RSTR
Rosalind #: 043
URL: http://rosalind.info/problems/rstr/
'''

with open('data/rosalind_rstr.txt') as input_data:
	N, gc_content, dna = input_data.read().strip().split()
	N = int(N)
	gc_content = float(gc_content)
	
# print [N, gc_content, dna]

# Counts in the number of G/C codons in index 0 and A/T codons in index 1.
codon_count = [0, 0]
for codon in dna:
	if codon in ['C', 'G']:
		codon_count[0] += 1
	elif codon in ['A', 'T']:
		codon_count[1] += 1


# The probability the a randomly created dna sequence will with a specific GC content will match the given dna sequence.
dna_prob = ((0.5*gc_content)**codon_count[0])*((0.5*(1-gc_content))**codon_count[1])

# The probability of one or more dna sequences out of N randomly generated sequences with a specific GC content will match the given dna sequence.
# Note: Using the probability of the complement. This is a binomial random variable.  However, we only need the 0th term for the probability of 
# the complement, so binomial coefficient and probability term will be one, and hence unnecessary in the calculation.
prob = 1 - (1-dna_prob)**N

print prob
with open('output/043_RSTR.txt', 'w') as output_data:
	output_data.write(str(prob))
