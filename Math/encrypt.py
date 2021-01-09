import string
import random

"""

One-time pad encryption.

"""


ALPHABET = string.ascii_letters + string.punctuation + ' '

def encrypt(msg, key):
    if len(msg) > len(key):
        print("Length of key must be greater than or equal to length of message.")

    cipher = ''
    for i in range(len(msg)):
        cipher += ALPHABET[(ALPHABET.find(msg[i]) + (ALPHABET.find(key[i]) + 1)) % len(ALPHABET)]

    return cipher

def decrypt(cipher, key):
    if len(cipher) > len(key):
        print("Length of key must be greater than or equal to length of cipher.")

    msg = ''
    for i in range(len(cipher)):
        msg += ALPHABET[(ALPHABET.find(cipher[i]) - (ALPHABET.find(key[i]) + 1))]

    return msg

msg = """In physics, a quantum is the minimum amount of any physical entity 
involved in an interaction. The fundamental notion that a physical 
property can be "quantized" is referred to as "the hypothesis of quantization".
"""

rand_key = ''.join(random.choice(ALPHABET) for _ in range(len(msg))) # Generate a random key the same length as the message.

cipher = encrypt(msg, rand_key) # Encrypt the message with the random key.

print(cipher)

print(decrypt(cipher, rand_key)) # Decrypt the message with the random key.

