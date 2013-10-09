#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Python location.  

Problem Title: Conditions and Loops
Rosalind Python ID: INI4
Rosalind Python #: 004
URL: http://rosalind.info/problems/ini4/
'''

with open('data/python/rosalind_ini4.txt') as input_data:
	a,b = map(int, input_data.read().strip().split())

if a % 2 == 0:
	a += 1

c = 0
for i in range(a, b+1, 2):
	c += i

print c
with open('output/python/Python_INI4.txt', "w") as output_data:
	output_data.write(str(c))
