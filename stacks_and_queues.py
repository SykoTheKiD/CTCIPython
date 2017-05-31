#!/usr/local/bin/python3
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

if __name__ == "__main__":
	main()