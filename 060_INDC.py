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

# Pull out a factor of 2**(-2*n) to avoid precision problems with large n.
prob = 2**(2*n)

# Initialize as the log of the factor of the probability that needs to be recombined.
 A = [-2*n*log10(2)]*2*n

for i in xrange(2*n):
	# Recall that we pulled out a factor of 2**(-2*n).
	prob -= comb(2*n, i, exact=True)
	# Covert to log and add in factor 2**(-2*n) using log rules.  
	A[i] += log10(prob)

with open('output/060_INDC.txt', 'w') as output_data:
	output_data.write(' '.join(map(str,A)))
