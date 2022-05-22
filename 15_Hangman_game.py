import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["testing", "production", "bugs", "hotfix", "frontend"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

def guess_letter():
  lives = 6
  display = []

  #Add underscores to the list
  for _ in range(word_length):
      display += "_"

  #Guessing letters...
  while "_" in display:
    guess = input("Guess a letter: ").lower()
    
    #Check guessed letter
    for position in range(word_length):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
        print("Guessed, continue...")
        print(f"{''.join(display)}")

    #While there are letters to guess - count lives
    if guess not in chosen_word:
      lives -= 1
      print(stages[lives])
    if lives == 0:
      print("Sorry, you lose.")
      
  print("Wohooo! Guessed word => ", f"{''.join(display)}")

guess_letter()
