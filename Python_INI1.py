#!/usr/bin/env python
'''
A solution to a ROSALIND problem from the Python location.  

Problem Title: Installing Python
Rosalind Python ID: INI1
Rosalind Python #: 001
URL: http://rosalind.info/problems/ini1/
'''

import sys

with open("output/python/Python_INI1.txt", "w") as output_data:
        sys.stdout = output_data
        import this
