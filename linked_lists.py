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

def sum_linked_list(head, head2):
	carry = 0
	current_head1 = head
	current_head2 = head2
	ret_sum = None
	ret_sum_ptr = None
	while current_head1 != None or current_head2 != None:
		node_sum = carry
		if current_head1 != None:
			node_sum += current_head1.data
		if current_head2 != None:
			node_sum += current_head2.data
		to_add = node_sum % 10 if current_head1 != None or current_head2 != None else node_sum
		if(ret_sum):
			ret_sum_ptr.next = LL_Node(to_add)
			ret_sum_ptr = ret_sum_ptr.next
		else:
			ret_sum = LL_Node(to_add)
			ret_sum_ptr = ret_sum
		
		current_head1 = current_head1.next if current_head1 != None else None
		current_head2 = current_head2.next if current_head2 != None else None
		carry = node_sum // 10
	return ret_sum
# 6 1 7
#   9 5
# 7 1 2
def sum_linked_list_reverse(head, head2):
	pass

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

	# Partition Linked List
	print("\n\nPartition Linked List")
	print("PASS: no idea what the question is asking\n")

	# Sum Linked List
	print("\nSum Linked List")
	head = LL_Node(7)
	head.next = LL_Node(1)
	head2 = LL_Node(5)
	print_linked_list(sum_linked_list(head, head2))

	# Sum Linked List (Reverse)
	print("\nSum Linked List (Reverse)")
	head = LL_Node(7)
	head.next = LL_Node(1)
	head2 = LL_Node(5)
	# print_linked_list(sum_linked_list_reverse(head, head2))

if __name__ == "__main__":
	main()