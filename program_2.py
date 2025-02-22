# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.  
# If the answer is correct, a message of congratulations should be displayed.  
# If the answer is incorrect a message showing the correct answer should be displayed.  
# The program must use a function that accomplishes part of the needed tasks.

import random

def generate_question():
    num1 = random.randint(100, 500)
    num2 = random.randint(500, 900)
    return num1, num2

def math_quiz():
    num1, num2 = generate_question()
    print(f"\n   {num1}\n+  {num2}\n------")

    user_answer = int(input("Your answer: "))
    correct_answer = num1 + num2

    if user_answer == correct_answer:
        print("Congratulations! That's correct!")
    else:
        print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.")

math_quiz()
