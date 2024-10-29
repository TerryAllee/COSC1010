#
# Name: Terry Allee 
# Date: October 28, 2024
# Lottery Number Generator Programming Project
# COSC 1010 
#
# Use comments liberally throughout the program. 

import random

# Use max number of digits
MAX_DIGITS = 7 
# Start with 0 for the number range
START = 0
# End with 9 on the random number range 
END = 9

# main function
def main():
    # Create the list
    numbers = [0] * 7

    # Populate the list with the random numbers
    for index in range(MAX_DIGITS):
        numbers[index] = random.randint(START, END)

    # Display the random numbers.
    print('Here are your lottery numbers:')
    for index in range(MAX_DIGITS) :
        print(numbers[index], end='')
    print()

# Call teh main function.
main()