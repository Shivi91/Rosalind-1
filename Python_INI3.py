#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Python location.  

Problem Title: Strings and Lists
Rosalind Python ID: INI3
Rosalind Python #: 003
URL: http://rosalind.info/problems/ini3/
'''

with open('data/python/rosalind_ini3.txt') as input_data:
	s, points = [line.strip() for line in input_data.readlines()]
	a,b,c,d = map(int, points.split())

slices = [s[a:b+1], s[c:d+1]]

print ' '.join(slices)
with open('output/python/Python_INI3.txt', "w") as output_data:
	output_data.write(' '.join(slices))
