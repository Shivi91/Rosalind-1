#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Mortal Fibonacci Rabbits
Rosalind ID: FIBD
Rosalind #: 011
URL: http://rosalind.info/problems/fibd/

--------------------------------------------------------
NOTE
--------------------------------------------------------
This solution is valid, but very slow for large numbers.
Use the Maple solution for large values.
'''

class MortalRabbit():

    def __init__(self, lifespan =  3):
        self.age = 0
        self.lifespan = lifespan


def Rab(months, lifespan):

    Rabbits = [MortalRabbit(lifespan)]
           
    for i in range(months - 1):
        newRabbits = []
        for bunny in Rabbits:
            bunny.age += 1
            if bunny.age > 1:
                newRabbits.append(MortalRabbit(lifespan))
            
            if bunny.age < bunny.lifespan:
                newRabbits.append(bunny)
        
        Rabbits = newRabbits
    return len(Rabbits)


for i in range(1,27):
    print i, '|', Rab(i,16)
