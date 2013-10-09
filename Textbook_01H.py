#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Frequent Words with Mismatches and Reverse Complements Problem 
Chapter #: 01
Problem ID: H
URL: http://rosalind.info/problems/1h/
'''

from scripts import ReverseComplementDNA
from Textbook_01G import KmerMismatchDict, MismatchList


def KmerRevCompMismatchDict(revc_dict, dna, k, d):
	'''Takes the regular k-mer mismatch dictonary from 1G and adds the number of times the reverse complement of a k-mer appears in a dna strand, up to d mismatches.'''
	for i in xrange(len(dna)-k+1):
		for kmer in MismatchList(ReverseComplementDNA(dna[i:i+k]), d):
			if kmer in revc_dict:
				revc_dict[kmer] += 1
			else:
				revc_dict[kmer] = 1
	return revc_dict


if __name__ == '__main__':

	with open('data/textbook/rosalind_1h.txt') as input_data:
		dna, [k, d] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]

	kmer_revc_mismatch_dict = KmerRevCompMismatchDict(KmerMismatchDict(dna, k, d), dna, k, d)

	# Computing the maximum value is time consuming to repeat, so only do it once!
	max_val = max(kmer_revc_mismatch_dict.values())
	kmers = [item[0] for item in kmer_revc_mismatch_dict.items() if item[1] == max_val]

	print ' '.join(kmers)
	with open('output/textbook/Textbook_01H.txt', 'w') as output_data:
		output_data.write(' '.join(kmers))
