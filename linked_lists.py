#!/usr/local/bin/python3
class LL_Node():
	def __init__(self, data):
		self.data = data
		self.next = None

	def __str__(self):
		return str(self.data)

def print_linked_list(head):
	current = head
	while current != None:
		print(str(current.data) + " ", end=" ")
		current = current.next

def remove_dups(head):
	current = head
	cnts = {head.data : 1}
	current = current.next
	head_ptr = head
	while current != None:
		if current.data not in cnts:
			head_ptr.next = current
			head_ptr = head_ptr.next
			cnts[current.data] = 1
		current = current.next
	return head

def return_kth_last(head, k):
	slow = head
	fast = head
	for i in range(k):
		if fast == None:
			return None
		fast = fast.next
	while fast != None:
		slow = slow.next
		fast = fast.next
	return slow

def delete_middle_node(node):
	if node != None and node.next != None:
		node.data = node.next.data
		node.next = node.next.next
		return node
	else:
		return None

def main():
	# Remove duplicates in Linked List
	print("Remove duplicates in Linked List")
	head = LL_Node(5)
	head.next = LL_Node(5)
	head.next.next = LL_Node(7)
	head.next.next.next = LL_Node(3)
	head.next.next.next.next = LL_Node(7)
	head.next.next.next.next.next = LL_Node(2)
	print("Original Linked List\n")
	print_linked_list(head)
	remove_dups(head)
	print("\n\nLinked List with Duplicates Removed\n")
	print_linked_list(head)

	# Return Kth to Last
	print("\n\nReturn Kth to Last")
	head = LL_Node(5)
	head.next = LL_Node(5)
	head.next.next = LL_Node(7)
	head.next.next.next = LL_Node(3)
	head.next.next.next.next = LL_Node(7)
	head.next.next.next.next.next = LL_Node(2)
	print("Original Linked List\n")
	print_linked_list(head)
	print("\n\n3rd from Last\n")
	print(return_kth_last(head, 3))

	# Delete Middle Node
	print("\nDelete Middle Node")
	head = LL_Node(5)
	head.next = LL_Node(5)
	head.next.next = LL_Node(7)
	head.next.next.next = LL_Node(3)
	head.next.next.next.next = LL_Node(7)
	head.next.next.next.next.next = LL_Node(2)
	print("Original Linked List\n")
	print_linked_list(head)
	print("\n\nDelete middle node\n")
	delete_middle_node(head.next.next.next)
	print_linked_list(head)

if __name__ == "__main__":
	main()