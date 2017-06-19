#!/usr/local/bin/python3

from queue import Queue
import sys

class Node():
	def __init__(self, data):
		self.data = data
		self.connections = []

	def connect(self, node):
		self.connections.append(node)

class Binary_Node():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.data)

class Binary_Node_Parent():
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
		self.parent = None

	def __str__(self):
		return str(self.data)

class LL_Node():
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)

class Custom_Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __str__(self):
    	return str(self.items)

def route_between_nodes(node1, node2):
	queue = Queue()
	queue.put(node1)
	while not queue.empty():
		current = queue.get()
		if node2 in current.connections:
			return True
		else:
			for each_node in current.connections:
				queue.put(each_node)
	return False

def array_to_tree(arr):
	if len(arr) == 0:
		return None
	elif len(arr) == 1:
		return Binary_Node(arr[0])
	else:
		mid_index = len(arr) // 2
		mid = arr[mid_index]
		root = Binary_Node(mid)
		root.left = array_to_tree(arr[:mid_index])
		root.right = array_to_tree(arr[mid_index:])
		return root

def print_tree(tree):
	if tree == None:
		return None
	else:
		print(tree.data)
		print_tree(tree.left)
		print_tree(tree.right)

def get_height(root):
	if root == None:
		return 0
	else:
		return 1 + max(get_height(root.left), get_height(root.right))

def check_balanced(root):
	if root == None:
		return True
	else:
		left_height = get_height(root.left)
		right_height = get_height(root.right)
		if abs(left_height - right_height) > 1:
			return False
		else:
			return check_balanced(root.left) and check_balanced(root.right)

def get_height_better(root):
	if root == None:
		return -1
	else:
		int left_height = get_height_better(root.left)
		if left_height == -sys.maxsize:
			return -sys.maxsize
		int right_height = get_height_better(root.right)
		if right_height == -sys.maxsize:
			return -sys.maxsize

		int diff = left_height - right_height
		if abs(diff) > 1:
			return -sys.maxsize
		else:
			return max(left_height, right_height) + 1

def check_balanced_better(root):
	return get_height_better(root) != -sys.maxsize

def validate_bst(root):
	return validate_bst_helper(root, None, None)

def validate_bst_helper(root, minimum, maximum):
	if root == None:
		return True
	if (minimum != None and root.data <= minimum) and (maximum != None and root.data > maximum):
		return False
	if not validate_bst_helper(root.left, minimum, root.data) or not validate_bst_helper(root.right, root.data, maximum)
		return False
	return True

def in_order_successor_parent(node):
	if node == None:
		return None
	else:
		if node.right != None:
			return left_most(node.right)
		else:
			current = node
			parent = node.parent
			while parent != None and parent.left != current:
				current = parent
				parent = parent.parent
			return parent

def left_most(node):
	if node == None:
		return None
	else:
		while node.left != None:
			node = node.left
		return node

def main():
	# Route between two nodes
	print("Route between two nodes\n\n")
	a = Node('a')
	b = Node('a')
	c = Node('a')
	d = Node('a')
	e = Node('a')
	f = Node('a')
	a.connections.append(b)
	b.connections.append(c)
	c.connections.append(e)
	e.connections.append(d)
	e.connections.append(f)
	d.connections.append(b)
	print(route_between_nodes(a, f))

	# Minimal Tree
	print("Minimal Tree\n")
	arr = [1,2,3,4,5,6]
	tree = array_to_tree(arr) 
	print_tree(tree)

	# List of Depths 
	print("\nList of Depths: SKIP\n")

	# Check Balanced
	print("\nCheck Balanced\n")
	root = Binary_Node(2)
	node1 = Binary_Node(7)
	node2 = Binary_Node(5)
	node3 = Binary_Node(2)
	node4 = Binary_Node(6)
	node5 = Binary_Node(9)
	node6 = Binary_Node(5)
	node7 = Binary_Node(11)
	node8 = Binary_Node(4)

	root.left = node1
	root.right = node2
	root.left.left = node3
	root.left.right = node4
	root.right.right = node5
	root.right.right.left = node8
	root.left.right.left = node6
	root.left.right.right = node7
	print(check_balanced_better(root))

	# Validate BST
	print("Validate BST\n")
	root = Binary_Node(27)
	node1 = Binary_Node(14)
	node2 = Binary_Node(35)
	node3 = Binary_Node(10)
	node4 = Binary_Node(19)
	node5 = Binary_Node(42)
	node6 = Binary_Node(31)

	root.left = node1
	root.right = node2
	root.left.left = node3
	root.left.right = node4
	root.right.right = node5
	root.right.right.left = node8
	root.right.left = node6

	print(validate_bst(root))

	# Successor
	print("Successor\n")
	root = Binary_Node_Parent(20)
	node1 = Binary_Node_Parent(8)
	node1.parent = root
	node2 = Binary_Node_Parent(22)
	node2.parent = root

	node4 = Binary_Node_Parent(4)
	node4.parent = node1
	node1.left = node4
	node12 = Binary_Node_Parent(12)
	node12.parent = node1

	node10 = Binary_Node_Parent(10)
	node10.parent = node12
	node14 = Binary_Node_Parent(14)
	node14.parent = node12
	node12.left = node10
	node12.right = node14
	node1.right = node12

	print(in_order_successor_parent(root))

	# Build Order
	print("\nBuild Order")
	print("\nSKIP: Use Topological Sort on a DAG or use DFS")

if __name__ == "__main__":
	main()