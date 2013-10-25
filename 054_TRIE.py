#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Introduction to Pattern Matching
Rosalind ID: TRIE
Rosalind #: 054
URL: http://rosalind.info/problems/trie/
'''

class Trie(object):
    '''Constructs a Trie'''
    def __init__(self):
        self.nodes = [[Node('', 1)]]
        self.edges = []

    def addWord(self, word):
    	if type(word) == list:
    		for w in word:
    			self.addWord(w)
    	else:
	        parent = self.findParent(word)
	        for i in range(len(parent.prefix), len(word)):
	            new_node = Node(word[:i+1], self.nodeCount()+1)
	            self.edges.append(Edge(word[i], parent.number, self.nodeCount()+1))
	            self.insertNode(new_node)
	            parent = new_node

    def insertNode(self, node):
        if node.depth > self.depth():
            self.nodes.append([node])
        else:
            self.nodes[node.depth].append(node)

    def depth(self):
        '''Returns the depth of the trie.'''
        return len(self.nodes) - 1

    def nodeCount(self):
        count = 0
        for trie_depth in self.nodes:
            count += len(trie_depth)
        return count

    def findParent(self, word):
        '''Return the parent node of the word to be inserted.'''
        for i in range(min(len(word), self.depth()), 0,-1):
            for node in self.nodes[i]:
                if word[:i] == node.prefix:
                    return node

        return self.nodes[0][0]

class Node(object):
    '''Trie Node'''
    def __init__(self, prefix, number):
        self.prefix = prefix
        self.number = number
        self.depth = len(prefix)

class Edge(object):
    '''Trie Edge'''
    def __init__(self, letter, par_node, chi_node):
        self.letter = letter
        self.parent_node = par_node
        self.child_node = chi_node

    def getInfo(self):
    	return ' '.join(map(str,[self.parent_node,self.child_node,self.letter]))

if __name__ == '__main__':
	
	with open('data/rosalind_trie.txt') as input_data:
		dna = [line.strip() for line in input_data.readlines()]

	myTrie = Trie()
	myTrie.addWord(dna)

	adjacency_list = []
	for edge in myTrie.edges:
		adjacency_list.append(edge.getInfo())

	print '\n'.join(adjacency_list)
	with open('output/054_TRIE.txt', 'w') as output_file:
		output_file.write('\n'.join(adjacency_list))