#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Mendel's First Law
Rosalind ID: IPRB
Rosalind #: 007
URL: http://rosalind.info/problems/iprb/
'''

from scipy.misc import comb

input_file = open('data/rosalind_iprb.txt')
hom, het, rec = map(int, input_file.read().split())
input_file.close()

# The total number different children that can be produced by two organisms. Factor of 4 because Punit squares yield 4 potential children. 
total = 4*comb(hom+het+rec, 2)

# The number of potential children who display the recessive gene.
totalrec = 4*comb(rec,2) + 2*rec*het + 1*comb(het,2)

# Using the complementary event to find the probability of a dominant gene expression.
print 1 - totalrec/total
