#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Creating a Restriction Map
Rosalind ID: PDPL
Rosalind #: 086
URL: http://rosalind.info/problems/pdpl/
'''

from math import sqrt

with open('data/rosalind_pdpl.txt') as input_data:
	deltaX = map(int,input_data.read().strip().split())

# Write n choose 2 as a quadratic, solve for n in terms of length with the quadratic formula.
# This tells us how many items we need in our multiset.
n = int(0.5 + 0.5*sqrt(8.0*len(deltaX)+1))

# Pick zero to be the in our multiset.  This is a valid assumption because there are infinitely many solutions.
# Given a solution, shifting each element by a fixed amount doesn't change the delta. Thus, there exists a solution with zero in the set.
myX=[0]

# Add the largest delta to the solution. Since zero is in our multiset, the only way for it to be the largest difference if it's in the multiset.
myX.append(max(deltaX))
deltaX.remove(myX[1])

# The other values in the multiset must come from deltaX, since zero is in our multiset.
deltaSet = set(deltaX)
for candidate in deltaSet:
	# Test to see if each difference for a candidate member is our list of desired differences.
	if sum([(abs(candidate-member) in deltaX) for member in myX])  == len(myX):
		for member in myX:
			# Remove the differences we've already found.
			deltaX.remove(abs(candidate-member))
		# insert the new value before the largest value to keep the set sorted.
		myX.append(candidate)
		if len(myX) == n:
			break

myX.sort()
print ' '.join(map(str, myX))
with open('output/086_PDPL.txt', 'w') as output_file:
	output_file.write(' '.join(map(str, myX)))
