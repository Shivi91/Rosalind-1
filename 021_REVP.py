#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Locating Restriction Sites
Rosalind ID: REVP
Rosalind #: 021
URL: http://rosalind.info/problems/revp/
'''

from scripts import ReadFASTA, ReverseComplementDNA

dna = ReadFASTA('data/rosalind_revp.txt')[0][1]
locations = []

for length in range(4,13):
	for index in range(len(dna)-length+1):
		if dna[index:index+length] == ReverseComplementDNA(dna[index:index+length]):
			print index+1, length
			locations.append(str(index+1)+' '+str(length))

with open('output/021_REVP.txt', 'w') as output_data:
	for location in locations:
		output_data.write(location+'\n')
