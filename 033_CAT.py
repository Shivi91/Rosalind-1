#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Catalan Numbers and RNA Secondary Structures
Rosalind ID: CAT
Rosalind #: 033
URL: http://rosalind.info/problems/cat/
'''

from scripts import ReadFASTA

def Noncrossing(rna):
	'''Returns the number of noncrossing bonding graphs for a given RNA sequence.'''
	global noncross_dict
	global matchings
	if len(rna) <= 2:
		# We only send valid rna matchings, so this return is ok.
		return 1
	else:
		# If we've already computed the value, return it!
		if rna in noncross_dict:
			return noncross_dict[rna]
		# Otherwise, calculate the values.
		else:
			subintervals = []
			for i in xrange(1, len(rna),2):
				if rna[0] == matchings[rna[i]] and check_subinterval(rna[1:i]):
					subintervals.append([rna[1:i],rna[i+1:]])

			if subintervals == []:
				# If we didn't find any subintervals, there are no possible noncrossing matchings.
				noncross_dict[rna] = 0
			else:
				# Reduce the problem to noncrossing matchings over the substrings.
				noncross_dict[rna] = sum([Noncrossing(subint[0])*Noncrossing(subint[1]) for subint in subintervals]) % 1000000
			
			return noncross_dict[rna]

def check_subinterval(subint):
	'''Checks if a given subinterval has the same number of matching nucleotides.'''
	N = [subint.count(nucleotide) for nucleotide in 'AUCG']
	if N[0] == N[1] and N[2] == N[3]:
		return True
	return False

rna = ReadFASTA('data/rosalind_cat.txt')[0][1]
noncross_dict = {}
matchings = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
noncross = Noncrossing(rna)
print noncross
with open('output/033_CAT.txt', 'w') as output_file:
	output_file.write(str(noncross))
