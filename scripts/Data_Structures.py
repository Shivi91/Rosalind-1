#!/usr/bin/env python
'''A ROSALIND bioinformatics script containing useful data structures.'''

class SuffixTree(object):
	'''Creates a suffix tree for the provided word.'''
	def __init__(self, word):
		'''Initializes the suffix tree.'''
		self.nodes = [self.Node(None,0)]
		self.edges = dict()
		if type(word) == str:
			self.addWord(word)

	class Node(object):
	    '''Suffix tree node class.'''
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
		'''Add a word to the suffix tree.'''
		# Check to make sure word ends in '$'.
		if word[-1] != '$':
			word += '$'
		self.word = word
		self.n = len(self.word)

		for i in xrange(self.n):
			parent_node, edge_start, overlap = self.insertPosition(i,self.nodes[0])

			if overlap:
				p_edge_start, p_edge_end = self.edges[(parent_node.parent.number, parent_node.number)]
				
				# Get the edge to insert
				insert_len = 0
				while word[edge_start:edge_start+insert_len] == word[p_edge_start:p_edge_start+insert_len]:
					insert_len += 1

				# Create a new node for insertion
				new_node = self.Node(parent_node.parent,len(self.nodes))
				new_node.addChild(parent_node)
				self.addNode(parent_node.parent, p_edge_start, p_edge_start + insert_len-1, new_node)

				# Update the parent node since a new node is inserted above it
				del self.edges[(parent_node.parent.number, parent_node.number)]
				parent_node.parent.removeChild(parent_node)
				parent_node.updateParent(new_node)
				self.edges[(parent_node.parent.number, parent_node.number)] = [p_edge_start + insert_len-1, p_edge_end]
				
				# Add new child node
				self.addNode(new_node, edge_start + insert_len-1, self.n)

			else:
				# No insertion necessary, just append the new node.
				self.addNode(parent_node, edge_start, self.n)

	def insertPosition(self, start_index, parent_node):
		'''Determine the location and method to insert a suffix into the suffix tree.'''
		for child_node in parent_node.children:
			edge_start, edge_end = self.edges[(parent_node.number,child_node.number)]
			if self.word[start_index:start_index+edge_end-edge_start] == self.word[edge_start:edge_end]:
				return self.insertPosition(start_index+edge_end-edge_start, child_node)

			elif self.word[edge_start] == self.word[start_index]:
				return child_node, start_index,  True

		return parent_node, start_index, False	

	def addNode(self, parent_node, edge_start, edge_end, child_node=None):
		'''Adds a node and the associated edge to the suffix tree.'''
		# Create child node, if necessary
		if child_node == None:
			child_node = self.Node(parent_node, len(self.nodes))
		# Add node to node list
		self.nodes.append(child_node)
		# Add child to parent
		parent_node.addChild(child_node)
		# Add edge to edge dict
		self.edges[(parent_node.number,child_node.number)] = [edge_start, edge_end]

	def printEdges(self):
		'''Returns the string representations of the edges.'''
		return [self.word[i:j] for i,j in self.edges.values()]


class Trie(object):
	'''Constructs a trie.'''
	def __init__(self, word=None):
		self.nodes = [[self.Node('', 1)]]
		self.edges = []
		if word != None:
			self.addWord(word)

	class Node(object):
		'''Trie node class.'''
		def __init__(self, prefix, number):
			self.prefix = prefix
			self.number = number
			self.depth = len(prefix)

	class Edge(object):
		'''Trie edge class.'''
		def __init__(self, letter, par_node, chi_node):
			self.letter = letter
			self.parent_node = par_node
			self.child_node = chi_node

		def getInfo(self):
			'''Return the edge information compactly.'''
			return ' '.join(map(str,[self.parent_node,self.child_node,self.letter]))

	def addWord(self, word):
		'''Adds a word to the trie.'''
		if type(word) == list:
			for w in word:
				self.addWord(w)
		else:
			parent = self.findParent(word)
			for i in range(len(parent.prefix), len(word)):
				new_node = self.Node(word[:i+1], self.nodeCount()+1)
				self.edges.append(self.Edge(word[i], parent.number, self.nodeCount()+1))
				self.insertNode(new_node)
				parent = new_node

	def insertNode(self, node):
		'''Determine the location to insert the current node.'''
		if node.depth > self.depth():
			self.nodes.append([node])
		else:
			self.nodes[node.depth].append(node)

	def depth(self):
		'''Returns the depth of the trie.'''
		return len(self.nodes) - 1

	def nodeCount(self):
		'''Returns the total number of nodes.'''
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

class Newick(object):
	'''Creates a Newick Tree from the given data.'''
	def __init__(self, data):
		'''Initialize the Newick Tree.'''
		self.nodes = []
		self.node_index = 0
		self.edges = []
		self.construct_tree(data)
		self.name_index = {node.name:node.number for node in self.nodes}


	class Node(object):
		'''Node class for Newick Trees.'''
		def __init__(self, number, parent, name = None):
			'''Node initialization.'''
			self.number = number
			self.parent = parent
			self.children = []
			self.name = [name, 'Node_'+str(self.number)][name==None]

        	def __repr__(self):
			'''Defines how Node instances are printed.'''
			children_names = '('+', '.join(map(str, self.children))+')'
			return self.name+children_names

		def add_child(self, child):
			'''Add a child to the node.'''
			self.children.append(child)


	def construct_tree(self, data):
		'''Constructs the Newick Tree.'''
		data = data.replace(',', ' ').replace('(', '( ').replace(')', ' )').strip(';').split()
		current_parent = self.Node(-1,None)
		for item in data:
			if item[0] == '(':
				current_parent = self.Node(len(self.nodes), current_parent.number)
				self.nodes.append(current_parent)
				if len(self.nodes) > 1:
					self.nodes[current_parent.parent].add_child(current_parent.number)
					self.edges.append((current_parent.parent,current_parent.number))

			elif item[0] == ')':
				if len(item) > 1:
					current_parent.name = item[1:]
				current_parent = self.nodes[current_parent.parent]


			else:
				self.nodes[current_parent.number].add_child(len(self.nodes))
				self.edges.append((current_parent.number, len(self.nodes)))
				self.nodes.append(self.Node(len(self.nodes), current_parent.number, item))

	def edge_names(self):
		'''Return a list of edges referencing node names.'''
		return [str((self.nodes[edge[0]].name, self.nodes[edge[1]].name)) for edge in self.edges]

	def distance(self, name1, name2):
		'''Returns the distance between name1 and name2.'''
		if name1 == name2:
			return 0

		#Create the branches from the two desired nodes to the root.
		branch1 = [self.name_index[name1]]
		branch2 = [self.name_index[name2]]
		while self.nodes[branch1[-1]].parent != -1:
			branch1.append(self.nodes[branch1[-1]].parent)
		while self.nodes[branch2[-1]].parent != -1:
			branch2.append(self.nodes[branch2[-1]].parent)

		return len(branch1) + len(branch2) - 2*len(set(branch1)&set(branch2))
