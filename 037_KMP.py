#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Speeding Up Motif Finding
Rosalind ID: KMP
Rosalind #: 037
URL: http://rosalind.info/problems/kmp/
'''

from scripts import ReadFASTA

dna = ReadFASTA('data/rosalind_kmp.txt')[0][1]

P = [0]*len(dna)
k = 0
for q in range(2, len(dna)):
    while k > 0 and dna[k] != dna[q-1]:
        k = P[k-1]
    if dna[k] == dna[q-1]:
        k += 1
    P[q-1] = k

print ' '.join(map(str, P))
with open('output/037_KMP.txt', 'w') as output_data:
	output_data.write(' '.join(map(str, P)))
