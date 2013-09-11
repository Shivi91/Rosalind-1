#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Enumerating Gene Orders
Rosalind ID: PERM
Rosalind #: 019
URL: http://rosalind.info/problems/perm/
'''

from itertools import permutations

def factorial(n):
	'''Returns the value of n!'''
	if n < 2:
		return 1
	else:
		return n*factorial(n-1)

file1 = open('data/rosalind_perm.txt')
perm_set = range(1, int(file1.read())+1)
file1.close()

# Create a list containing ordered lists of all permutations.
perm_list = map(list,list(permutations(perm_set)))

output_file = open('output/019_PERM.txt', 'w')

# Write the total number of permutations, n!
output_file.write(str(factorial(len(perm_set))))

# Write the permuations in the desired format.
for permutation in perm_list:
	output_file.write('\n'+' '.join(map(str,permutation)))

output_file.close()
