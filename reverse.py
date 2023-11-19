message = 'Reverse Ciphertext'
Plaintext = 'TonDucThangUniversity'
ciphertext = ''

i = len(Plaintext) - 1

while i >= 0:
	ciphertext  = ciphertext+Plaintext[i]
	i = i-1

print('Cipher text: ' + ciphertext)
