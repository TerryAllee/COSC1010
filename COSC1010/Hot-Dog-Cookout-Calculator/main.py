#
# Name: Terry Allee
# Date: September 15th, 2024
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

import math

# Input from user
people = int(input("Enter how many people will be attending cookout:"))
hot_dogs_per_person = int(input("Enter the number of hot dogs per person:"))

# Constants
HOT_DOGS_PER_PACKAGE = 10
BUNS_PER_PACKAGE = 8

# Local variables
total_hot_dogs = people * hot_dogs_per_person
total_buns = total_hot_dogs

# Calculations for the minimum packages required
hot_dogs_packages = math.ceil(total_hot_dogs / HOT_DOGS_PER_PACKAGE)
packages_buns = math.ceil(total_hot_dogs/BUNS_PER_PACKAGE)

# Calculations for leftovers
leftover_hot_dogs = (hot_dogs_packages * HOT_DOGS_PER_PACKAGE)
leftover_buns = (packages_buns * BUNS_PER_PACKAGE)

# Print the results
print("Minumum number of hot dog packages needed:{}".format(hot_dogs_packages))
print("Minumum number of hot dog buns needed:{}".format(packages_buns))
print("Number of hot dogs left over: {}".format(leftover_hot_dogs)) 
print("Number of hot dog buns left over:{}".format(leftover_buns))

#Enter how many people will be attending cookout:100
#Enter the number of hot dogs per person:3
#Minumum number of hot dog packages needed:30
#Minumum number of hot dog buns needed:38
#Number of hot dogs left over: 300
#Number of hot dog buns left over:304
#terrygarcia@Terrys-MacBook-Air ~ % 
