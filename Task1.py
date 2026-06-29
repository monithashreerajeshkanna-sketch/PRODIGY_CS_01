def caesar_cipher(text, shift, mode):
    result = ""
    
    if mode == "decrypt":
        shift = -shift  # Reverse shift for decryption
    
    for char in text:
        if char.isalpha():  # Only letters shift ஆகும்
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            result += char  # Space, numbers - as is
    
    return result

# Main program
print("=== Caesar Cipher ===")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

print("\n1. Encrypt")
print("2. Decrypt")
choice = input("Choose (1/2): ")

if choice == "1":
    encrypted = caesar_cipher(message, shift, "encrypt")
    print(f"Encrypted: {encrypted}")
elif choice == "2":
    decrypted = caesar_cipher(message, shift, "decrypt")
    print(f"Decrypted: {decrypted}")
else:
    print("Invalid choice!")