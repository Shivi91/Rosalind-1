#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding a Motif in DNA
Rosalind ID: SUBS
Rosalind #: 009
URL: http://rosalind.info/problems/subs/
'''

with open('data/rosalind_subs.txt') as input_data:
	s,t = input_data.readlines()
	s = s.rstrip()
	t = t.rstrip()

locations = []
for i in range(0, len(s)-len(t)+1):
    if s[i:i+len(t)] == t:
        locations.append(str(i+1))

print ' '.join(locations)
with open('output/009_SUBS.txt', 'w') as output_data:
	output_data.write(' '.join(locations))
