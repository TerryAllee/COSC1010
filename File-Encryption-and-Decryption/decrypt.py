#
# Name: Terry Allee
# Date: Novmeber 24th 
# File Encryption and Decryption Programming Project
# COSC 1010 
#
# Use comments liberally throughout the program. 

# Part 2 decrypt.py

import os
print("Current Working Directory:", os.getcwd())
print("Files in Directory:", os.listdir(os.getcwd()))

# Encryption program

# Dictionary for character encodiing
CODE = {
        'A': '%', 'a': '9', 'B': '@', 'b': '#',
        'C': '&', 'c': '1', 'D': '*', 'd': '2',
        'E': '3', 'e': '^', 'F': '4', 'f': '(',
        'G': '5', 'g': ')', 'H': '_', 'h': '6',
        'I': '+', 'i': '7', 'J': '-', 'j': '8',
        'K': '=', 'k': '[', 'L': '{', 'l': '}',
        'M': '0', 'm': '!', 'N': ']', 'n': '|',
        'O': ':', 'o': ';', 'P': '"', 'p': '<',
        'Q': '>', 'q': '/', 'R': '~', 'r': '`',
        'S': ',', 's': '.', 'T': 'z', 't': 'x',
        'U': 'v', 'u': 'u', 'V': 't', 'v': 's',
        'W': 'r', 'w': 'q', 'X': 'p', 'x': 'o',
        'Y': 'n', 'y': 'm', 'Z': 'l', 'z': 'k',
        ' ': '_', '\n': '\n','!': 'A', '@': 'B',
        '#': 'C', '$': 'D', '%': 'E', '^': 'F',
        '&': 'G', '*': 'H', '(': 'I', ')': 'J',
        '_': 'K', '-': 'L', '=': 'M', '+': 'N',
        '~': 'O', '`': 'P', '|': 'Q', ':': 'R',
        ';': 'S', '"': 'T', '<': 'U', '>': 'V',
        '/': 'W', ',': 'X', '.': 'Y', 'z': 'Z'
}

# Reverse the dictionary
REVERSE_CODE = {v: k for k, v in CODE.items()}

def decrypt():
    # Ask the user for the encrypted file name
    input_name = input("Enter the name of the encrypted file: ").strip()
    if not os.path.exists(input_name):
        print(f"Error: The file '{input_name}' does not exist.")
        return

    try:
        # open encrypted file
        with open(input_name, 'r') as file:
            encrypted_text = file.read()
    except Exception as e:
        print(f"Error reading the file: '{e}")
        return None
    
    #Decrypt the contents
    decrypted_text = ''   
    for char in encrypted_text:
        if char.isspace():
            # Keep spaces and newlines as they are in the text. 
            decrypted_text += char
        else:
            # Get mapped character
            # Replace unmapped characters with a ?
            mapped_char = REVERSE_CODE.get(char, '?')
            decrypted_text += mapped_char

            
    # Show the decrypted text on the screen
    print("\nDecrypted Text:")
    print(decrypted_text)
    return decrypted_text


def main():
    # obtain the decrpted text.
    result = decrypt()

    # Exit if the decrypion fails.
    if result is None:
        return
    
    # Write the decrypted text to the screen
    print("\nDecrypted Text:" )
    print(result)

    # Save to a decrypted text file
    output_name = input('Enter the name of the output file:').strip()
     # Write the decrypted text for the output file
    with open(output_name, 'w') as output_file:
        output_file.write(result)

    print(f"Decryption complete. Decrypted text saved to '{output_name}'." )

# Call main function
main()
