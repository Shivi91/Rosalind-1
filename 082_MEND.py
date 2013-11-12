#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Inferring Genotype from a Pedigree
Rosalind ID: MEND
Rosalind #: 082
URL: http://rosalind.info/problems/mend/
'''

def child_prob(a,b):
	'''Returns the genotype probability for a child with parents who have genotype probabilities a and b.'''
	# Comes from the conditional probability of each possible Punit square.
	AA = a[0]*b[0] + 0.5*(a[0]*b[1] + a[1]*b[0] + 0.5*a[1]*b[1])
	Aa = a[0]*b[2] + a[2]*b[0] + 0.5*(a[0]*b[1] + a[1]*b[0] + a[1]*b[1] + a[2]*b[1] + a[1]*b[2])
	aa = a[2]*b[2] + 0.5*(a[1]*b[2] + a[2]*b[1] + 0.5*a[1]*b[1])
	return [AA,Aa,aa]


if __name__ == '__main__':

	from scripts import Newick

	with open('data/rosalind_mend.txt') as input_data:
		tree = input_data.read().strip()

	nwck = Newick(tree)
	genotype_prob = lambda genotype:[int(genotype.count('a') == i) for i in xrange(3)]

	# Convert the nodes with genotype names to probabilities.
	for node in [node for node in nwck.nodes if 'Node' not in node.name]:
		node.name = genotype_prob(node.name)

	# Compute the offspring genotype probabilities.
	while nwck.nodes[0].name == 'Node_0':
		for node in [node for node in nwck.nodes if 'Node' in node.name]:
			if 'Node' not in ''.join([str(nwck.nodes[i].name) for i in node.children]):
				node.name = child_prob(nwck.nodes[node.children[0]].name, nwck.nodes[node.children[1]].name)

	# Print and save the answer.
	print ' '.join(map(str,nwck.nodes[0].name))
	with open('output/082_MEND.txt', 'w') as output_data:
		output_data.write(' '.join(map(str,nwck.nodes[0].name)))
