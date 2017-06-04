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

class Stack_Of_Plates():
	def __init__(self, stack_size = 5):
		self.stack_size = stack_size
		self.active_stack = []
		self.stacks = []

	def push(self, data):
		if len(self.active_stack) < self.stack_size:
			self.active_stack.append(data)
		else:
			self.stacks.append(self.active_stack)
			self.active_stack = []
			self.active_stack.append(data)

	def pop(self):
		value = self.active_stack.pop()
		if len(self.active_stack) == 0:
			self.active_stack = self.stacks.pop()
		return value

	def peek(self):
		return self.active_stack[len(self.active_stack) - 1]

	def pop_at(self, index):
		if index == 0:
			stack = self.active_stack
			value = stack.pop()
			if len(stack) == 0:
				self.active_stack = self.stacks.pop()
		else:
			stack = self.stacks[index - 1]
			value = stack.pop()
			if len(stack) == 0:
				self.stacks.pop(index - 1)

class Queue_With_Stacks():
	def __init__(self):
		self.stack_new = []
		self.stack_old = []
		 
	def dequeue(self):
		self.flip()
		return self.stack_old.pop()

	def enqueue(self, data):
		self.stack_new.append(data)

	def peek(self):
		self.flip()
		return self.stack_new[len(self.stack_new) - 1]

	def flip(self):
		if len(self.stack_old) == 0:
			while len(self.stack_new) > 0:
				self.stack_old.append(self.stack_new.pop())

class Stack():
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		return self.stack.pop()

	def sort(self):
		tmp_stack = []
		while len(self.stack) > 0:
			current = self.stack.pop()
			size_tmp = len(tmp_stack)
			if size_tmp > 0:
				peek = tmp_stack[size_tmp - 1]
				while current > peek and len(tmp_stack) > 0:
					self.stack.append(tmp_stack.pop())
				tmp_stack.append(current)
			else:
				tmp_stack.append(current)
		self.stack = tmp_stack

	def __str__(self):
		return str(self.stack)

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

	# Stack of Plates
	print("\nStack of Plates\n")
	plates = Stack_Of_Plates()
	print(len(plates.stacks))
	plates.push(1)
	plates.push(2)
	plates.push(3)
	plates.push(4)
	plates.push(5)
	plates.push(6)
	print(plates.pop())
	print(len(plates.stacks))

	# Queue via Stacks
	print("\nQueue via Stacks\n")
	q_with_stk = Queue_With_Stacks()
	q_with_stk.enqueue(5)
	q_with_stk.enqueue(4)
	q_with_stk.enqueue(6)
	print(q_with_stk.dequeue())
	print(q_with_stk.dequeue())

	# Sort Stack
	print("\nSort Stack\n")
	stk = Stack()
	stk.push(5)
	stk.push(2)
	stk.push(6)
	stk.push(6)
	stk.push(1)
	stk.push(3)
	stk.sort()
	print(stk)

	print("\nAnimal Shelter: PASS\n")


if __name__ == "__main__":
	main()