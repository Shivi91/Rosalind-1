#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding a Motif in DNA
Rosalind ID: SUBS
Rosalind #: 009
URL: http://rosalind.info/problems/subs/
'''

file1 = open('data/rosalind_subs.txt')
s,t = file1.readlines()
s = s.rstrip()
t = t.rstrip()
file1.close()

locations = ''
for i in range(0, len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        locations += str(i+1)+' '

print locations.rstrip()
