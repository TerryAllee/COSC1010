#
# Name: Terry Allee
# Date: 10/19/2024
# Average of Numbers Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# Open the file to reading
with open('/Users/terrygarcia/Library/CloudStorage/GoogleDrive-terrydallee@gmail.com/My Drive/COSC1010/Average-of-Numbers/numbers.txt', 'r') as myfile:
    # Initialize variable to store the total sum and count the number
    total = 0
    count = 0

    # Create a loop that goes through each line in the file
    for line in myfile:
        # Convert the line into an integer and add it the total
        number = int(line)
        # Add to total
        total += number
        # Add to count
        count +=1

# Calculate the average
if count > 0:
    average = total / count
    print(f'the average of the numbers is: {average}')
else: 
    print('The file is empty, no numbers to calculate the average.')

