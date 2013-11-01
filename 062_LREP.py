#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding the Longest Multiple Repeat
Rosalind ID: LREP
Rosalind #: 062
URL: http://rosalind.info/problems/lrep/
'''

with open('data/rosalind_lrep.txt') as input_data:
	raw_data = input_data.readlines()

# Parse the data.
s = raw_data[0].strip()
k = int(raw_data[1].strip())
node_info = [line.strip().split() for line in raw_data[2:]]
node_info = [[[line[0],line[1]], int(line[2]),int(line[3])]  for line in node_info]
edges = [info[0] for info in node_info]

# Construct a previous node dictionary for quick backtracking.
previous_node = {'node1':'ROOT'}
for edge in edges:
	previous_node[edge[1]] = edge[0]

# Construct a dictionary relating a node to its substring.
node_str = {'node1':''}
for info in node_info:
	node_str[info[0][1]] = s[info[1]-1:info[1]+info[2]-1].strip('$')

# Determine the leaves.
heads = set([edge[0] for edge in edges])
tails = set([edge[1] for edge in edges])
leaves = tails - heads

# Count the number of descendants for each node.
num_nodes = max([int(node[4:]) for node in leaves])
descendants = [0]*num_nodes
for leaf in leaves:
	descendants[int(leaf[4:])-1] += 1
	temp_node = previous_node[leaf]
	while temp_node != 'ROOT':
		descendants[int(temp_node[4:])-1] += 1
		temp_node = previous_node[temp_node]

# Find the candidate substrings.
candidate_nodes = []
for i, num in enumerate(descendants[1:]): # Skip node1, as it is the empty string.
	if num >= k:
		candidate_nodes.append('node'+str(i+2)) # Plus two since we're starting at at index 0 = node 2.

candidate_strings = []
for node in candidate_nodes:
	temp_str = ''
	temp_node = node
	while temp_node != 'ROOT':
		temp_str = node_str[temp_node] + temp_str
		temp_node = previous_node[temp_node]
	candidate_strings.append(temp_str)

# Print and save a longest candidate substring.
lrep = max(candidate_strings, key=len)
print lrep
with open('output/062_LREP.txt', 'w') as output_file:
	output_file.write(lrep)
