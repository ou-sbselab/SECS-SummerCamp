alphabet = ‘abcdefghijklmnopqrstuvwxyz’
key = int(input(‘Please enter a key value from 1-26: ’))
ciphertext = ‘’

plaintext = input(‘Please enter a message: ’)

for plain_char in plaintext:
	if plain_char in alphabet:
		plain_position = alphabet.find(plain_char)
		cipher_position = (plain_position + key) % 26
		cipher_char = alphabet[cipher_position]
		ciphertext += cipher_char
	else:
		ciphertext += plain_char
print(’Your ciphertext is:’, ciphertext)