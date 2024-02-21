def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            # Get the Unicode code point of the character
            unicode_point = ord(char)
            # Adjust the shift for uppercase or lowercase letters
            if char.isupper():
                encrypted_unicode = ((unicode_point - 65 + shift) % 26) + 65
            else:
                encrypted_unicode = ((unicode_point - 97 + shift) % 26) + 97
            encrypted_text += chr(encrypted_unicode)
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text

def decrypt_caesar_cipher(encrypted_text, shift):
    return caesar_cipher(encrypted_text, -shift)  # Decrypt by shifting in the opposite direction

def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (a number between 1 and 25): "))
    
    encrypted_text = caesar_cipher(text, shift)
    print("Encrypted text:", encrypted_text)
    
    decrypted_text = decrypt_caesar_cipher(encrypted_text, shift)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()
