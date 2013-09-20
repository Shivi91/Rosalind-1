#!/usr/bin/env python
'''ROSALIND bioinformatics scripts that returns that operate on DNA and RNA.'''

from string import maketrans 

# Kind of pointless, as it's so simple.
def DNA_to_RNA(dna):
	'''Translates DNA to RNA'''
	return dna.replace('T', 'U')

# Kind of pointless, as it's so simple.
def RNA_to_DNA(rna):
	'''Translates RNA to DNA'''
	return rna.replace('U', 'T')


def ReverseComplement(nucleic_acid):
	'''Returns the reverse complement of a given DNA or RNA strand.'''

	# Determine if we have DNA or RNA, and create the appropriate translation.
	if ('T' in nucleic_acid) and ('U' not in nucleic_acid):
		nucleotide = 'ATCG'
		complement = 'TAGC'
	elif ('U' in nucleic_acid) and ('T' not in nucleic_acid):
		nucleotide = 'AUCG'
		complement = 'UAGC'
	else:
		return 'Error: Not DNA or RNA.'

	transtab = maketrans(nucleotide, complement)
	
	# Return the reverse complement.
	return nucleic_acid.translate(transtab)[::-1].lstrip()
