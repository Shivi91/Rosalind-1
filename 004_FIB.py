#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Rabbits and Recurrence Relations
Rosalind ID: FIB
Rosalind #: 004
URL: http://rosalind.info/problems/fib/
'''

def Fib(n,k):
    '''The total number of rabbit pairs that will be present after n months if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter of k rabbit pairs'''
    
    if n < 1:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fib(n-1,k) + k*Fib(n-2, k)


input_file = open('data/rosalind_fib.txt')
n,k = map(int, input_file.read().split())
input_file.close()

print Fib(n,k)
