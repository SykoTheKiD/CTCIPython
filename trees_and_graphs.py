#!/usr/local/bin/python3

from queue import Queue

class Node():
	def __init__(self, data):
		self.data = data
		self.connections = []
		self.visited = False

	def connect(self, node):
		self.connections.append(node)

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

def main():
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

if __name__ == "__main__":
	main()