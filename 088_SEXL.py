#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Sex-Linked Inheritance
Rosalind ID: SEXL
Rosalind #: 088
URL: http://rosalind.info/problems/sexl/
'''

# This solution is more mathematics than programming.
# 
# Recall from Rosalind Problem 065: Counting Disease Carriers that if x = proportion homozygous recessive, y = proportion heterozygous
# then it was derived that y = 2*sqrt(x) - 2x.
# 
# The derivation remains the same for this problem, only with the substitution x = x^2, because the recessive proportion effects both
# X chromosomes, and not just one allele as in Problem 65.
# 
# Thus, y = 2(x - x^2)

with open('data/rosalind_sexl.txt') as input_data:
	A = map(float, input_data.read().strip().split())

B = [2*(x - x**2) for x in A]

print ' '.join(map(str,B))
with open('output/088_SEXL.txt', 'w') as output_data:
	output_data.write(' '.join(map(str,B)))
