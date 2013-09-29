#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Expected Number of Restriction Sites
Rosalind ID: EVAL
Rosalind #: 047
URL: http://rosalind.info/problems/eval/
'''

with open('data/rosalind_eval.txt') as input_data:
	n, dna, gc_content = input_data.readlines()
	n = int(n.strip())
	dna = dna.strip()
	gc_content = map(float, gc_content.split())

# Counts in the number of G/C codons in index 0 and A/T codons in index 1.
codon_count = [dna.count('C')+dna.count('G'), dna.count('A')+dna.count('T')]

# The number of slots where a substring of length len(dna) can appear in a dna string of length n.
substring_slots = n - len(dna) + 1

expected_substrings = []
for gc_value in gc_content:
	# The probability the a randomly created dna sequence will with a specific GC content will match the given dna sequence.
	dna_prob = ((0.5*gc_value)**codon_count[0])*((0.5*(1-gc_value))**codon_count[1])

	# Expected values is additive, and we're adding the same probability for each possible slot, hence EV = dna_prob*substring_slots
	expected_substrings.append(str(dna_prob*substring_slots))

print ' '.join(expected_substrings)
with open('output/047_EVAL.txt', 'w') as output_data:
	output_data.write(' '.join(expected_substrings))
