#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Leaderboard Cyclopeptide Sequencing
Chapter #: 02
Problem ID: E
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/Adapting-Cyclopeptide-Sequencing-for-Spectra-with-Errors-102/#step-3
'''

from scripts import ProteinWeightDict

def append_protein(add_list):
	'''Returns a list containing all peptides from add_list with every possible protein suffix.'''
	newlist = []
	for item in add_list:
		newlist += [item+ch for ch in ProteinWeightDict().keys()]
	return newlist

def spectrum(peptide):
	'''Returns the circular spectrum of a given peptide.'''
	# Initialize as the mass 0 and the mass of the entire peptide.
	spec = [0, sum([int(weight[protein]) for protein in peptide])]
	# Find the masses of the adjacent intermediary subpeptides
	spec += [sum([int(weight[protein]) for protein in (peptide*2)[j:j+i]]) for i in xrange(1,len(peptide)) for j in xrange(len(peptide))]

	return sorted(spec)

def spectrum_score(peptide, exp_spec):
	'''Returns the number of matching masses from the spectrum of peptide when compared with the spectrum exp_spec.'''
	pep_spec = spectrum(peptide)
	# Return -1 if the peptide has more mass than exp_spec.
	if pep_spec[-1] > exp_spec[-1]:
		return -1
	return sum([min(pep_spec.count(protein),exp_spec.count(protein)) for protein in set(pep_spec)])

if __name__ == '__main__':

	with open('data/textbook/rosalind_2e.txt') as input_data:
		n, spec = [int(line.strip()) if i==0 else map(int,line.strip().split()) for i, line in enumerate(input_data.readlines())]
	
	# Create the protein weight dictionary.
	weight = ProteinWeightDict()
	# Initialize the scores dictionary.
	scores = dict()
	# Build the intial peptides.
	seq = filter(lambda L: L[0] != -1, [[spectrum_score(peptide,spec), peptide] for peptide in append_protein(weight.keys())]) 

	# Build the sequence until the masses all grow too large.
	while seq != []:
		# Store the scores of the current sequence in a dictionary.
		scores = dict()
		for item in seq:
			if item[0] in scores:
				scores[item[0]].append(item[1])
			else:
				scores[item[0]] = [item[1]]

		# Get the n leading scores with ties, remove lower scores from dictionary.
		leaders, leader_scores = [], []
		if sum(len(peptides) for peptides in scores.values()) < n:
			leaders = scores[max(scores.keys())]
		else:
			while len(leaders) < n:
				leaders += scores[max(scores.keys())]
				del scores[max(scores.keys())]		

		# Use this line to reduce runtime, removes excess ties.
		# leaders = leaders[:100]

		# Generate a new sequence of scores from the leaders.
		seq = filter(lambda L: L[0] != -1, [[spectrum_score(peptide,spec), peptide] for peptide in append_protein(leaders)])

	# By construction, the scores are listed in descending order, so take the first peptide as the leader peptide.
	leader_peptide = '-'.join([str(int(weight[protein])) for protein in leaders[0]])

	# Print and save the answer.
	print leader_peptide
	with open('output/textbook/Textbook_02E.txt', 'w') as output_data:
		output_data.write(leader_peptide)
