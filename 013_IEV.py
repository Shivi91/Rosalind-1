#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Calculating Expected Offspring
Rosalind ID: IEV
Rosalind #: 013
URL: http://rosalind.info/problems/iev/
'''

with open('data/rosalind_iev.txt') as input_data:
	s = input_data.read().split()

# Probabilities of Child Dominant Genotype
# ----------------------------------------
# s[0]: AA-AA -> 100% chance of dominant
# s[1]: AA-Aa -> 100%
# s[2]: AA-aa -> 100%
# s[3]: Aa-Aa -> 75%
# s[4]: Aa-aa -> 50%
# s[5]: aa-aa -> 0%

p_list = [1, 1, 1, 0.75, 0.5, 0]
EV_list =[]

# A simple application of expected value.
for index, num_parents in enumerate(s):
    EV_list.append(2*int(num_parents)*p_list[index])

print sum(EV_list)
