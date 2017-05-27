#!/usr/local/bin/python3
def is_unique(string):
	freq = {}
	for each in string:
		if each in freq:
			return False
		else:
			freq[each] = 1
	return True

def is_permutation(string1, string2):
	cnts = {}
	for each_1 in string1:
		if each_1 in cnts:
			cnts[each_1] +=1
		else:
			cnts[each_1] = 1

	for each_2 in string2:
		if each_2 in cnts:
			cnts[each_2] -=1
		else:
			return False

	for key in cnts:
		if cnts[key] != 0:
			return False
	return True

def urlify(string):
	ret = ""
	for each in string:
		if each == " ":
			ret +="%20"
		else:
			ret +=each
	return ret

def palindrome_permutation(string1, string2):
	cnts = {}
	for each in string1:
		if each in cnts:
			cnts[each] +=1
		else:
			cnts[each] = 1

	for each_2 in string2:
		if each_2 in cnts:
			cnts[each_2] -=1
		else:
			return False
	
	odd = False
	for key in cnts:
		if cnts[key] % 2 == 1 and odd:
			return False
		else:
			odd = True
	return True

def one_away(string1, string2):
	if len(string1) != len(string2):
		return one_away_insert_or_remove(string1, string2)
	else:
		return one_away_replace(string1, string2)


def one_away_insert_or_remove(string1, string2):
	# insert a char
	cnts = {}
	num_edits = 0
	for each_1 in string1:
		if each_1 in cnts:
			cnts[each_1] +=1
		else:
			cnts[each_1] = 1

	for each_2 in string2:
		if each_2 in cnts:
			cnts[each_2] -=1
		else:
			num_edits+=1

	for key in cnts:
		if cnts[key] == 1:
			num_edits +=1

	return num_edits

def one_away_replace(string1, string2):
	cnts = {}
	num_edits = 0
	for each in string1:
		if each in cnts:
			cnts[each] +=1
		else:
			cnts[each] = 1

	for each_2 in string2:
		if each_2 not in cnts:
			num_edits +=1

	return num_edits

def string_compress(string1):
	index = 1
	current_char = string1[0]
	count = 1
	ret = ""
	length = len(string1)
	while index < length:
		if string1[index] == current_char:
			count+=1
		else:
			ret += current_char + str(count)
			count = 1
			current_char = string1[index]
		index+=1
	ret += current_char + str(count)
	return ret

# 1 2 3     7 4 1
# 4 5 6		8 5 2
# 7 8 9		9 6 3
def rotate_matrix(matrix):
	matrix_size = len(matrix)
	for i in range(0, matrix_size):
		for j in range(0, matrix_size):
			tmp = matrix[i][j]
			matrix[i][j] = matrix[j][matrix_size - 1 - i]
			matrix[j][matrix_size - 1 - i] = tmp
	return matrix

def main():
	# Is Unique
	print("Is Unique")
	print(is_unique("hello"))
	print(is_unique("hope"))

	# Is Permutation
	print("\nIs Permutation")
	print(is_permutation("dog", "god"))
	print(is_permutation("doggy", "god"))

	# URLify
	print("\nURLify")
	print(urlify("Mr John Smith"))
	print(urlify("dog is here"))

	# Palindrome Permutation
	print("\nPalindrome Permutation")
	print(palindrome_permutation("taco cat", "atco cta"))
	print(palindrome_permutation("taco", "atco cta"))

	# One Away
	print("\nOne Away")
	print(one_away("pale", "ple"))
	print(one_away("pales", "pale"))
	print(one_away("pale", "bale"))
	print(one_away("pale", "bae"))

	# String Compress
	print("\nString Compress")
	print(string_compress("aabcccccaa"))

	# Rotate Matrix
	print("\nRotate Matrix")
	print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))

if __name__ == "__main__":
	main()