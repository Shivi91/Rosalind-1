#!/usr/bin/env python
'''A ROSALIND bioinformatics script to create RNA and DNA to Protein dictionary.'''



def ProteinDictDNA():
	'''Returns a dictionary that translates DNA to Protein'''
	# Get the raw codon table.
	dna2protein = CodonTableDNA()

	# Convert to dictionary.
	dna_dict = {}
	for translation in dna2protein:
	    dna_dict[translation[0]] = translation[1]

	return dna_dict


def ProteinDictRNA():
	'''Returns a dictionary that translates RNA to Protein'''
	# Get the raw codon table.
	rna2protein = CodonTableRNA()

	# Convert to dictionary.
	rna_dict = {}
	for translation in rna2protein:
	    rna_dict[translation[0]] = translation[1]

	return rna_dict


def CodonTableDNA():
	'''Returns a DNA Codon translation list.'''
	table = '''TTT F
	CTT L      
	ATT I      
	GTT V
	TTC F      
	CTC L      
	ATC I      
	GTC V
	TTA L     
	CTA L      
	ATA I      
	GTA V
	TTG L      
	CTG L      
	ATG M      
	GTG V
	TCT S      
	CCT P      
	ACT T      
	GCT A
	TCC S      
	CCC P      
	ACC T      
	GCC A
	TCA S      
	CCA P      
	ACA T      
	GCA A
	TCG S      
	CCG P      
	ACG T      
	GCG A
	TAT Y      
	CAT H      
	AAT N      
	GAT D
	TAC Y      
	CAC H      
	AAC N      
	GAC D
	TAA Stop   
	CAA Q      
	AAA K      
	GAA E
	TAG Stop   
	CAG Q      
	AAG K      
	GAG E
	TGT C      
	CGT R      
	AGT S      
	GGT G
	TGC C      
	CGC R      
	AGC S      
	GGC G
	TGA Stop   
	CGA R      
	AGA R      
	GGA G
	TGG W      
	CGG R      
	AGG R      
	GGG G'''

	table = table.split('\n')
	for index, item in enumerate(table):
		table[index] = item.strip().split()

	return table



def CodonTableRNA():
	'''Returns an RNA Codon translation list.'''
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
	
	table = table.split('\n')
	for index, item in enumerate(table):
		table[index] = item.strip().split()

	return table
