#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Python location.  

Problem Title: Working with Files
Rosalind Python ID: INI5
Rosalind Python #: 005
URL: http://rosalind.info/problems/ini5/
'''

with open('data/python/rosalind_ini5.txt') as input_data:
	lines = [line.strip() for line in input_data.readlines()]

with open('output/python/Python_INI5.txt', "w") as output_data:
	output_data.write(lines[1])
	for i in range(3,len(lines), 2):
		output_data.write('\n'+lines[i])
