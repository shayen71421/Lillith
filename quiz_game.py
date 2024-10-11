# Python quiz game with user inputs

questions = []
options = []
answers = []
guesses = []
score = 0
num_questions = int(input("Enter the number of questions for the quiz: "))
for i in range(num_questions):
    print(f"\nQuestion {i + 1}:")
    question = input(f"Enter question {i + 1}: ")
    questions.append(question)
    option_set = []
    for j in range(4):
        option = input(f"Enter option {chr(65+j)}: ")
        option_set.append(f"{chr(65+j)}. {option}")
    options.append(option_set)
    answer = input("Enter the correct answer (A, B, C, or D): ").upper()
    answers.append(answer)
for question_num in range(num_questions):
    print("\n______________")
    print(f"Question {question_num + 1}: {questions[question_num]}")
    
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter your guess (A, B, C, or D): ").upper()
    guesses.append(guess)

    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"The correct answer is {answers[question_num]}")
print("\nQuiz Completed!")
print(f"Your score is: {score} out of {num_questions}")