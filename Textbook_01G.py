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
		# Each combination gives the indicies we want to mismatch.
		kmer_mismatches += CreateMismatches([[kmer, list(combo)] for combo in combinations(range(len(kmer)),i)])
	return kmer_mismatches


def CreateMismatches(swap_list):
	'''Generates k-mer mismatches by replacing the characters at given indicies with mismatching characters.'''
	nucleotides = 'ACGT'
	mismatch_list = []
	# Swap the i-th character of string with the character ch.
	swap = lambda string, ch, i: string[:index]+ch+string[index+1:]

	# If we have more than one index left to mismatch, repeat the process.
	if len(swap_list[0][1]) > 1:
		for kmer, indicies in swap_list:
			index = indicies[0]
			for nuc in [nucleotide for nucleotide in nucleotides if nucleotide != kmer[index]]:
				mismatch_list.append([swap(kmer, nuc, index), indicies[1:]])
		
		return CreateMismatches(mismatch_list)
	
	# Otherwise, on the final mismatch return the list of k-mers.
	else:
		for kmer, [index] in swap_list:
			for nuc in [nuc for nuc in nucleotides if nuc != kmer[index]]:
				mismatch_list.append(swap(kmer, nuc, index))
		
		return mismatch_list


if __name__ == '__main__':

	with open('data/textbook/rosalind_1g.txt') as input_data:
		dna, [k, d] = [line.strip() if index == 0 else map(int, line.strip().split()) for index, line in enumerate(input_data.readlines())]

	# Count the occurence of each k-mer with up to d mismatches in a dictionary.
	mismatch_dict = {}
	for i in xrange(len(dna)-k+1):
		for kmer in MismatchList(dna[i:i+k], d):
			if kmer in mismatch_dict:
				mismatch_dict[kmer] += 1
			else:
				mismatch_dict[kmer] = 1

	# Computing the maximum value is somewhat time consuming to repeat, so only do it once!
	max_val = max(mismatch_dict.values())
	kmers = [item[0] for item in mismatch_dict.items() if item[1] == max_val]

	print ' '.join(kmers)
	with open('output/textbook/Textbook_01G.txt', 'w') as output_data:
		output_data.write(' '.join(kmers))
