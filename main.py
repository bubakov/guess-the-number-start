#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import art
import random

print(art.logo)
print(art.greetings)

user_level_selection = input("Choose a dificulty. Type 'easy' or 'hard': ")

def hard_game():
  computer_number = random.randint(1, 100)
  print(f"{computer_number}")
  number_of_lives = 5
  continue_game = False
  while not continue_game:
    user_guess = int(input("Make a guess: "))
    if number_of_lives > 0:
      number_of_lives -= 1
      if user_guess > computer_number:
        print(f"Too high. \nYou have {number_of_lives} lives.")
      elif user_guess < computer_number:
        print(f"Too low. \nYou have {number_of_lives} lives.")
      else:
        print(f"You got it! The answer was {computer_number}")
        continue_game = True
    else:
      print(f"You are out of lives. You lose. Guessed number was {computer_number}.")
      return
  
def easy_game():
  computer_number = random.randint(1, 100)
  print(f"{computer_number}")
  number_of_lives = 10
  continue_game = False
  while not continue_game:
    user_guess = int(input("Make a guess: "))
    if number_of_lives > 0:
      number_of_lives -= 1
      if user_guess > computer_number:
        print(f"Too high. \nYou have {number_of_lives} lives.")
      elif user_guess < computer_number:
        print(f"Too low. \nYou have {number_of_lives} lives.")
      else:
        print(f"You got it! The answer was {computer_number}")
        continue_game = True
    else:
      print(f"You are out of lives. You lose. Guessed number was {computer_number}.")
      return
        
if user_level_selection == "hard":
  print("You have 5 lives.")
  hard_game()
else:
  print("You have 10 lives.")
  easy_game()







