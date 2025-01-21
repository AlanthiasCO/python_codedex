# Hello! My name is Alan and I live in Brazil.
# I study Computer Science and I took a 2y break from coding in Python.
# Your course is helping me to remember and improve my skills. Thank you very much!
# Note: I used automatic translators to write this comment, so I apologize if there are any errors
# in English or anything like that.

import random

print("Welcome to the Terminal Adventure Game!")
print("You find yourself in a dark forest with two paths ahead.")
print("1. Take the left path")
print("2. Take the right path")
choice = input("Enter 1 or 2: ")

if choice == "1":
    print("You took the left path and encountered a wild animal!")
    print("1. Fight the animal")
    print("2. Run away")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("You decided to fight the animal!")
        # use random.randint (Return a number between 0 and 1 (both included))
        # source: https://www.w3schools.com/python/ref_random_randint.asp
        if random.randint(0, 1) == 0:
            print("You defeated the animal! You win!")
        else:
            print("The animal hit you and you start bleeding.")
            sub_choice = input("Do you want to continue fighting (1) or run away (2)? ")
            if sub_choice == "1":
                if random.randint(0, 1) == 0:
                    print("You defeated the animal! You win!")
                else:
                    print("The animal defeated you. Game over.")
            elif sub_choice == "2":
                print("You ran away safely. You win!")
            else:
                print("Invalid choice. The animal defeated you. Game over.")
    elif choice == "2":
        print("You ran away safely. You win!")
    else:
        print("Invalid choice. Please try again.")
elif choice == "2":
    print("You took the right path and found a treasure chest!")
    print("1. Open the chest")
    print("2. Ignore the chest and move on")
    choice = input("Enter 1 or 2: ")
    if choice == "1":
        print("You opened the chest and found a magical sword! You win!")
    elif choice == "2":
        print("You ignored the chest and moved on. You win!")
    else:
        print("Invalid choice. Please try again.")
else:
    print("Invalid choice. Please try again.")

# TO-DO: Add more paths, choices, and outcomes to the game
# TO-DO: Improve the game with more complex logic and interactions
# TO-DO: Add a scoring system and multiple levels to the game