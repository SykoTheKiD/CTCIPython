#!/usr/local/bin/python3

import sys

class ThreeStacks():
	def __init__(self, stack_size, num_stacks = 3):
		self.stacks = []
		self.sizes = {}
		self.num_stacks = num_stacks
		self.stack_size = stack_size
		self.empty = '-'
		for i in range(num_stacks):
			self.sizes[i] = 0
		for j in range(stack_size * num_stacks):
			self.stacks.append(self.empty)

	def pop(self, stack_number):
		if self.is_empty(stack_number):
			raise Exception("Stack Underflow")
		else:
			index = self.get_index(stack_number)
			value = self.stacks[index]
			self.stacks[index] = self.empty
			self.sizes[stack_number] -= 1
			return value

	def push(self, value, stack_number):
		print("PUSH: " + str(value) + " to Stack: " + str(stack_number))
		if self.is_full(stack_number):
			raise Exception("Stack Overflow")
		else:
			self.sizes[stack_number] += 1
			self.stacks[self.get_index(stack_number)] = value

	def is_empty(self, stack_number):
		return self.sizes[stack_number] == 0

	def peek(self, stack_number):
		if self.is_empty(stack_number):
			raise Exception("Stack Underflow")
		else:
			return self.stacks[get_index(stack_number)]

	def is_full(self, stack_number):
		return self.sizes[stack_number] == self.stack_size

	def get_index(self, stack_number):
		factor = stack_number * self.stack_size
		size = self.sizes[stack_number]
		return factor + size - 1

class Stack_Min():
	def __init__(self):
		self.stack = []

	def push(self, data):
		old_min_value = self.get_min()
		new_min_value = min(data, old_min_value)
		obj = Stack_Object(data, new_min_value)
		self.stack.append(obj)

	def pop(self):
		if len(self.stack) == 0:
			raise Exception("Stack Underflow")
		else:
			self.stack.pop()

	def is_empty(self):
		return len(self.stack) == 0

	def peek(self):
		return self.stack[len(self.stack) - 1]

	def get_min(self):
		if self.is_empty():
			return sys.maxsize
		else:
			return self.peek().min_value

class Stack_Object():
	def __init__(self, data, min_value):
		self.data = data
		self.min_value = min_value

	def __str__(self):
		return str(self.data)

def main():
	# Andre 3000
	print("Andre 3000\n\n")
	three_stack = ThreeStacks(4)
	three_stack.push(1, 1)
	three_stack.push(2, 2)
	three_stack.push(3, 1)
	three_stack.push(4, 1)
	try:
		three_stack.push(5, 1)
	except Exception:
		print("Stack Overflow")

	print(three_stack.pop(1))

	# Min Stack
	print("\nMin Stack\n")
	min_stack = Stack_Min()
	min_stack.push(2)
	min_stack.push(8)
	min_stack.push(5)
	min_stack.push(1)
	min_stack.pop()
	print(min_stack.peek())
	print(min_stack.get_min())

if __name__ == "__main__":
	main()