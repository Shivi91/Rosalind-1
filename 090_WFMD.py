#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: The Wright-Fisher Model of Genetic Drift
Rosalind ID: WFMD
Rosalind #: 090
URL: http://rosalind.info/problems/wfmd/
'''

from scipy.misc import comb

with open('data/rosalind_wfmd.txt') as input_data:
	N,m,g,k = [int(num) for num in input_data.read().strip().split()]

# Determine the probabiliy of a given of recessive allels in the first generation.
# Use a binomial random variable with the given parameters.
# Note:  We omit the 0th term throughout the problem, as it has no contribution to the desired probability.
#        For future problems, start the ranges at 0 if the 0 term ever becomes necessary. 
p_rec = 1.0 - (m/(2.0*N))
p = [comb(2*N, i)*((p_rec)**i)*(1.0-p_rec)**(2*N-i) for i in range(1,2*N+1)]

# Determine the probabiliy of a given of recessive allels in the 2nd to k-th generations.
# Use the total law of probability, along with the probabilities from the previous generation.
# i.e., P(1 Rec) = P(1 Rec | 0 Rec in previous gen) +  P(1 Rec | 1 Rec in previous gen) + ... + P(1 Rec | 2N Rec in previous gen)
# Notice that the conditional probabilities are binomial terms, similar to the first generation calculations.
for gen in range(2,g+1):
    temp_p = []
    for j in range(1,2*N+1):
        temp_term = [comb(2*N, j)*((x/(2.0*N))**j)*(1.0-(x/(2.0*N)))**(2*N-j) for x in range(1,2*N+1)]
        temp_p.append(sum([temp_term[i]*p[i] for i in range(len(temp_term))]))
    p = temp_p

# Now, sum to get the desired probability.  Note: We have k-1 due to omitting the 0th term.
prob = sum(p[k-1:])
print prob
with open('output/090_WFMD.txt', 'w') as output_file:
	output_file.write(str(prob))
