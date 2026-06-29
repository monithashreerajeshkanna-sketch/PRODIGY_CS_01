# PRODIGY_CS_01
Implemented a Caesar Cipher program in Python that encrypts and decrypts user input text using a customizable shift value.

Features

Encrypts any text message using Caesar Cipher algorithm
Decrypts encrypted messages back to original text
Supports both uppercase and lowercase letters
Numbers and special characters remain unchanged
Custom shift value chosen by the user
Simple and interactive command-line interface

 How It Works

User enters a message
User enters a shift value (any number)
User chooses Encrypt or Decrypt
Each letter in the message is shifted by the given value
Encrypted/Decrypted result is displayed

 Code Explanation

- `ord(char)` converts a character into its ASCII value.
- `% 26` ensures circular shifting (after Z comes A).
- `chr()` converts the ASCII value back into a character.
- `isalpha()` checks whether the character is a letter or not.
- `isupper()` checks if the letter is uppercase or lowercase.
- `if mode == "decrypt": shift = -shift` reverses the shift value for decryption.
- Non-alphabetic characters like spaces and numbers remain unchanged.



 Technology Used
Python -  3Core programming language
ord() - Converts character to ASCII number
chr() - Converts ASCII number to character
isalpha() - Checks if character is a letter
isupper() - Checks if letter is uppercase
% (Modulo) - Handles wrap-around (Z → A)

 How to Run
 
python caesar_cipher.py

Example

Input

Enter message: Monitha Shree

Enter shift value: 4

Output

Encrypted text: Qsrmxle Wlvii

Decrypted text: Monitha Shree
