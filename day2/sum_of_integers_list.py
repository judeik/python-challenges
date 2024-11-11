# Task 1: Accept user input to create a list of integers, then compute the sum.

# Prompt the user to enter a list of integers separated by spaces
numbers = input("Enter a list of integers separated by spaces: ")

# Convert the input string into a list of integers
int_list = [int(num) for num in numbers.split()]

# Calculate the sum of all integers in the list
total_sum = sum(int_list)

# Print the total sum of the integers
print("The sum of all integers in the list is:", total_sum)
