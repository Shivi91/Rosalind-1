#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Introduction to Alternative Splicing
Rosalind ID: ASPC
Rosalind #: 045
URL: http://rosalind.info/problems/aspc/
'''

from scipy.misc import comb

with open('data/rosalind_aspc.txt') as input_data:
	n, m = map(int, input_data.read().split())

aspc_count = 0
for k in xrange(m,n+1):
	aspc_count = (aspc_count + comb(n,k, exact=True))%1000000

print aspc_count
with open('output/045_ASPC.txt', 'w') as output_data:
	output_data.write(str(aspc_count))
