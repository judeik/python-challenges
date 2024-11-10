# quiz_game.py

# Define questions and answers
questions = {
    "What is the capital of France?": "a) Paris\nb) Berlin\nc) Rome\n",
    "Which language is known as the language of the web?": "a) Python\nb) HTML\nc) JavaScript\n",
    "Which planet is known as the Red Planet?": "a) Earth\nb) Mars\nc) Jupiter\n"
}
answers = {"What is the capital of France?": "a", "Which language is known as the language of the web?": "b", "Which planet is known as the Red Planet?": "b"}

# Start the quiz
score = 0
for question, options in questions.items():
    print(question)
    print(options)
    answer = input("Your answer (a/b/c): ").lower()
    if answer == answers[question]:
        print("Correct!\n")
        score += 1
    else:
        print("Oops! That's incorrect.\n")

# Display score
print(f"Your final score is: {score}/{len(questions)}")
