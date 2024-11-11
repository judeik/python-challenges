# Task 3: Use a dictionary to store information about a person.

# Create an empty dictionary to hold the person's information
person_info = {}

# Prompt the user for their name and store it in the dictionary
person_info["name"] = input("Enter your name: ")

# Prompt the user for their age, convert it to an integer, and store it in the dictionary
person_info["age"] = int(input("Enter your age: "))

# Prompt the user for their favorite color and store it in the dictionary
person_info["favorite_color"] = input("Enter your favorite color: ")

# Print the complete dictionary containing the person's information
print("Person Information:", person_info)
