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
		# insert a char
		# remove a char
		# replace a char

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
	print(one_away("taco cat", "atco cta"))
	print(one_away("taco", "atco cta"))

if __name__ == "__main__":
	main()
