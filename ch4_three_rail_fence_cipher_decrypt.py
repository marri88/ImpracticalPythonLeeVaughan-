r"""Decrypt a Civil War 'rail fence' type cipher.

This is for a "3-rail" fence cipher for short messages.

Example text to encrypt: 'Buy more Maine potatoes'

Rail fence style: B   O   A   P   T 
                   U M R M I E O A O S
                    Y   E   N   T   E

Read zig zag:      \  /\  /\  /\  /\  
					\/  \/  \/  \/  \/

Ciphertext: BOAPT UMRMI EOAOS YENTE

This challenge project prompt is from Chapter 4 of "Impractical Python Projects" by Lee Vaughan.

"""

import math
import itertools

#------------------------------------------------------
# USER INPUT:

# the string to be encrypted (paste between quotes):
ciphertext = """LSSEE EDTEE DTREU COSVR HRVRN RSUDR HSAEF HTEST ROTIA ENTHO EE"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!

#------------------------------------------------------

def main():
	"""Run program to decrypt 3-rail rail fence cipher."""
	message = prep_ciphertext(ciphertext)
	row1, row2, row3 = split_rails(message)
	decrypt(message, row1, row2, row3)

def prep_ciphertext(ciphertext):
	"""Remove whitespace."""
	message = "".join(ciphertext.split())
	print(f"\nciphertext = {ciphertext}")
	return message

def split_rails(message):
	"""Calculate row length for message according to 3-rail pattern."""
	if len(message) % 4 == 0:
		row_1_len = int(len(message) / 4)
		row_2_len = int(len(message) / 2)
	elif len(message) % 4 == 1:
		row_1_len = int((len(message) / 4) + 1)
		row_2_len = int(len(message) / 2)
	elif len(message) % 4 == 2:
		row_1_len = int((len(message) / 4) + 1)
		row_2_len = int((len(message) / 2) + 1)

	row1 = (message[:row_1_len])
	row2 = (message[row_1_len:(row_1_len + row_2_len)])
	row3 = (message[(row_1_len + row_2_len):])

	return row1, row2, row3

def decrypt(message, row1, row2, row3):
	"""Build list with every other letter in 2 strings & print."""
	plaintext = []

	i = 0
	while i < (len(message) / 4):
		plaintext.append(row1[i])
		plaintext.append(row2[2*i])
		plaintext.append(row3[i])
		plaintext.append(row2[(2*i)+1])
		i += 1

	if None in plaintext:
		plaintext.pop()

	print(f"rail 1 = {row1}")
	print(f"rail 2 = {row2}")
	print(f"rail 3 = {row3}")
	print(f"\nplaintext = {''.join(plaintext)}")
	
if __name__ == '__main__':
	main()
