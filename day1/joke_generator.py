# joke_generator.py

import random

# List of jokes
jokes = [
    "Why did the Python programmer break up with the JavaScript developer? Because they didn't get closure!",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It left its Windows open!",
    "Why do Python programmers prefer snakes? Because they slither through code with ease!"
]

# Pick a random joke
joke = random.choice(jokes)
print("Here's a joke for you: ")
print(joke)
