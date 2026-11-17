import random
import string


chars = ""+ string.whitespace + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

#Encrypt
plain_text = input("enter a message to encrypt:  ")
cipher_text = ""

for char in plain_text:
    index = chars.index(char)
    cipher_text += key[index]

print (f"Original Message: {plain_text}")
print (f"Encrypted Message: {cipher_text}")

print()

#Decrypt
cipher_text = input("enter a message to decrypt:  ")
plain_text = ""

for char in cipher_text:
    index = key.index(char)
    plain_text += chars[index]

print (f"Encrypted Message: {cipher_text}")
print (f"Original Message: {plain_text}")