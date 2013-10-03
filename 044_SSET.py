#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Subsets
Rosalind ID: SSET
Rosalind #: 044
URL: http://rosalind.info/problems/sset/
'''

# This problem is somewhat trivial, as it is well known that for a set with n elements,
# the order of the power set is 2**n.
# 
# Let each element of a set take on the value of 0 or 1.  Then, with the convention that 0 = excluded
# and 1 = included, all possible combinations of 0's and 1's yields all possible subsets.
# Clearly there are 2**n combinations.

with open('data/rosalind_sset.txt') as input_data:
	n = int(input_data.read().strip())

# The answer is supposed to be modulo 1000000, so in case n is very large take the remainder after every multiplication.
sset = 1
for i in xrange(n):
	sset = (sset*2)%1000000

print sset
with open('output/044_SSET.txt', 'w') as output_data:
	output_data.write(str(sset))
