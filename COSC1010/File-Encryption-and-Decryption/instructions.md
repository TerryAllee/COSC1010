# Instructions  

Write a program that uses a dictionary to assign “codes” to each letter of the alphabet. For example:

    codes = { ‘A’ : ‘%’, ‘a’ : ‘9’, ‘B’ : ‘@’, ‘b’ : ‘#’, ... }
Using this example, the letter `A` would be assigned the symbol `%`, the letter `a` would be assigned the number `9`, the letter `B` would be assigned the symbol `@`, and so forth.

The program should open a specified text file (text.txt is provided), read its contents, then use the dictionary to write an encrypted version of the file’s contents to a second file (encrypted.txt). Each character in the second file should contain the code for the corresponding character in the first file.

Write a second program that opens an encrypted file and displays its decrypted contents on the screen. Use encrypted.txt.