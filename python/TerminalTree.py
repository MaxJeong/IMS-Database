import SQL_StoredProcedures
from Input_Data import *
import sys
'''
So idea is to represent the terminal as a tree structure.
Children are stored as lists
Leaf nodes contain commands.
Regular nodes are just menus, which navigate to another menu, or a child node.
Node should always have a QuitNode 
'''
class Leaf(object):
	"""docstring for Leaf"""
	def __init__(self,description):
		super(Leaf, self).__init__()
		self.description = description
		self.parent = self

	def get_description(self):
		return (self.description)

	def execute(self,args):
		'''Leafs should contain some command
		Meant to be overridden '''
		pass

class QuitLeaf(Leaf):
	"""docstring for QuitLeaf"""
	def __init__(self):
		super(QuitLeaf, self).__init__("Quit")
		
	def execute(self):
		sys.exit()

class ReturnLeaf(Leaf):
	"""Basically a no operation leaf"""
	def __init__(self):
		super(ReturnLeaf, self).__init__("Go up a level")
		
	def execute(self):
		pass

class Node(Leaf):
	"""
	Main difference is that Nodes can have Children
	Children can be either another Node, or a Leaf
	Nodes only exist to select another Node or Leaf
	"""
	def __init__(self,description,children=[]):
		super(Node, self).__init__(description)
		self.children = children
		r = ReturnLeaf()
		for item in children:
			if isinstance(item, Node):
				item.root_children(self.parent)
			item.parent = self
		# print (self.get_options())
		r.parent = self.parent
		self.children.append(r)
		self.children.append(QuitLeaf())		

	
	def get_options(self):
		result = ""
		for i in range(0,len(self.children)):
			result = result + \
					 (("\n%d:%s") % (i+1,self.children[i].get_description()))
		return result

	def root_children(self, root):
		""" Parents need to re-root for creating tree structure"""
		self.children[len(self.children) - 2].parent = root
		self.children[len(self.children) - 2].description = "Return to " + root.description

	def get_description(self):
		return self.description
		
	def execute(self):
		return self.get_description()

	def select(self,i):
		return self.children[i]