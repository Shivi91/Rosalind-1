#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Point Mutations
Rosalind ID: HAMM
Rosalind #: 006
URL: http://rosalind.info/problems/hamm/
'''

inpfile = open('data/rosalind_hamm.txt')
lines = inpfile.readlines()
inpfile.close()

s = lines[0].rstrip('\n')
t = lines[1]

count = 0
for index, dna in enumerate(s):
    if dna != t[index]:
        count += 1

print count
