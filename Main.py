import string

def encrypt(plain_text, shift):
    encrypted_text = ""
    alphabet = string.ascii_uppercase

    for char in plain_text:
        if char.upper() in alphabet:
            char_index = (alphabet.index(char.upper()) + shift) % 26
            encrypted_text += alphabet[char_index]
        else:
            encrypted_text += char

    return encrypted_text

def decrypt(encrypted_text, shift):
    decrypted_text = ""
    alphabet = string.ascii_uppercase

    for char in encrypted_text:
        if char.upper() in alphabet:
            char_index = (alphabet.index(char.upper()) - shift) % 26
            decrypted_text += alphabet[char_index]
        else:
            decrypted_text += char

    return decrypted_text

# Example usage
shift_amount = 3
message = string(input("Type Your Message: "))

# Encrypt the message
encrypted_message = encrypt(message, shift_amount)
print("Encrypted:", encrypted_message)

# Decrypt the encrypted message
decrypted_message = decrypt(encrypted_message, shift_amount)
print("Decrypted:", decrypted_message)
