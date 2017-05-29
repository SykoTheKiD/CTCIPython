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

def check_palindrome(head):
	if head == None:
		return False
	else:
		slow, fast = head, head
		stack = []
		while fast != None and fast.next != None:
			stack.append(slow.data)
			slow = slow.next
			fast = fast.next.next
		slow = slow.next
		while len(stack) > 0:
			current_stack = stack.pop()
			current_list = slow.data
			if current_list != current_stack:
				return False
			slow = slow.next
		return True

def intersection(head, head2):
	len_head  = 0
	head_1 = head
	while head_1 != None:
		len_head +=1
		head_1 = head_1.next

	len_head2 = 0
	head_2 = head2
	while head_2 != None:
		len_head2 +=1
		head_2 = head_2.next

	longest = max(len_head, len_head2)
	shortest = min(len_head, len_head2)
	longest_list = head if len_head > len_head2 else head2
	shortest_list = head if len_head < len_head2 else head2

	for i in range(longest-shortest):
		longest_list = longest_list.next

	while longest_list != None and shortest_list != None:
		if longest_list == shortest_list:
			return longest_list
		longest_list = longest_list.next
		shortest_list = shortest_list.next
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

	# Partition Linked List
	print("\n\nPartition Linked List")
	print("PASS: no idea what the question is asking\n")

	# Sum Linked List
	print("\nSum Linked List")
	head = LL_Node(7)
	head.next = LL_Node(1)
	head2 = LL_Node(5)
	print_linked_list(sum_linked_list(head, head2))

	# Palindrome
	print("\nPalindrome\n")
	head = LL_Node("r")
	head.next = LL_Node("a")
	head.next.next = LL_Node("c")
	head.next.next.next = LL_Node("e")
	head.next.next.next.next = LL_Node("c")
	head.next.next.next.next.next = LL_Node("a")
	head.next.next.next.next.next.next = LL_Node("r")
	print(check_palindrome(head))

	# Intersection
	print("\nIntersection\n\n")
	head = LL_Node(3)
	head.next = LL_Node(1)
	head.next.next = LL_Node(5)
	head.next.next.next = LL_Node(9)
	intersect = LL_Node(7)
	head.next.next.next.next = intersect
	intersect.next = LL_Node(2)
	intersect.next.next = LL_Node(1)
	head2 = LL_Node(4)
	head2.next= LL_Node(6)
	head2.next.next = intersect
	print(intersection(head, head2))
if __name__ == "__main__":
	main()