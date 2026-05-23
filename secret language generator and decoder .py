#make a secret language generator or decoder 

import base64

def encrypt(message, key):
    encrypted = ""

    for i in range(len(message)):
        char = message[i]
        key_char = key[i % len(key)]

        value = (ord(char) + ord(key_char)) % 256
        encrypted += chr(value)

    return base64.b64encode(encrypted.encode()).decode()


def decrypt(encrypted, key):
    encrypted = base64.b64decode(encrypted).decode()

    decrypted = ""

    for i in range(len(encrypted)):
        char = encrypted[i]
        key_char = key[i % len(key)]

        value = (ord(char) - ord(key_char)) % 256
        decrypted += chr(value)

    return decrypted

choice = input("Enter ENCRYPT or DECRYPT: ").upper()

if choice not in ["ENCRYPT", "DECRYPT"]:
    raise ValueError("Invalid choice!")

key = input("Enter secret key: ")

if choice == "ENCRYPT":
    message = input("Enter message: ")
    encrypted = encrypt(message, key)
    print("Encrypted message:", encrypted)

elif choice == "DECRYPT":
    encrypted = input("Enter encrypted message: ")
    decrypted = decrypt(encrypted, key)
    print("Decrypted message:", decrypted)
