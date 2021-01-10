import string
import random
import sys

"""

One-time pad encryption.

"""


ALPHABET = string.ascii_letters + string.punctuation + string.digits + ' '

def encrypt(msg, key):
    if len(msg) > len(key):
        return None

    cipher = ''
    for i in range(len(msg)):
        cipher += ALPHABET[(ALPHABET.find(msg[i]) + (ALPHABET.find(key[i]) + 1)) % len(ALPHABET)]

    return cipher

def decrypt(cipher, key):
    if len(cipher) > len(key):
        return None

    msg = ''
    for i in range(len(cipher)):
        msg += ALPHABET[(ALPHABET.find(cipher[i]) - (ALPHABET.find(key[i]) + 1))]

    return msg


def cmd_encrypt():
    msg = input("\n\t> Enter message: ")
    key = input("\t> Enter key:     ")

    cipher = encrypt(msg, key)

    while cipher is None:
        print("\tERROR: Key must be same length or longer than message.")
        cmd_encrypt()

    print(f"\n\tYour encrypted message is {cipher}")


def cmd_decrypt():
    cipher = input("\n\t> Enter cipher: ")
    key = input("\t> Enter key:    ")

    msg = decrypt(cipher, key)

    while cipher is None:
        print("\tERROR: Key must be same length or longer than cipher.")
        cmd_decrypt()

    print(f"\n\tYour decrypted message is {msg}")

def cmd_randkey():
    try:
        kLen = int(input("\n\t> Enter length of key: "))
    except Exception:
        print("\tERROR: Invalid key length.")
        cmd_randkey()

    print(f"\n\tYour key is {''.join(random.choice(ALPHABET) for _ in range(kLen))}")

def cmd_help():
    print("""
    COMMAND | DESCRIPTION
    ------------------------------------
    E       | Encrypt a message.
    D       | Decrypt a message.
    RDNK    | Generate a random key.
    HELP    | View command descriptions.
    EXIT    | Exit the program.
    """, end='')


print('Welcome!\nThis is a one-time pad encryption program.\nType "HELP" to get started.\n')

while 1:
    cmd = input("> Enter command (E/D/RNDK/HELP/EXIT): ").upper()

    if cmd == "E":
        cmd_encrypt()
    elif cmd == "D":
        cmd_decrypt()
    elif cmd == "RNDK":
        cmd_randkey()
    elif cmd == "HELP":
        cmd_help()
    elif cmd == "EXIT":
        sys.exit(0)
    else:
        print("\nERROR: Unrecognized command.")

    print()