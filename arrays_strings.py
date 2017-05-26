def is_unique(string):
	char = string[0]
	for i in range(1, len(string)):
		char = char != string[i]
	return char


def main():
	# Is Unique
	print(is_unique("hello"))
	print(is_unique("hope"))

if __name__ == "__main__":
	main()
