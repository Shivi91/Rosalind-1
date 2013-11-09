#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem from the Armory problem area, 
which focuses on using prebuilt bioinformatics packages, in this case BioPython.

Problem Title: GenBank Introduction
Rosalind Armory ID: GBK
Rosalind Armory #: 003
URL: http://rosalind.info/problems/gbk/
'''

from Bio import Entrez

with open('data/armory/rosalind_gbk.txt') as input_data:
	genus, start_date, end_date = [line.strip() for line in input_data.readlines()]

Entrez.email = 'jschendel@users.noreply.github.com'
handle = Entrez.esearch(db='nucleotide', term=genus+'[ORGN]', mindate=start_date, maxdate=end_date, datetype='pdat')
record = Entrez.read(handle)

print record['Count']
with open('output/armory/Armory_003_GBK.txt', 'w') as output_data:
	output_data.write(record['Count'])
