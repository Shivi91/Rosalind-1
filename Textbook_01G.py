#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Frequent Words with Mismatches Problem
Chapter #: 01
Problem ID: G
URL: http://rosalind.info/problems/1g/
'''

from itertools import combinations

def MismatchList(kmer, d):
	'''Returns a list of all k-mers that mismatch a given k-mer by at most d characters.'''
	kmer_mismatches = [kmer]
	for i in xrange(1,d+1):
		for combo in combinations(range(len(kmer)),i):
			kmer_mismatches += CreateMismatches([[kmer, list(combo)]])

	return kmer_mismatches


def CreateMismatches(swap_list):
	'''Generates mismatching k-mers by replacing the character a given index.'''
	nucleotides = 'ACGT'
	
	# If we have more than one index left to mismatch, repeat the process.
	if len(swap_list[0][1]) > 1:
		mismatch_list = []
		for kmer, indicies in swap_list:
			index = indicies[0]
			indicies = indicies[1:]
			for nuc in [nuc for nuc in nucleotides if nuc != kmer[index]]:
				temp = list(kmer)
				temp[index] = nuc
				mismatch_list.append([''.join(temp), indicies])
		return CreateMismatches(mismatch_list)
	
	# If on the final mismatch, return the list of k-mers.
	else:
		mismatch_list = []
		for kmer, [index] in swap_list:
			for nuc in [nuc for nuc in nucleotides if nuc != kmer[index]]:
				temp = list(kmer)
				temp[index] = nuc
				mismatch_list.append(''.join(temp))
		return mismatch_list


def KmerMismatchDict(dna, k, d):
	'''Returns a dictionary listing the number of times a k-mer appears in a dna strand, up to d mismatches.'''
	kmer_dict = dict()
	for i in xrange(len(dna)-k+1):
		for kmer in MismatchList(dna[i:i+k], d):
			if kmer in kmer_dict:
				kmer_dict[kmer] += 1
			else:
				kmer_dict[kmer] = 1
	return kmer_dict


if __name__ == '__main__':

	with open('data/textbook/rosalind_1g.txt') as input_data:
		dna, [k, d] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]

	kmer_mismatch_dict = KmerMismatchDict(dna, k, d)

	# Computing the maximum value is time consuming to repeat, so only do it once!
	max_val = max(kmer_mismatch_dict.values())
	kmers = [item[0] for item in kmer_mismatch_dict.items() if item[1] == max_val]

	print ' '.join(kmers)
	with open('output/textbook/Textbook_01G.txt', 'w') as output_data:
		output_data.write(' '.join(kmers))
