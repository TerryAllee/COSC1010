#
# Name: Terry Allee
# Date: 10/19/2024
# File Display Programming Project
# COSC 1010 
#
# Use comments liberally throughout the program. 


# Open the file.
myfile = open('/Users/terrygarcia/Library/CloudStorage/GoogleDrive-terrydallee@gmail.com/My Drive/COSC1010/File-Display/numbers.txt', 'r')

# Read and display the file's contents.
for line in myfile:
    number = int(line)
    print(number)

# Close the file.
myfile.close()