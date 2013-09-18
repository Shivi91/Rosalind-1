#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Mortal Fibonacci Rabbits
Rosalind ID: FIBD
Rosalind #: 011
URL: http://rosalind.info/problems/fibd/
'''

with open('data/rosalind_fibd.txt') as input_data:
    n,m = map(int, input_data.read().split())

# Populate the initial rabbits.
Rabbits = [1]+[0]*(m-1)

# Calculate the new rabbits (bunnies), in a given year.
# Start at use range(1,n) since our initial population is year 0.
for year in range(1, n):
    Bunnies = 0
    # Get the number of Rabbits able to old enough to give birth.
    for j in range(1,m):
        Bunnies += Rabbits[(year-j-1)%m]
    # Bunnies replace the old rabbits who died.
    Rabbits[(year)%m] = Bunnies

# Total rabbits is the sum of the living rabbits.
Total_Rabbits = sum(Rabbits)

# Write the output data.
with open('output/011_FIBD.txt', 'w') as output_data: 
	print Total_Rabbits
	output_data.write(str(Total_Rabbits))
