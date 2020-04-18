class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None
	def insert(self,node, data):
		if node.root == None:
			node.root = Node(data)
		else:
			if data<node.data:
				p.left = insert(p.left, data)
			elif data>node.data:
				p.right = insert(p.right, data)
			return p

	def search(self, root, key):
		if root == None or root.data == key:
			return root
		

o = BST()
o.insert(o.root, 10)


