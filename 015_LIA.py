#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Independent Alleles
Rosalind ID: LIA
Rosalind #: 05
URL: http://rosalind.info/problems/lia/
'''

from scipy.misc import comb

file1 = open('data/rosalind_lia.txt')
k, N = map(int, file1.read().split())
file1.close()

prob = 0
for i in range(N, 2**k + 1):
    prob += comb(2**k, i) * ((1/4.0)**i) * ((3/4.0)**((2**k)-i))

print prob
