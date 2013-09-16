#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Point Mutations
Rosalind ID: HAMM
Rosalind #: 006
URL: http://rosalind.info/problems/hamm/
'''

with open('data/rosalind_hamm.txt') as input_data:
	lines = input_data.readlines()

s = lines[0].rstrip('\n')
t = lines[1]

count = 0
for index, dna in enumerate(s):
    if dna != t[index]:
        count += 1

print count
