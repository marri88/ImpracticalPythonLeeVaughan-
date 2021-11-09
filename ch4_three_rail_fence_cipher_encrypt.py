r"""Encrypt a Civil War 'rail fence' type cipher.

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
#------------------------------------------------------
# USER INPUT:

# the string to be encrypted (paste between quotes):
plaintext = """Let us cross over the river and rest under the shade of the trees"""

# END OF USER INPUT - DO NOT EDIT BELOW THIS LINE!

#------------------------------------------------------

def main():
	"""Run program to encrypt message using 3-rail rail fence cipher."""
	message = prep_plaintext(plaintext)
	rails = build_rails(message)
	encrypt(rails)

def prep_plaintext(plaintext):
	"""Remove spaces & leading/trailing whitespace."""
	message = "".join(plaintext.split())
	message = message.upper() # convention for ciphertext is uppercase
	print(f"\nplaintext = {plaintext}")
	return message

def build_rails(message):
	"""Build strings from letters in the message according to pattern."""
	row_1 = message[::4]
	row_2 = message[1::2]
	row_3 = message[2::4]
	rails = row_1 + row_2 + row_3
	return rails

def encrypt(rails):
	"""Split letters in ciphertext into chunks of 5 & join to make string."""
	ciphertext = ' '.join([rails[i:i+5] for i in range(0, len(rails), 5)])
	print(f"ciphertext = {ciphertext}")

if __name__ == '__main__':
	main()