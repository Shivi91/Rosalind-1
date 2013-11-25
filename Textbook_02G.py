#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Convolution Cyclopeptide Sequencing
Chapter #: 02
Problem ID: G
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/The-Spectral-Convolution-Saves-the-Day-104/#step-7
'''

def append_protein(add_list, protein_alphabet):
	'''Returns a list containing all peptides from add_list with every possible protein suffix.'''
	newlist = []
	for item in add_list:
		for p in protein_alphabet:
			newlist.append(item+[p])

	return newlist

def spectrum(peptide):
	'''Returns the circular spectrum of a given peptide.'''
	# Initialize as the mass 0 and the mass of the entire peptide.
	spect = [0, sum(peptide)]
	# Find the masses of the adjacent intermediary subpeptides
	spect += [sum([protein for protein in (peptide*2)[j:j+i]]) for i in xrange(1,len(peptide)) for j in xrange(len(peptide))]

	return sorted(spect)

def spectrum_score(peptide, exp_spec):
	'''Returns the number of matching masses from the spectrum of peptide when compared with the spectrum exp_spec.'''
	pep_spec = spectrum(peptide)
	# Return -1 if the peptide has more mass than exp_spec.
	if pep_spec[-1] > exp_spec[-1]:
		return -1
	return sum([min(pep_spec.count(protein),exp_spec.count(protein)) for protein in set(pep_spec)])

if __name__ == '__main__':

	with open('data/textbook/rosalind_2g.txt') as input_data:
		m, n, spec = [int(line.strip()) if i <= 1 else sorted(map(int,line.strip().split())) for i, line in enumerate(input_data.readlines())]

	# Get the convolution.
	convolution = [i-j for i in spec for j in spec if i-j > 0]

	# Get the top M elements from the convolution that are between 57 and 200.
	convo_dict = dict()
	for c in set(filter(lambda c: 57<=c<=200, convolution)):
		num_c = convolution.count(c)
		if num_c in convo_dict:
			convo_dict[num_c].append(c) 
		else:
			convo_dict[num_c] = [c]

	alphabet = []
	while len(alphabet) < m:
		alphabet += convo_dict[max(convo_dict.keys())]
		del convo_dict[max(convo_dict.keys())]

	# Initialize the overall leader.
	overall_leader = [-1,-1]
	# Build the intial peptides.
	seq = filter(lambda L: L[0] != -1, [[spectrum_score([peptide],spec), [peptide]] for peptide in alphabet]) 

	# Build the sequence until the masses all grow too large.
	while seq != []:

		# Add the peptides and scores from the current round to the scores dictonary.
		scores = dict()
		for item in seq:
			if item[0] in scores:
				scores[item[0]].append(item[1])
			else:
				scores[item[0]] = [item[1]]

		# If we have less than n total items, then use all of them.
		if len(seq) < n:
			leaders = [item[1] for item in seq]
			leader_scores = [min(item[0] for item in seq)]

		# Otherwise, get the n leading scores with ties, remove lower scores from dictionary.
		else:
			leaders, leader_scores = [], []
			while len(leaders) < n:
				current_max = max(filter(lambda s: s not in leader_scores, scores.keys()))
				leaders += scores[current_max]
				leader_scores.append(current_max)

		# Use this line to reduce runtime, removes excess ties.
		# leaders = leaders[:100]

		# If necessary, update the overall leader.
		if overall_leader[0] <= max(scores.keys()):
			overall_leader = [max(scores.keys()), '-'.join(map(str, scores[max(scores.keys())][0]))]

		# Generate a new sequence of scores from the leaders.
		seq = filter(lambda L: L[0] != -1, [[spectrum_score(peptide,spec), peptide] for peptide in append_protein(leaders, alphabet)])

	# Print and save the answer.
	print overall_leader[1]
	with open('output/textbook/Textbook_02G.txt', 'w') as output_data:
		output_data.write(overall_leader[1])
