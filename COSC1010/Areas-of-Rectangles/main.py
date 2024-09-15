#
# Name: Terry Allee
# Date: 9/15/2024
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
length_a = .0
width_a = .0
length_b = .0
width_b = .0
area_a = .0
area_b = .0


# Get length A
length_a = float(input("Enter the length of rectangle A: "))

# Get width A
width_a = float(input("Enter with width of rectangle A: "))

# Get length B
length_b = float(input("Enter the length of rectangle B: "))

# Get width B
width_b= float(input("Enter with width of rectangle B: "))

# Calculate area A
area_a = length_a * width_a

# Calculate area B
area_b = length_b * width_b

# Print area comparison using if-elif-else statements
if area_a > area_b:
    print("Rectangle A has a larger area than Rectangle B.")
elif area_b > area_a:
    print("Rectangle B has a larger area than Rectangle A.")
else:
    print ("Both rectangles have the same area")



# below is the screen shot that the code is running:
#terrygarcia@Terrys-MacBook-Air ~ % /usr/bin/python3 "/Users/terrygarcia/Library/CloudStorage/GoogleDrive-terrydallee@gmail.com/My Drive/COSC1010/Areas-of-Rec
#tangles/main.py"
#Enter the length of rectangle A: 89
#Enter with width of rectangle A: 89
#Enter the length of rectangle B: 90
#Enter with width of rectangle B: 89
#Rectangle B has a larger area than Rectangle A.
#errygarcia@Terrys-MacBook-Air ~ % 
