rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

# Rock wins against scissors.
# Scissors win against paper.
# Paper wins against rock.

def user_choice():
  
  u_c = input("What do you choose? Type 'r' for Rock, 'p' for Paper or 's' for Scissors.\n").lower()
  
  if u_c == "r":
    print("User choosed ", rock)
  elif u_c == "p":
    print("User choosed ", paper)
  elif u_c == "s":
    print("User choosed ", scissors)
  else:
    print("Invalid input!")

  return u_c

def computer_choice():
  choice = ["r", "p", "s"]
  c_c = random.choice(choice)
  
  if c_c == "r":
    print("Computer's choice", rock)
  elif c_c == "p":
    print("Computer's choice", paper)
  elif c_c == "s":
    print("Computer's choice ", scissors)

  return c_c

def play():
  u_c = user_choice()
  c_c = computer_choice()
  
  if u_c == "r" and c_c == "s" or u_c == "s" and c_c == "p" or u_c == "p" and c_c == "r":
    print("Congrats! You won!")
  elif u_c == c_c:
    print("Draw, keep going ;-)")
  else:
    print("Game Over. You lost.")

play()
