#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Perfect Matchings and RNA Secondary Structures
Rosalind ID: PMCH
Rosalind #: 026
URL: http://rosalind.info/problems/pmch/
'''

from math import factorial
from scripts import ReadFASTA

rna = ReadFASTA('data/rosalind_pmch.txt')[0][1]

pmch = factorial(rna.count('A'))*factorial(rna.count('C'))
print pmch

with open('output/026_PMCH.txt', 'w') as output_data:
	output_data.write(str(pmch))
