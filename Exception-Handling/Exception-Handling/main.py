#
# Name Terry Allee
# Date  10/28/2024
# Exception Handling Programming Project
# COSC 1010 
#
# Use comments liberally throughout the program. 
# calculating the average and handles the file and data conversion errors

def main():
    try:
        # Open the file to read
        infile = open('numbers.txt', 'r')

        # Declare local variable
        total = 0
        count = 0
        
        # Print contents and calculate the sum of the count for valid numbers
        print("File Contents:")
        # Loop through each line of the file
        for line in infile:
            #  Print each line 
            print(line.strip())

            try:
                # convert line to an integer
                number = int(line.strip())

                # add to total and increment count
                total += number
                
                # Add to count
                count +=1
        
            except ValueError:
                # handle lines that can not be converted to integers
                print(f"Warning: Could not convert line to integer: {line.strip()}")
        
        # close the file
        infile.close()

        # Calculate and display the average if there is valid data
        if count > 0:
            average = total / count
            print(f'\nThe average of the numbers is: {average}')
        else: 
            print('\nThe file is empty or contains no valid numbers to calculate the average')
    
    except IOError as e:
        # Handle an file-related errors
        print(f"An error occured and can not read the file: {e}")

# Call the main function
main()