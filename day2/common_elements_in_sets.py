# Task 4: Accept user input to create two sets and find common elements.

# Prompt the user to enter integers for the first set, separated by spaces
set1 = set(map(int, input("Enter integers for the first set separated by spaces: ").split()))

# Prompt the user to enter integers for the second set, separated by spaces
set2 = set(map(int, input("Enter integers for the second set separated by spaces: ").split()))

# Find common elements by calculating the intersection of the two sets
common_elements = set1.intersection(set2)

# Print the set of common elements
print("Common elements in both sets:", common_elements)
