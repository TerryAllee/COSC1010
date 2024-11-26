#
# Name: Terry Allee
# Date: Novmeber 24th 
# File Encryption and Decryption Programming Project
# COSC 1010 
#
# Use comments liberally throughout the program. 

import os
print(f"Current Working Directory: {os.getcwd()}")
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
    ' ': '_', '\n': '\n', '!': 'A', '@': 'B',
    '#': 'C', '$': 'D', '%': 'E', '^': 'F',
    '&': 'G', '*': 'H', '(': 'I', ')': 'J',
    '_': 'K', '-': 'L', '=': 'M', '+': 'N',
    '~': 'O', '`': 'P', '|': 'Q', ':': 'R',
    ';': 'S', '"': 'T', '<': 'U', '>': 'V',
    '/': 'W', ',': 'X', '.': 'Y', 'z': 'Z',
    '0': 'a', '1': 'b', '2': 'c', '3': 'd',
    '4': 'e', '5': 'f', '6': 'g', '7': 'h',
    '8': 'i', '9': 'j'
}

def main():
    # obtain the string for the converted text.
    result = convert()

    if result is None:
        #  Exit the program if an error is occured for the file handleing. 
        return

    # Ask user for the output file name
    output_name = input ('Enter the name of the output file:')
    
    # Write the encrypted text for the output file
    with open(output_name, 'w') as output_file:
        output_file.write(result)

    print(f"Encryption complete. Encrypted text saves to '{output_name}'." )

    # Convert the fuction that asks the user for the file name and opens the file
    # then converts the contents use the CODE listed above. 
    # Return the string with the converted text. 
def convert():
    # Ask the user for the input file name
    input_name = input("Enter the name of the input file: ").strip()
    print(f"Using input file: {input_name}")

    try:
        # open file in read mode
        with open(input_name, 'r') as input_file:
            text = input_file.read()
    except FileNotFoundError:
        print(f"Error: the file '{input_name}' was not found." )
        # Exit the function if the file is not found
        return None
    
    # Initializa an empty result string
    result = ''
    
    # Encrypt each character
    for ch in text:
        if ch.isspace():
            # Keep spaces and newlines as they are in the text. 
            result += ch
        else:
            # Encrypt character or leave alove
            result += CODE.get(ch, ch)

    return result


# Call main function

main()
    