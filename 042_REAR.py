#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Reversal Distance
Rosalind ID: REAR
Rosalind #: 042
URL: http://rosalind.info/problems/rear/
'''

from copy import deepcopy

with open('data/rosalind_rear.txt') as input_data:
	Permutations = [pair.strip().split('\n') for pair in input_data.read().split('\n\n')]
	for index, pair in enumerate(Permutations):
		Permutations[index] = [map(int, perm.split()) for perm in pair]

# with open('D:/test.txt') as input_data:
# 	Permutations = [pair.strip().split('\n') for pair in input_data.read().split('\n\n')]
# 	for index, pair in enumerate(Permutations):
# 		Permutations[index] = [map(int, perm.split()) for perm in pair]

count_set =[]

count_list = []
A = deepcopy(Permutations)
for fixed_perm, perm in A:
	i, count = 0, 0
	while i < len(fixed_perm) - 1:
		if fixed_perm[i] == perm[i]:
			i += 1
		else:
			j = perm.index(fixed_perm[i])
			perm[i:j+1] = reversed(perm[i:j+1])
			count += 1

	count_list.append(count)

print count_list
count_set.append(count_list)


count_list = []
A = deepcopy(Permutations)
for fixed_perm, perm in A:
	i, count = len(perm)-1, 0
	while i > 0:
		if fixed_perm[i] == perm[i]:
			i -= 1
		else:
			j = perm.index(fixed_perm[i])
			perm[j:i+1] = reversed(perm[j:i+1])
			count += 1

	count_list.append(count)

print count_list
count_set.append(count_list)


A = deepcopy(Permutations)
count_list = []
for fixed_perm, perm in A:
	count, left_index, right_index = 0, 0, len(perm)-1
	while fixed_perm != perm:

		while perm[left_index] == fixed_perm[left_index]:
			left_index += 1
		while perm[right_index] == fixed_perm[right_index]:
			right_index -= 1

		left_dist = perm.index(fixed_perm[left_index]) - left_index
		right_dist = right_index - perm.index(fixed_perm[right_index])

		if left_dist <= right_dist :
			perm[left_index:left_index+left_dist+1] = reversed(perm[left_index:left_index+left_dist+1])
			count += 1
		else:
			perm[right_index-right_dist:right_index+1] = reversed(perm[right_index-right_dist:right_index+1])
			count += 1

	count_list.append(count)

print count_list
count_set.append(count_list)


A = deepcopy(Permutations)
count_list = []
for fixed_perm, perm in A:
	count, left_index, right_index = 0, 0, len(perm)-1
	while fixed_perm != perm:

		while perm[left_index] == fixed_perm[left_index]:
			left_index += 1
		while perm[right_index] == fixed_perm[right_index]:
			right_index -= 1

		left_dist = perm.index(fixed_perm[left_index]) - left_index
		right_dist = right_index - perm.index(fixed_perm[right_index])

		if left_dist >= right_dist :
			perm[left_index:left_index+left_dist+1] = reversed(perm[left_index:left_index+left_dist+1])
			count += 1
		else:
			perm[right_index-right_dist:right_index+1] = reversed(perm[right_index-right_dist:right_index+1])
			count += 1

	count_list.append(count)

print count_list
count_set.append(count_list)


A = deepcopy(Permutations)
count_list = []
for fixed_perm, perm in A:
	count, left_index, right_index = 0, 0, len(perm)-1
	while fixed_perm != perm:

		while perm[left_index] == fixed_perm[left_index]:
			left_index += 1
		while perm[right_index] == fixed_perm[right_index]:
			right_index -= 1

		left_dist = perm.index(fixed_perm[left_index]) - left_index
		right_dist = right_index - perm.index(fixed_perm[right_index])

		if left_dist + right_dist > right_index - left_index + 1:
			if left_dist >= right_dist :
				perm[left_index:left_index+left_dist+1] = reversed(perm[left_index:left_index+left_dist+1])
				count += 1
			else:
				perm[right_index-right_dist:right_index+1] = reversed(perm[right_index-right_dist:right_index+1])
				count += 1

		elif left_dist <= right_dist :
			perm[left_index:left_index+left_dist+1] = reversed(perm[left_index:left_index+left_dist+1])
			count += 1
		else:
			perm[right_index-right_dist:right_index+1] = reversed(perm[right_index-right_dist:right_index+1])
			count += 1

	count_list.append(count)

print count_list
count_set.append(count_list)

min_count = [str(min(perm_count)) for perm_count in zip(*count_set)]

print ' '.join(min_count)
with open('output/042_REAR.txt', 'w') as output_data:
	output_data.write(' '.join(min_count))
