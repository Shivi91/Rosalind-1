#!/usr/bin/env python
'''A ROSALIND bioinformatics script to create an RNA to Protein dictionary.'''


def RNA_to_Protein_Dict():
	'''Returns a dictionary that translates RNA to Protein'''
	# Get the raw codon table.
	rna2protein = CodonTable()

	# Convert to dictionary.
	rna_dict = {}
	for index, item in enumerate(rna2protein):
	    rna_dict[item.split()[0]] = item.split()[1]

	return rna_dict


def CodonTable():

	table = '''UUU F
	UUC F
	UUA L
	UUG L
	UCU S
	UCC S
	UCA S
	UCG S
	UAU Y
	UAC Y
	UAA Stop
	UAG Stop
	UGU C
	UGC C
	UGA Stop
	UGG W
	CUU L
	CUC L
	CUA L
	CUG L
	CCU P
	CCC P
	CCA P
	CCG P
	CAU H
	CAC H
	CAA Q
	CAG Q
	CGU R
	CGC R
	CGA R
	CGG R
	AUU I
	AUC I
	AUA I
	AUG M
	ACU T
	ACC T
	ACA T
	ACG T
	AAU N
	AAC N
	AAA K
	AAG K
	AGU S
	AGC S
	AGA R
	AGG R
	GUU V
	GUC V
	GUA V
	GUG V
	GCU A
	GCC A
	GCA A
	GCG A
	GAU D
	GAC D
	GAA E
	GAG E
	GGU G
	GGC G
	GGA G
	GGG G'''

	return table.split('\n')
