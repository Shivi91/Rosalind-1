#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding a Protein Motif
Rosalind ID: MPRT
Rosalind #: 016
URL: http://rosalind.info/problems/mprt/
'''

# To allow for the presence of its varying forms,
# a protein motif is represented by a shorthand as follows: 
# [XY] means "either X or Y" and {X} means "any amino acid except X." 
# For example, the N-glycosylation motif is written as N{P}[ST]{P}.

from scripts import ReadFASTA

with open('data/rosalind_mprt.txt') as f, open('output/016_MPRT.txt', 'w') as output_file:
	line_written = False
	for protein_name in f:
		protein_url = 'http://www.uniprot.org/uniprot/'+protein_name.strip()+'.fasta'
		protein_fasta = ReadFASTA(protein_url)
		locations = ''
		for i in range(0, len(protein_fasta[0][1])-4+1):
			# Check for the N-glycosylation motif is written as N{P}[ST]{P}.
			if (protein_fasta[0][1][i] == 'N') and (protein_fasta[0][1][i+1] != 'P') and (protein_fasta[0][1][i+2] in ['S','T']) and (protein_fasta[0][1][i+3] != 'P'):
				locations += str(i+1)+' '
            
		if locations != '':
			print protein_name.strip()
			print locations.strip()

			if not line_written:
				output_file.write(protein_name.strip()+'\n'+locations.strip())
				line_written = True

			else:
				output_file.write('\n'+protein_name.strip()+'\n'+locations.strip())
