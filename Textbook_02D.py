#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Cyclopeptide Sequencing
Chapter #: 02
Problem ID: D
URL: https://beta.stepic.org/Bioinformatics-Algorithms-2/A-Faster-Algorithm-for-Cyclopeptide-Sequencing-100/#step-4
'''

from math import sqrt
from scripts import ProteinWeightDict

def append_char(add_list, add_chars):
	'''Returns a list containing all words possible from add_list with suffixes from add_chars.'''
	newlist = []
	for item in add_list:
		newlist += [item+ch for ch in set(add_chars)]
	return newlist

def spectrum(peptide):
	'''Returns the linear spectrum of a given peptide.'''
	# Dictionary translating RNA to Protein
	weight = ProteinWeightDict()
	# Initialize as the mass 0 and the mass of the entire peptide.
	spec = [0, sum([int(weight[protein]) for protein in peptide])]
	# Find the masses of the adjacent intermediary subpeptides
	spec += [sum([int(weight[protein]) for protein in peptide[j:j+i]]) for i in xrange(1,len(peptide)) for j in xrange(len(peptide)-i+1)]
	# Sort the list in ascending order and convert to strings.
	spec = map(str,sorted(spec))

	return spec

with open('data/textbook/rosalind_2d.txt') as input_data:
	cyclospec = input_data.read().strip().split()

# Create the protein weight dictionary.
weight = ProteinWeightDict()

# Let n be the length of a given peptide, and L be the length of its cyclospectrum.  Then L = n(n-1) + 2.
# Using the quadratic formula to to solve for n:  n = (sqrt(4L-7) + 1)/2
n = int((sqrt(4*len(cyclospec)-7)+1)/2)

# Find the first n protein in the peptide.  
# Need to be careful: two small proteins can add to be less than a larger one, so we can't just take the first n nonzero entries.
# Fortunately, no two small proteins masses add to that of a larger protein.
protein, i = [], 1
while len(protein) != n:
	if int(cyclospec[i]) in map(int,weight.values()):
		protein.append(cyclospec[i])
	i += 1

# Get the name of each protein corresponding to a given weight (if multiple, only take one).
names = []
for w in protein:
	names.append([items[0] for items in weight.items() if int(items[1])==int(w)][0])

# Build the possible sequences.
seq = append_char(names,names)
for repeat in xrange(1,n):
	seq = filter(lambda subpeptide:set(spectrum(subpeptide)) < set(cyclospec), set(seq))
	if repeat != n-1:
		seq = append_char(seq,names)

# Convert each protein to the proper format. 
cyclopeptide_sequence = ['-'.join([str(int(weight[protein])) for protein in peptide]) for peptide in seq]

# Print and save the answer.
print ' '.join(cyclopeptide_sequence)
with open('output/textbook/Textbook_02D.txt', 'w') as output_data:
	output_data.write(' '.join(cyclopeptide_sequence))
