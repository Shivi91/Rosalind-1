#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Independent Alleles
Rosalind ID: LIA
Rosalind #: 015
URL: http://rosalind.info/problems/lia/
'''

from scipy.misc import comb

with open('data/rosalind_lia.txt') as input_data:
	k, N = map(int, input_data.read().split())

prob = 0
for i in range(N, 2**k + 1):
    prob += comb(2**k, i) * ((1/4.0)**i) * ((3/4.0)**((2**k)-i))

print prob
