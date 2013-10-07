#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Disease Carriers
Rosalind ID: AFRQ
Rosalind #: 065
URL: http://rosalind.info/problems/afrq/
'''

# This solution is more mathematics than programming.
# 
# Let x = proportion homozygous recessive, y = proportion heterozygous.
# We want the proportion of the population carrying at least one recessive gene, so the answer is x + y.
# 
# Assume that the allele frequency is stable, meaning that it remains the same after mating.
# We're given the proportion of recessive individuals, so setup an equation for the proportion of recessive indiviudals.
# Observe that the only way we get the recessive trait is mating between recessives and/or heterozygous.
# 
# Use the total law of probability, noting that the unlist terms are zero:
# Proportion Recessive = P(Recessive|2 Rec Mate)P(2 Rec Mate) + P(Recessive|1 Rec 1 Het Mate)P(1 Rec 1 Het Mate) + P(Recessive|2 Het Mate)P(2 Het Mate)
# In terms of variables:  x = (1)*(x^2) + (0.5)(2*x*y) + (0.25)*(y^2)
#                         x = x^2 + xy + 0.25y^2  
# 
# Use the quadratic formula to solve for y: y = -2x +/- 2*sqrt(x)  ==> y = 2*sqrt(x) - 2x since y must be positive. (note x in [0,1] ==> y in [0,1])
# 
# Subsititute into the solution formula: x + y = x +(2*sqrt(x)-2x) = 2*sqrt(x) - x
# 
# Thus, the solution is 2*sqrt(x) - x

from math import sqrt

with open('data/rosalind_afrq.txt') as input_data:
	A = map(float, input_data.read().strip().split())

B = [2*sqrt(i)-i for i in A]

print ' '.join(map(str,B))
with open('output/065_AFRQ.txt', 'w') as output_data:
	output_data.write(' '.join(map(str,B)))
