#!/usr/local/bin/python3

from queue import Queue

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
if __name__ == "__main__":
	main()