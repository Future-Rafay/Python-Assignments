# Problem Statement:
# Write a simple joke bot. The bot starts by asking the user what they want.
# However, your program will only respond to one response: Joke.
#
# If the user enters Joke then we will print out a single joke.
# Each time the joke is always the same:
#
# "Here is a joke for you! Panaversity GPT - Sophia is heading out to the grocery store.
# A programmer tells her: get a liter of milk, and if they have eggs, get 12.
# Sophia returns with 13 liters of milk.
# The programmer asks why and Sophia replies: 'because they had eggs'"
#
# If the user enters anything else we print out:
# "Sorry I only tell jokes"
#
# You should use three constants:
# PROMPT, JOKE, and SORRY.
# The program uses an if-statement: if user_input == "Joke"

import random

def get_random_joke() -> str:
    jokes: list[str] = [
        "Why do programmers prefer dark mode? Because light attracts bugs. 🐛💡",
        "Why do Java developers wear glasses? Because they can't C#. 🤓",
        "What's a programmer's favorite hangout place? The Foo Bar. 🍻",
        "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?' 🍷",
        "There are 10 types of people in the world: those who understand binary and those who don't. 💾",
        "Why was the developer unhappy at their job? They wanted arrays. 😢➡️😊",
        "How do you comfort a JavaScript bug? You console it. 🖥️",
        "Why did the functions break up? Because they had constant arguments. 💔",
        "Why did the programmer quit their job? Because they didn't get arrays (a raise). 🤑",
        "I would tell you a joke about recursion... but you'd have to hear it again. 🔁"
    ]
    return random.choice(jokes)

def greet_user():
    print("👋 Welcome to the Programmer Joke Bot!")
    print("Type 'joke' to hear a joke 🤖")
    print("Type 'exit' or press Enter to quit 🚪\n")

def main():
    greet_user()

    while True:
        user_input: str = input("What do you want? 👉 ").strip().lower()

        if user_input == "joke":
            print(f"\n😂 Here's your joke:\n{get_random_joke()}\n")
        elif user_input == "exit" or user_input == "":
            print("👋 Goodbye, and don't forget to debug with a smile!")
            break
        else:
            print("❌ Sorry, I only tell programmer jokes. Type 'joke' or 'exit'.\n")

if __name__ == '__main__':
    main()
