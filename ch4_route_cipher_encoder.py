"""Encrypt a Union Route Cipher.

Designed for whole-word transposition ciphers with variable rows & columns. 
Assumes encryption began at either top or bottom of a column.
Key indicates the order to read columns and the direction to traverse.
Negative column numbers mean start at bottom and read up.
Positive column numbers mean start at top & read down.

Example below is for 4x4 matrix with key -1 2 -3 4.
Note "0" is not allowed.
Arrows show encryption route.

  1   2   3   4
 ___ ___ ___ ___
| ^ | | | ^ | | |
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | |
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | |
|_|_|_v_|_|_|_v_|
| ^ | | | ^ | | |
|_|_|_v_|_|_|_v_|
START        END

Required inputs - a text message, # of columns, # of rows, key string

Prints translated ciphertext, along with some intermediate steps.

This challenge project prompt is from Chapter 4 of "Impractical Python Projects" by Lee Vaughan.
"""

import sys
import string

#=========================================================================
# USER INPUT:

# the string to be decrypted:
plaintext = """We will run the batteries at Vicksburg the night of April 16 and proceed to Grand Gulf where we will reduce the forts. Be prepared to cross the river on April 25 or 29. Admiral Porter.
"""

filler_material = """This scratch sentence means absolutely nothing.
"""

# number of columns in the transposition matrix:
COLS = 6

# number of rows in the transposition matrix:
ROWS = 7

# key with spaces between numbers; negative to read UP column:
key = """ -1 3 -2 6 5 -4 """

# END OF USER INP?UT - DO NOT EDIT BELOW THIS LINE! 
#=========================================================================

def main():
	"""Run program and print decrypted plaintext."""
	print(f"\nPlaintext = {plaintext}")
	print(f"Trying {COLS} columns")
	print(f"Trying {ROWS} rows")
	print(f"Trying key {key}")
	
	# Adding filler line
	plaintext_and_filler = plaintext + filler_material

	# removing punctuation
	plaintext_no_punc = plaintext_and_filler.translate(str.maketrans('', '', string.punctuation))
	print(f"\nPlainlist with filler, no punctuation = {plaintext_no_punc}")

	# split elements into words, not letters
	plainlist = list(plaintext_no_punc.upper().split())

	# convert some words to code words
	plainlist_code = convert_code_words(plainlist)

	validate_col_row(plainlist_code)
	key_int = key_to_int(key)

	translation_matrix = build_matrix(plainlist_code)
	ciphertext = encrypt(key_int, translation_matrix)

	print("\nSuccessful encryption. Your ciphertext is:")
	print(f"\n{ciphertext}\n")

def convert_code_words(plainlist):
	"""Select words in plaintext will be converted to code words."""
	code_word_dictionary = {'BATTERIES': 'HOUNDS', 'VICKSBURG': 'ODOR', 'APRIL': 'CLAYTON',
	'16': 'SWEET', 'GRAND': 'TREE', 'GULF': 'OWL', 'FORTS': 'BAILEY', 'RIVER': 'HICKORY', 
	'25': 'MULTIPLY', '29': 'ADD', 'ADMIRAL': 'HERMES', 'PORTER': 'LANGFORD'}

	plainlist_code = []

	for item in plainlist:
		if item not in code_word_dictionary.keys():
			plainlist_code.append(item)
		else:
			value = code_word_dictionary[item]
			plainlist_code.append(value)

	return plainlist_code

def validate_col_row(plainlist_code):
	"""Check that input columns & rows are valid vs. message length."""
	factors = []
	len_plain = len(plainlist_code)
	for i in range(2, len_plain): # range excludes 1-column ciphers
		if len_plain % i == 0:
			factors.append(i)
	print(f"Length of plainlist = {len_plain}")
	print(f"Acceptable column/row values for matrix include: {factors}")
	print()
	if ROWS * COLS != len_plain:
		print("\nError - Input columns & rows not factors of length "
			"of cipher. Terminating program.")
		sys.exit(1)

def key_to_int(key):
	"""Turn key into list of integers & check validity."""
	key_int = [int(i) for i in key.split()]
	key_int_lo = min(key_int)
	key_int_hi = max(key_int)
	print(f"List key is: {key_int}")
	if len(key_int) != COLS or key_int_lo < -COLS or key_int_hi > COLS \
		or 0 in key_int:
		print("\nError - Problem with key. Terminating.")
		sys.exit(1)
	else:
		return key_int

def build_matrix(plainlist_code):
	"""Use a list of lists as a COLS x ROWS matrix to hold plaintext."""
	translation_matrix = [[None] * COLS] * ROWS

	i = 0
	while i <= ROWS - 1:
		value = COLS * i
		translation_matrix[i] = plainlist_code[value:value+6]
		i += 1
	
	return translation_matrix

def encrypt(key_int, translation_matrix):
	"""Use index slicing to add select words in nested lists to ciphertext string according to key."""
	ciphertext = ''

	for key in key_int:
		if key > 0:
			i = 0
			while i <= ROWS - 1:
				word = str(translation_matrix[i][key-1])
				ciphertext += word + ' '
				i += 1
		else:
			j = 0
			while j <= ROWS - 1:
				word = str(translation_matrix[ROWS-1-j][(key*-1) - 1])
				ciphertext += word + ' '
				j += 1

	return ciphertext 

if __name__ == '__main__':
	main()

