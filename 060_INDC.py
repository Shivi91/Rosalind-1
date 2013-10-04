#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Independent Segregation of Chromosomes
Rosalind ID: INDC
Rosalind #: 060
URL: http://rosalind.info/problems/indc/
'''

from scipy.misc import comb
from math import log10

with open('data/rosalind_indc.txt') as input_data:
	n = int(input_data.read().strip())

A = [0]*2*n

# Pull out a factor of 2**(-2*n) so we don't get log10(0) problems with large n.
prob = 2**(2*n)

for i in xrange(2*n):
	# Recall that we pulled out a factor of 2**(-2*n).
	prob -= comb(2*n,i, exact=True)
	# Factor back in the 2**(-2*n) when taking the log!  
	A[i] = -2*n*log10(2)+log10(prob)

with open('output/060_INDC.txt', 'w') as output_data:
	output_data.write(' '.join(map(str,A)))
