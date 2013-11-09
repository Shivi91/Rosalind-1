#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem from the Armory problem area, 
which focuses on using prebuilt bioinformatics packages, in this case BioPython.

Problem Title: RefSeq Database
Rosalind Armory ID: REFS
Rosalind Armory #: 007
URL: http://rosalind.info/problems/refs/
'''

from Bio import Entrez

with open('data/armory/rosalind_refs.txt') as input_data:
	genus, a, b, end_date = [line.strip() for line in input_data.readlines()]

Entrez.email = 'jschendel@users.noreply.github.com'
handle = Entrez.esearch(db='nucleotide', term=genus+'[Organism] AND ('+a+'[SLEN]:'+b+'[SLEN]) AND srcdb_refseq[PROP]', mindate='1986/1/1', maxdate=end_date, datetype='pdat')
record = Entrez.read(handle)

print record['Count']
with open('output/armory/Armory_007_REFS.txt', 'w') as output_data:
	output_data.write(record['Count'])
