#!/usr/bin/env python
'''A ROSALIND bioinformatics script containing useful data structures.'''

class SuffixTree(object):
	'''Suffix Tree Class'''
	def __init__(self):
		self.nodes = [self.Node(None,0)]
		self.edges = dict()


	class Node(object):
	    '''Suffix Tree Node'''
	    def __init__(self, parent, number):
	        self.parent = parent
	        self.number = number
	        self.children = []

	    def addChild(self, child):
	    	self.children.append(child)

	    def removeChild(self, child):
	    	self.children.remove(child)

	    def updateParent(self, parent):
	    	self.parent = parent


	def addWord(self, word):
		'''Add a word to the suffix tree'''
		# Check to make sure word ends in '$'.
		if word[-1] != '$':
			word += '$'

		for suff in [word[i:] for i in xrange(len(word))]:
			parent_node, edge_name, overlap = self.insertPosition(suff, self.nodes[0])

			if overlap:
				previous_edge = self.edges[(parent_node.parent.number, parent_node.number)]
				
				# Get the prefix overlap
				pre_overlap = ''
				i = 0
				while edge_name[i] == previous_edge[i]:
					pre_overlap += edge_name[i]
					i+=1

				# CHANGE CHILDREN HERER???????

				# Create a new node for insertion
				new_node = self.Node(parent_node.parent,len(self.nodes))
				new_node.addChild(parent_node)
				self.addNode(parent_node.parent, pre_overlap, new_node)

				# Update the parent node since a new node is inserted above it
				del self.edges[(parent_node.parent.number, parent_node.number)]
				parent_node.parent.removeChild(parent_node)
				parent_node.updateParent(new_node)
				self.edges[(parent_node.parent.number, parent_node.number)] = previous_edge[len(pre_overlap):]
				
				# Add new child node
				self.addNode(new_node, edge_name[len(pre_overlap):])

			else:
				self.addNode(parent_node, edge_name)

	def insertPosition(self, suff, parent_node):
		for child_node in parent_node.children:
			edge = self.edges[(parent_node.number,child_node.number)]
			if suff[:len(edge)] == edge:
				return self.insertPosition(suff[len(edge):], child_node)

			elif edge[0] == suff[0]:
				return child_node, suff,  True

		return parent_node, suff, False	

	def addNode(self, parent_node, edge_name, child_node=None):
		# Create child node, if necessary
		if child_node == None:
			child_node = self.Node(parent_node, len(self.nodes))
		# Add node to node list
		self.nodes.append(child_node)
		# Add child to parent
		parent_node.addChild(child_node)
		# Add edge to edge dict
		self.edges[(parent_node.number,child_node.number)] = edge_name
		# print self.edges
		# print [(n.number, n.parent.number) for n in self.nodes if n.parent != None]
