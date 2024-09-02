#
# Name Terry Allee
# Date September 1st, 2024
# Sales Prediction Programming Project
# COSC 2409 DNT
#

# Variables to hold the sales total and the profit

# Get the amount of projected sales.
total_sales = float(input('Enter the projected sales:'))
# Calculate the projected profit.
profit = total_sales * 0.23
# print the projected profit.
#print ('The profit is $', format(profit, ', .2f'))
print ('The profit is $%.2f' % profit)
#print (f'The profit is ${profit}')
