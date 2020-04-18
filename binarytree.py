class Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, val):
		self.root = Node(val)
	def preorder_travesal(self,node):
		if node == None:
			return
		print(node.value)
		self.preorder_travesal(node.left)
		self.preorder_travesal(node.right)
	# def inorder_traversal(self, node):
	# 	if node:
	# 		self.preorder_travesal(node.left)
	# 		print(node.value)
	# 		self.preorder_travesal(node.right)

		

tree = BinaryTree(27)
tree.root.left = Node(14)
tree.root.right = Node(35)
tree.root.left.left = Node(10)
tree.root.left.right = Node(19)
tree.root.right.left = Node(31)
tree.root.right.right = Node(42)
# tree.preorder_travesal(tree.root)
# tree.inorder_traversal(tree.root)



