#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Edit Distance
Rosalind ID: EDIT
Rosalind #: 046
URL: http://rosalind.info/problems/edit/
'''

from numpy import zeros
from scripts import ReadFASTA

s, t = [fasta[1] for fasta in ReadFASTA('data/rosalind_edit.txt')]

# Initialize matrix M.
M = zeros((len(s)+1,len(t)+1), dtype=int)
for i in range(1,len(s)+1):
	M[i][0]= i
for i in range(1,len(t)+1):
	M[0][i]= i

# Compute each entry of M.
for i in xrange(1,len(s)+1):
	for j in xrange(1,len(t)+1):
		if s[i-1] == t[j-1]:
			M[i][j] = M[i-1][j-1]
		else:
			M[i][j] = min(M[i-1][j]+1,M[i][j-1]+1, M[i-1][j-1]+1)

# Print and save the desired edit distance.
print M[len(s)][len(t)]
with open('output/046_EDIT.txt', 'w') as output_file:
	output_file.write(str(M[len(s)][len(t)]))
