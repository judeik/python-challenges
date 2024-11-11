# Task 5: Store a list of words and create a new list with words of odd length.

# Define a list of words
words = ["apple", "banana", "cherry", "date", "elderberry"]

# Use list comprehension to create a new list with only words that have an odd number of characters
odd_length_words = [word for word in words if len(word) % 2 != 0]

# Print the new list containing words with an odd number of characters
print("Words with an odd number of characters:", odd_length_words)
