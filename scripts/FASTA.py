#!/usr/bin/env python
'''A ROSALIND bioinformatics script to extract FASTA DNA data.'''

def ReadFASTA(fname):
        '''Extracts DNA name and DNA sequence from the a FASTA styled file.'''
        dna_list = []
        with open(fname) as f:
        	for line in f:

        		# If the line starts with '>' we've hit a new DNA strand, so append the old one and create the new one.
        		if line[0] == '>':
        			
        			# Using try/except because intially there will be no current DNA strand to append.
        			try:
        				dna_list.append(current_dna)
        			except UnboundLocalError:
        				pass
  
        			current_dna = [line.lstrip('>').rstrip('\n'),'']

        		# Otherwise, append the current DNA line to the current DNA
        		else:
        			current_dna[1] += line.rstrip('\n')
        	
        	# Append the final DNA strand after reading all the lines.
        	dna_list.append(current_dna)
     
        return dna_list
