"""
Find palindromes recursively from a dictionary file.
This challenge project prompt is from Chapter 2 of "Impractical Python Projects" by Lee Vaughan.
"""

import sys

def load(file):
	"""Open a text file & return a list of lowercase strings."""
	try:
		with open(file) as in_file:
			loaded_txt = in_file.read().strip().split('\n')
			loaded_txt = [x.lower() for x in loaded_txt]
			return loaded_txt
	except IOError as e:
		print("{}\nError opening {}. Terminating program.".format(e, file))
		sys.exit(1)

def isPalindrome(word):
	"""Checks first and last letter of word."""
	if len(word) <= 1:
		return True
	elif word[0] == word[(len(word) - 1)]:
		return isPalindrome(word[1:(len(word) - 1)])
	else:
		return False

def main():
	""" """
	word_list = load('2of4brif.txt')
	palindrome_list = []

	for word in word_list:
		if isPalindrome(word): 
			palindrome_list.append(word)

	print(f"\nNumber of palindromes found = {len(palindrome_list)}")
	print(*palindrome_list, sep='\n')

if __name__ == '__main__':
	main()