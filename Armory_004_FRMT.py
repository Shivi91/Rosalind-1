#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem from the Armory problem area, 
which focuses on using prebuilt bioinformatics packages, in this case BioPython.

Problem Title: Data Formats
Rosalind Armory ID: FRMT
Rosalind Armory #: 004
URL: http://rosalind.info/problems/frmt/
'''

from Bio import Entrez
from Bio import SeqIO

with open('data/armory/rosalind_frmt.txt') as input_data:
	IDs = input_data.read().strip().split()

Entrez.email = 'jschendel@users.noreply.github.com'
handle = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
records = list(SeqIO.parse(handle, 'fasta'))

[min_index] = [i for i in range(len(records)) if len(records[i]) == min([len(record.seq) for record in records])]

handle2 = Entrez.efetch(db='nucleotide', id=IDs, rettype='fasta')
minFASTA = handle2.read().strip().split('\n\n')[min_index]

print minFASTA
with open('output/armory/Armory_004_FRMT.txt', 'w') as output_data:
	output_data.write(minFASTA)
