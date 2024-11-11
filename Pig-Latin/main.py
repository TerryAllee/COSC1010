#
# Terry Allee
# November 10, 2024
# Pig Latin Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

# User inputs a sentence
sentence = input("Enter a sentence")

# Spilt sentence into separate words
words= sentence.split()

# Define function to convert the words to Pig Latin
def to_pig_latin(word):
    if len(word) == 1:
        return word + "ay"
    else:
        return word [1:] + word[0] + "ay"

# Convert each word to Pig Latin
pig_latin_words = [to_pig_latin(word) for word in words]

# combine the converted words into a sentence
pig_latin_sentence = "".join(pig_latin_words)

# Print the Pig Latin sentences
print("Pig Latin:", pig_latin_sentence)
