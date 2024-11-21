#
# Terry Allee
# November 17, 2024
# Capital Quiz Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import random

# Constant for the number fo the states to quiz user. 
NUM_STATES = 5

def main():
    # Initalize the state_caps dictionary.
    state_caps = state_cap_dictionary()

    # NUM_STATES is not greater than teh number of states
    if NUM_STATES > len(state_caps):
        print("Error: NUM_STATES exceeds the number of states.")
        return

    # Initialize variable to keep count of the number of correct and incorrect answers
    correct = 0
    incorrect = 0
    try:
        # Quiz the user
        for count in range(NUM_STATES):
            # Get a random entry from the dictionary
            state, capital = random.choice(list(state_caps.items()))

            # Quiz the user
            print('What is the capital of', state, '?', end='')
            response = input().strip()

            # validate input and keep asking until user provides a response
            while not response:
                print("Input can not be blank. Try again")
                response = input().strip()

            # Check if the user is correct?
            if response.lower() == capital.lower():
                correct+= 1 
                print('Correct!')
            else:
                incorrect += 1
                print('Incorrect.')
    except KeyboardInterrupt:
        # Handles a CTRL + C interruptions    
        print("\nQuiz interrupted by the user. Goodbye!")
        return
    
    # Display the results.
    print ('Correct responses:', correct)
    print ('Incorrect responses:', incorrect)



# The state_cap_dictionary functions builds the dictionary that contain the names of the U.S. states and their capitals. 
# and returns a reference to the dictionary. 

# Define the state_cap_dictionary function
def state_cap_dictionary():
    return {
        'Alabama':'Montgomery', 'Alaska':'Juneau',
        'Arizona':'Phoenix', 'Arkansas':'Little Rock',
        'California':'Sacramento', 'Colorado':'Denver',
        'Connecticut':'Hartford', 'Delaware':'Dover',
        'Florida':'Tallahassee', 'Georgia':'Atlanta',
        'Hawaii':'Honolulu', 'Idaho':'Boise',
        'Illinois':'Springfield', 'Indiana':'Indianapolis',
        'Iowa':'Des Moines', 'Kansas':'Topeka',
        'Kentucky':'Frankfort', 'Louisiana':'Baton Rouge',
        'Maine':'Augusta', 'Maryland':'Annapolis',
        'Massachusetts':'Boston', 'Michigan':'Lansing',
        'Minnesota':'Saint Paul', 'Mississippi':'Jackson',
        'Missouri':'Jefferson City', 'Montana':'Helena',
        'Nebraska':'Lincoln', 'Nevada':'Carson City',
        'New Hampshire':'Concord', 'New Jersey':'Trenton',
        'New Mexico':'Santa Fe', 'New York':'Albany',
        'North Carolina':'Raleigh', 'North Dakota':'Bismarck',
        'Ohio':'Columbus', 'Oklahoma':'Oklahoma City',
        'Oregon':'Salem', 'Pennsylvania':'Harrisburg',
        'Rhode Island':'Providence', 'South Carolina':'Columbia',
        'South Dakota':'Pierre', 'Tennessee':'Nashville',
        'Texas':'Austin', 'Utah':'Salt Lake City',
        'Vermont':'Montpelier', 'Virginia':'Richmond',
        'Washington':'Olympia', 'West Virginia':'Charleston',
        'Wisconsin':'Madison', 'Wyoming':'Cheyenne'
    }

    # Local variables

    # Continue until user quits the game.

# Call the main function.
main()#
