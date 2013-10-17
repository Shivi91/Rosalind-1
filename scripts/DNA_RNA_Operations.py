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


def ReverseComplementDNA(nucleic_acid):
	'''Returns the reverse complement of a given DNA strand.'''
	nucleotide = 'ATCG'
	complement = 'TAGC'
	transtab = maketrans(nucleotide, complement)
	
	return nucleic_acid.translate(transtab)[::-1].lstrip()

def ReverseComplementRNA(nucleic_acid):
	'''Returns the reverse complement of a given RNA strand.'''
	nucleotide = 'AUCG'
	complement = 'UAGC'
	transtab = maketrans(nucleotide, complement)
	
	return nucleic_acid.translate(transtab)[::-1].lstrip()

def HammingDistance(seq1, seq2):
    'Return the Hamming distance between equal-length sequences.'
    if len(seq1) != len(seq2):
        raise ValueError('Undefined for sequences of unequal length.')
    return sum(ch1 != ch2 for ch1, ch2 in zip(seq1, seq2))