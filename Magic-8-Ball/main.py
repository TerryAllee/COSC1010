# Name Terry Allee
# November 3, 2024
# Magic 8 Ball Project
# COSC 1010
#

# Import the random module for random selection
import random

def main():
    # Declare local varaibles
    contents = ''

    # File path 8_ball_responses.txt file
    file_path = '8_ball_responses.txt'

    # List to for stored the repsonses
    responses = []
    # Try to open and read the file
    try:
        # Open the file to read
        infile = open(file_path, 'r')

        # Read in data and store the contents
        contents = infile.read()

        # Print contents to debug the file
        print("Contenct if 8_ball_responses.txt")
        print(contents)

        # Close fle after reading
        infile.close()

        # Repsond with indidual responses on a new line
        responses = contents.strip().split('\n')

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        # Quit program if file is not found
        return 
    
    # Ask the user to ask a question or press Return to exit
    user_input = input("Ask teh Magic 8 Ball a yes or no question (or press Return to quit):")

    # Continue as long as the user input is empty
    while user_input.strip():

        # Select a random response from the lsit
        response = random.choice(responses)

        # Print the response in the console
        print ("Magic 8 Ball says:", response)

        # User to ask another question or quit the program
        user_input = input("\nAsk anotehr yes or no question (or press RETURN to quit)")
    
    # Print goodbye message with the user quits
    print("Goodbye! Remember, the Magic 8 Ball is here for more questions.")

# Run the main function when this file is executed
    __name__ == '__main__';
    main()
