print("My First Python Code")
print("My Second Python Code")

print("Hello", end="")
print("World")

name = "Alex"
age = 20
print(f"{name} is {age} years old")

name_2 = "Alice"
print("Hello" + name_2)
print("{} is {} years old".format("Alice",30))
################################################################
print()

print(342+699)
print(265 + 5924)
print(5022 - 901)
print(5 * 10)
print(604 / 4)
print(3 % 2)
print(10 % 4)
print(9 // 3)
print(8 // 3)#
print(5 ** 2)
print(4 ** 3)

a = 265
b = 5924
result = a + b
print("a + b =", result)

print()

a = 6
b = 4
c = 5
d = 2
e = 4
f = 3

print((a * b) + (c ** d) - (e % f))
##############################################################
print()

import random

# List of random responses to be given after each answer
responses = [
    "Cool!",
    "Nice!",
    "Wow, great!"
]

# Function to ask a question and provide a random response
def ask_question(question):
    answer = input(question + " ")
    print(random.choice(responses))
    print()  # For spacing between questions
    
    # List of questions to be filled in by students
    questions = [
        "What's your favorite hobby?",    # Example question
        "What's your favorite movie?",
        "What's your name?",
        "What's your favorite animal?",
]

# Function to randomly select and ask two questions
def icebreaker():
    print("Let's break the ice! I'll ask you two random questions:")
    selected_questions = random.sample(question, 2)  # Randomly select 2 questions
    for question in selected_questions:
        ask_question(question)
           
# Call the icebreaker function to start the program
icebreaker()