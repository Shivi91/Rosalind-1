#!/usr/bin/env python
'''
A solution to a code challenges that accompanies Bioinformatics Algorithms: An Active-Learning Approach by Phillip Compeau & Pavel Pevzner.
The textbook is hosted on Stepic and the problem is listed on ROSALIND under the Textbook track.

Problem Title: Reverse Complement Problem
Chapter #: 01
Problem ID: B
URL: http://rosalind.info/problems/1b/
'''

from scripts import ReverseComplementDNA

with open('data/textbook/rosalind_1b.txt') as input_data:
	dna = input_data.read().strip()

# The script I previously wrote solves the problem...
with open('output/textbook/Textbook_01B.txt', 'w') as output_data:
	output_data.write(ReverseComplementDNA(dna))
