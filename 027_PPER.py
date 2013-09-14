#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Partial Permutations
Rosalind ID: PPER
Rosalind #: 027
URL: http://rosalind.info/problems/pper/
'''

with open('data/rosalind_pper.txt') as f:
	n,k = map(int,f.read().split())

# Want to calculate n!/(n-k)! = n*(n-1)*...*(n-k+1) modulo 1,000,000
partial_perm = 1
for i in range(n-k+1,n+1):
	partial_perm = (partial_perm*i)%1000000

print partial_perm
with open('output/027_PPER.txt', 'w') as output_file:
	output_file.write(str(partial_perm))
