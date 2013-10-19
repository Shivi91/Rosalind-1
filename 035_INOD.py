#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Phylogenetic Ancestors
Rosalind ID: INOD
Rosalind #: 035
URL: http://rosalind.info/problems/inod/
'''

# -----------------------------------------------------------------------------------------------------------------
# This solution is more mathematics (graph theory) than programming.

# Let m = number of internal nodes, n = number of leaves, and E = number of edges

# An elementary property of any graph is that the sum of the degrees of all verticies is twice the number of edges.
# In terms of variables: 2E = 3m + n 

# From Rosalind Problem #32, we have that the total number of edges is one less than the number of nodes.
# In terms of variables: E = m + n - 1.
# Scaling to match the above: 2E = 2m + 2n - 2

# Now set the two expressions equal to each other, and solve for m in terms of n.
# 3m + n = 2m + 2n - 2  ==> m = n - 2

# Thus, an unrooted binary tree with n leaves has n-2 internal nodes.
# -----------------------------------------------------------------------------------------------------------------

with open('data/rosalind_inod.txt') as input_data, open('output/035_INOD.txt', 'w') as output_data:
	n = int(input_data.read().strip())
	print n-2
 	output_data.write(str(n-2))
